from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views as ind_views
from .forms import CustomAuthForm

app_name = 'users'  # Namespace for reverse URL lookups

urlpatterns = [
    # Home page
    path('home/', ind_views.home, name='home'),
    
    # Authentication URLs
    path('', auth_views.LoginView.as_view(
        template_name='login.html',
        authentication_form=CustomAuthForm
    ), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
    path('registration/', ind_views.registration, name='registration'),
    
    # Order-related URLs
    path('your-orders/', ind_views.yourorders, name='yourorders'),
    path('confirmed-orders/', ind_views.confirmproducts, name='confirmedorders'),
    path('chechouts/', ind_views.chechouts, name='chechouts'),
    
    # Product-related URLs
    re_path(r'^view-ratings/(?P<pk>\d+)/$', ind_views.viewratings, name='viewratings'),
    path('product-list/', ind_views.productlist, name='productlist'),
    path('top-products/', ind_views.topproducts, name='topproducts'),
    
    # Miscellaneous
    path('graphs/', ind_views.graphs, name='graphs'),
]