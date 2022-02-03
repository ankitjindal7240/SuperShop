from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import Product,Contact
def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        allProds.append([prod,range(len(prod))])

    params={'allProds':allProds }
    return render(request, 'shop/index.html',params)
def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method=="POST":
        # print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        # print(name,email,phone, desc )
    return render(request, "shop/contact.html")

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')