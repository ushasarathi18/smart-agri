from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Review, Wishlist, CartItem

def _ser(p):
    return {'id':p.id,'title':p.title,'description':p.description,
            'image_url':p.image_url or 'https://placehold.co/400x300?text='+p.title.replace(' ','+'),
            'buying_price':float(p.buying_price),'selling_price':float(p.selling_price),
            'stock':p.stock,'sold':p.sold,
            'category':p.category.name if p.category else None,
            'soil_suitability':p.soil_suitability,'cultivation_guide':p.cultivation_guide,
            'storage_info':p.storage_info,'safety_info':p.safety_info,
            'state':p.state,'seller':p.seller.username if p.seller else 'SmartAgri',
            'reviews_count':p.reviews.count(),
            'avg_rating':round(sum(r.rating for r in p.reviews.all())/max(1,p.reviews.count()),1),
            'in_stock': p.stock > 0}

@api_view(['GET'])
def list_products(request):
    qs = Product.objects.filter(is_active=True)
    cat = request.GET.get('category')
    q = request.GET.get('q')
    if cat: qs = qs.filter(category__slug=cat)
    if q: qs = qs.filter(title__icontains=q)
    return Response([_ser(p) for p in qs])

@api_view(['GET'])
def detail(request, pk):
    try: p = Product.objects.get(pk=pk)
    except Product.DoesNotExist: return Response({'error':'not found'}, status=404)
    data = _ser(p)
    data['reviews'] = [{'user':r.user.username if r.user else 'anon','rating':r.rating,
                        'comment':r.comment,'verified':r.verified_purchase,
                        'date':r.created_at.strftime('%d-%m-%Y')} for r in p.reviews.all()]
    return Response(data)

@api_view(['GET'])
def categories(_):
    return Response([{'name':c.name,'slug':c.slug} for c in Category.objects.all()])

@api_view(['POST'])
def add_review(request, pk):
    if not request.user.is_authenticated: return Response({'error':'login'}, status=401)
    p = Product.objects.get(pk=pk)
    Review.objects.create(product=p, user=request.user,
                          rating=int(request.data.get('rating',5)),
                          comment=request.data.get('comment',''),
                          verified_purchase=False)  # TODO: verify after order completion
    return Response({'ok':True})

@api_view(['POST'])
def add_to_cart(request, pk):
    if not request.user.is_authenticated: return Response({'error':'login'}, status=401)
    p = Product.objects.get(pk=pk)
    qty = int(request.data.get('quantity',1))
    if qty > p.stock: return Response({'error':'Insufficient stock'}, status=400)
    item,_ = CartItem.objects.get_or_create(user=request.user, product=p, defaults={'quantity':0})
    item.quantity += qty; item.save()
    return Response({'ok':True})

@api_view(['POST'])
def toggle_wishlist(request, pk):
    if not request.user.is_authenticated: return Response({'error':'login'}, status=401)
    p = Product.objects.get(pk=pk)
    w = Wishlist.objects.filter(user=request.user, product=p).first()
    if w: w.delete(); return Response({'wishlisted':False})
    Wishlist.objects.create(user=request.user, product=p); return Response({'wishlisted':True})

@api_view(['GET'])
def cart(request):
    if not request.user.is_authenticated: return Response([])
    items = CartItem.objects.filter(user=request.user)
    return Response([{'id':i.id,'product':_ser(i.product),'quantity':i.quantity,
                      'total':float(i.product.selling_price)*i.quantity} for i in items])
