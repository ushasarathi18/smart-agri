import qrcode, io, base64
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Order
from apps.products.models import Product

def _qr(data):
    img = qrcode.make(data); buf = io.BytesIO(); img.save(buf, format='PNG')
    return 'data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()

@api_view(['POST'])
def create_order(request):
    d = request.data
    try: p = Product.objects.get(pk=d['product_id'])
    except Product.DoesNotExist: return Response({'error':'product not found'}, status=404)
    qty = int(d.get('quantity',1))
    if qty > p.stock: return Response({'error':'insufficient stock'}, status=400)
    base = float(p.selling_price)*qty
    gst = round(base*0.05,2)
    transport = 100.0
    total = round(base+gst+transport,2)
    o = Order.objects.create(user=request.user if request.user.is_authenticated else None,
                             product=p, quantity=qty, base_price=base, gst=gst,
                             transport=transport, total_price=total,
                             payment_method=d.get('payment_method','cod'),
                             address=d.get('address',''), state=d.get('state',''))
    # Decrement live stock
    p.stock -= qty; p.sold += qty; p.save()
    upi = f'upi://pay?pa=smartagri@upi&pn=SmartAgri&am={total}&cu=INR&tn=Order{o.id}'
    return Response({'order_id':o.id,'base_price':base,'gst':gst,'transport':transport,
                      'total':total,'payment_method':o.payment_method,
                      'qr_code':_qr(upi),'upi_link':upi,
                      'remaining_stock':p.stock})

@api_view(['GET'])
def my_orders(request):
    if not request.user.is_authenticated: return Response([])
    return Response([{'id':o.id,'product':o.product.title if o.product else 'N/A',
                      'quantity':o.quantity,'total':float(o.total_price),
                      'status':o.status,'payment':o.payment_method,
                      'date':o.created_at.strftime('%d-%m-%Y %H:%M')}
                     for o in Order.objects.filter(user=request.user)])

@api_view(['GET'])
def invoice(request, pk):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    try: o = Order.objects.get(pk=pk)
    except Order.DoesNotExist: return Response({'error':'not found'}, status=404)
    resp = HttpResponse(content_type='application/pdf')
    resp['Content-Disposition'] = f'attachment; filename=invoice_{pk}.pdf'
    c = canvas.Canvas(resp, pagesize=A4)
    c.setFont('Helvetica-Bold',18); c.drawString(50,800,'SMART AGRI - INVOICE')
    c.setFont('Helvetica',11)
    y=760
    for line in [f'Order #{o.id}', f'Date: {o.created_at.strftime("%d-%m-%Y")}',
                 f'Product: {o.product.title if o.product else "N/A"}',
                 f'Quantity: {o.quantity}', f'Base: Rs.{o.base_price}',
                 f'GST(5%): Rs.{o.gst}', f'Transport: Rs.{o.transport}',
                 f'TOTAL: Rs.{o.total_price}', f'Payment: {o.payment_method}',
                 f'Status: {o.status}', f'Address: {o.address}']:
        c.drawString(50,y,line); y-=22
    c.drawString(50,y-20,'Thank you for shopping with Smart Agri!')
    c.save(); return resp
