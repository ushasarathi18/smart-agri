"""Seed default users + sample products. Run after migrations."""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','agri_project.settings')
django.setup()
from django.contrib.auth.models import User
from apps.accounts.models import Profile
from apps.products.models import Category, Product

defaults = [('admin','admin123','admin',True,True),
            ('seller','seller123','seller',False,True),
            ('vendor','vendor123','vendor',False,True),
            ('user','user123','user',False,False)]
for u,p,r,sup,staff in defaults:
    if not User.objects.filter(username=u).exists():
        usr = User.objects.create_user(username=u,password=p,email=f'{u}@smartagri.in')
        usr.is_superuser=sup; usr.is_staff=staff; usr.save()
        Profile.objects.create(user=usr, role=r, verified=True)
        print(f'created {u}/{p}')

cats = [('Seeds','seeds'),('Fertilizers','fertilizers'),('Pesticides','pesticides'),
        ('Machinery','machinery'),('Irrigation','irrigation'),('Crops','crops')]
for n,s in cats: Category.objects.get_or_create(slug=s, defaults={'name':n})

seller = User.objects.get(username='seller')
samples = [
    ('Premium Ragi Seeds 1kg','seeds',180,250,500,'Red soil','Sow in Jun-Jul, harvest in Oct-Nov.'),
    ('Urea Fertilizer 50kg','fertilizers',280,320,200,'All','Apply 50kg/acre during tillering.'),
    ('Mancozeb 75% WP 500g','pesticides',180,240,150,'-','For leaf spot. 2g/L water spray.'),
    ('Mini Tractor 25HP','machinery',280000,350000,5,'-','4WD, suitable for 2-5 acre farms.'),
    ('Drip Irrigation Kit','irrigation',8500,11000,40,'-','Covers 1 acre, 15-year UV pipe.'),
    ('Hybrid Tomato Seeds 50g','seeds',120,180,300,'Loamy','Transplant in 25 days.'),
    ('Organic Neem Spray 1L','pesticides',280,380,80,'-','100% organic. 5ml/L water.'),
    ('Power Sprayer 16L','machinery',3200,4500,25,'-','Battery operated, 8hr backup.'),
    ('Premium Basmati Rice 25kg','crops',2200,2800,100,'Alluvial','Direct from Punjab farms.'),
    ('NPK 19:19:19 Fertilizer 25kg','fertilizers',1200,1500,60,'All','Balanced nutrient mix.'),
]
for t,c,bp,sp,st,soil,guide in samples:
    if not Product.objects.filter(title=t).exists():
        Product.objects.create(seller=seller, category=Category.objects.get(slug=c),
                                title=t, buying_price=bp, selling_price=sp, stock=st,
                                soil_suitability=soil, cultivation_guide=guide,
                                description=f'High quality {t}. Trusted by 1000+ farmers.',
                                image_url=f'https://placehold.co/400x300/2e7d32/fff?text={t[:20].replace(" ","+")}',
                                state='karnataka')
print('Seed complete:', User.objects.count(), 'users,', Product.objects.count(), 'products')
