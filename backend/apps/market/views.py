import csv, statistics, datetime
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

def _read():
    rows = []
    try:
        with open(settings.CSV_DATA_PATH, newline='') as f:
            for r in csv.DictReader(f):
                try:
                    rows.append({'crop':r['crop'].lower(),'location':r['location'].lower(),
                                  'date':r['date'],
                                  'buying_price':float(r['buying_price']),
                                  'selling_price':float(r['selling_price'])})
                except: continue
    except FileNotFoundError: pass
    return rows

@api_view(['GET'])
def crops(_):
    return Response(sorted({r['crop'] for r in _read()}))

@api_view(['GET'])
def locations(_):
    return Response(sorted({r['location'] for r in _read()}))

@api_view(['GET'])
def history(request):
    crop = request.GET.get('crop','rice').lower()
    loc = request.GET.get('location','karnataka').lower()
    data = [r for r in _read() if r['crop']==crop and r['location']==loc]
    data.sort(key=lambda x: datetime.datetime.strptime(x['date'],'%d-%m-%Y'))
    if not data: return Response({'error':'No data','data':[]}, status=404)
    cur = data[-1]
    # Simple linear forecast (TODO: replace with ARIMA/LSTM)
    sells = [d['selling_price'] for d in data[-6:]]
    avg_change = sum(sells[i+1]-sells[i] for i in range(len(sells)-1))/max(1,len(sells)-1)
    last = data[-1]['selling_price']
    forecast = []
    base = datetime.datetime.strptime(data[-1]['date'],'%d-%m-%Y')
    for i in range(1,5):
        last = round(last+avg_change,2)
        forecast.append({'date':(base+datetime.timedelta(weeks=4*i)).strftime('%d-%m-%Y'),
                         'predicted_price':last})
    # Best location to sell
    all_rows = [r for r in _read() if r['crop']==crop]
    by_loc = {}
    for r in all_rows: by_loc.setdefault(r['location'],[]).append(r)
    latest_by_loc = {l: max(rs, key=lambda x: datetime.datetime.strptime(x['date'],'%d-%m-%Y'))['selling_price']
                     for l,rs in by_loc.items()}
    best_sell = max(latest_by_loc.items(), key=lambda x: x[1]) if latest_by_loc else (loc,0)
    best_buy = min(latest_by_loc.items(), key=lambda x: x[1]) if latest_by_loc else (loc,0)
    return Response({
        'crop':crop,'location':loc,
        'current':{'date':cur['date'],'buying_price':cur['buying_price'],'selling_price':cur['selling_price']},
        'history':data,'forecast':forecast,
        'best_sell_location':{'name':best_sell[0],'price':best_sell[1]},
        'best_buy_location':{'name':best_buy[0],'price':best_buy[1]},
        'india_average':round(statistics.mean(latest_by_loc.values()),2) if latest_by_loc else 0,
    })

@api_view(['GET'])
def compare(request):
    crop = request.GET.get('crop','rice').lower()
    rows = [r for r in _read() if r['crop']==crop]
    by_loc = {}
    for r in rows:
        by_loc.setdefault(r['location'],[]).append(r)
    out = []
    for loc, rs in by_loc.items():
        rs.sort(key=lambda x: datetime.datetime.strptime(x['date'],'%d-%m-%Y'))
        out.append({'location':loc,'latest_selling':rs[-1]['selling_price'],
                    'latest_buying':rs[-1]['buying_price']})
    out.sort(key=lambda x:-x['latest_selling'])
    return Response(out)

@api_view(['GET'])
def dynamic_price(request):
    """Dynamic pricing engine — adjusts based on weather/season/supply/demand factors.
    TODO: integrate real weather API + supply/demand from order data."""
    crop = request.GET.get('crop','rice').lower()
    loc = request.GET.get('location','karnataka').lower()
    rows = [r for r in _read() if r['crop']==crop and r['location']==loc]
    if not rows: return Response({'error':'No data'}, status=404)
    base = rows[-1]['selling_price']
    season_factor = 1.05  # TODO real season detection
    weather_factor = 1.02 # TODO real weather API
    demand_factor = 1.03  # TODO from orders
    festival_factor = 1.01
    govt_factor = 1.00
    dynamic = round(base*season_factor*weather_factor*demand_factor*festival_factor*govt_factor,2)
    return Response({'crop':crop,'location':loc,'base_price':base,
                      'dynamic_price':dynamic,
                      'factors':{'season':season_factor,'weather':weather_factor,
                                  'demand':demand_factor,'festival':festival_factor,'govt':govt_factor}})
