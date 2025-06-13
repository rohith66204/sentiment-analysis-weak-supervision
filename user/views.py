from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, OrderForm, RatingsForm
from admins.models import Products
from .models import Orders, Ratings
from .sensitive1 import naive_bayes
from django.db.models import Count, Avg


@login_required(login_url='users:login')
def home(request):
    prod = Products.objects.all()
    form = OrderForm(request.POST)
    if 'addcart' in request.POST:
        if form.is_valid():
            frm = form.save(commit=False)
            frm.user = request.user
            pr = request.POST.get("idu")
            prd = get_object_or_404(Products, id=pr)
            frm.prod = prd
            prd.stock = prd.stock - frm.prodqty
            prd.save(update_fields=["stock"])
            frm.save()
            return redirect('users:home')
        else:
            form = OrderForm(request.POST)
    elif 'vieratg' in request.POST:
        return redirect('users:home')

    return render(request, 'home.html', {'prod': prod, 'form': form})


def registration(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()  # load the profile instance created by the signal
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        return redirect('users:login')
    return render(request, 'signup.html', {'form': form})


def yourorders(request):
    pror = Orders.objects.filter(user=request.user, status='pending')
    if request.method == 'POST':
        if 'updates' in request.POST:
            idy = request.POST.get("idy")
            qty = request.POST.get("qty")
            loc = request.POST.get("loc")
            ord = get_object_or_404(Orders, id=idy)
            prd = get_object_or_404(Products, id=ord.prod.id)
            if prd.stock > 0:
                if ord.prodqty > int(qty):
                    ort = ord.prodqty - int(qty)
                    prd.stock = prd.stock + ort
                elif ord.prodqty < int(qty):
                    ort = int(qty) - ord.prodqty
                    prd.stock = prd.stock + ort
                elif ord.prodqty == int(qty):
                    prd.stock = int(qty)
            else:
                prd.stock = 0
            ord.prodqty = qty
            ord.location = loc
            ord.save(update_fields=["prodqty", "location"])
            prd.save(update_fields=["stock"])
        elif 'cancel' in request.POST:
            idys = request.POST.get("idys")
            ord = get_object_or_404(Orders, id=idys)
            prd = get_object_or_404(Products, id=ord.prod.id)
            prd.stock = prd.stock + ord.prodqty
            prd.save(update_fields=["stock"])
            ord.delete()
    return render(request, 'yourorders.html', {'pror': pror})


def confirmproducts(request):
    pror = Orders.objects.filter(user=request.user, status='confirmed')
    return render(request, 'confirmed.html', {'prod': pror})


def chechouts(request):
    Orders.objects.filter(user=request.user).update(status='confirmed')
    return redirect('users:home')


def viewratings(request, pk):
    productdetails = get_object_or_404(Products, pk=pk)
    ratings = Ratings.objects.filter(product=productdetails)
    if request.method == 'POST':
        if 'rtngbtn' in request.POST:
            rati = request.POST.get("ratings")
            review = request.POST.get("review")
            result = naive_bayes(review)
            if result['1'] > result['-1']:
                res = 'positive'
            else:
                res = 'negative'
            rev_instance = Ratings.objects.create(
                user=request.user, product=productdetails, ratings=rati, reviews=review, sentiments=res)
    return render(request, 'viewratings.html', {'productdetails': productdetails, 'ratings': ratings})


def productlist(request):
    vallit = Products.objects.values('category').distinct()
    prod = Products.objects.all()
    return render(request, 'topproducts.html', {'prod': prod, 'vallit': vallit})


def topproducts(request):
    prod = Ratings.objects.all().values('product__name').annotate(
        rati=Avg('ratings')).order_by('-rati')
    return render(request, 'productlist.html', {'prod': prod})


def graphs(request):
    prod = Ratings.objects.all().values('product__name').annotate(
        ratings=Avg('ratings'))
    return render(request, 'graphs.html', {'prod': prod})

