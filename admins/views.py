from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Products
from user.models import Orders,Ratings
from django.db.models import Count,Avg

def logins(request):
    context=""
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return redirect('admins:home')
        else:
            context = "username and password wrong"
    return render(request, 'admins/login.html',{'context':context})

def home(request):
    prod=Products.objects.all()
    return render(request, 'admins/home.html',{'prod':prod})
    
def uploadProduct(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        book = form.save()
        return redirect('admins:home')
    return render(request, 'admins/uploadProduct.html', {'form':form})
    
def viewratings(request):
    ratings=Ratings.objects.all()
    return render(request, 'admins/viewratings.html',{'ratings':ratings})
    
def orderedproducts(request):
    order=Orders.objects.filter(status='pending')
    return render(request, 'admins/orderedproducts.html',{'order':order})
    
def confirmedproduct(request):
    order=Orders.objects.filter(status='confirmed')
    return render(request, 'admins/confirmedproduct.html',{'order':order})
    
def graph(request,chart_type):
    template_name = 'admins/graph.html'
    prod=Ratings.objects.all().values('product','product__name').annotate(ratings=Avg('ratings'))
    prod1=0
    
    if chart_type == 'products':
        prod=Ratings.objects.all().values('product__name').annotate(ratings=Avg('ratings'))
        template_name = 'admins/graph.html'
    elif chart_type == 'category':
        prod=Ratings.objects.all().values('product__category').annotate(ratings=Avg('ratings'))
        template_name = 'admins/graph1.html'
    elif chart_type == 'sentiment':
        prod=Ratings.objects.filter(sentiments='positive').values('product__name').annotate(ratings=Count('sentiments'))
        prod1=Ratings.objects.filter(sentiments='negative').values('product__name').annotate(ratings=Count('sentiments'))
        template_name = 'admins/graph2.html'
    return render(request, template_name,{'prod':prod,'prod1':prod1,'chart_type':chart_type})