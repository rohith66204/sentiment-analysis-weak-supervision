from django.conf.urls import url
from . import views as ind_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',ind_views.logins, name='login'),
    url(r'^home/$',ind_views.home, name='home'),
     url(r'^logout/$', auth_views.LogoutView.as_view(next_page='admins:login'), name='logout'),
    url(r'^upload/product/$',ind_views.uploadProduct, name='uploadproduct'),
    url(r'^View/Ratings/$',ind_views.viewratings, name='viewratings'),
    url(r'^Ordered/Products/$',ind_views.orderedproducts, name='orderedproducts'),
    url(r'^Confirmed/Products/$',ind_views.confirmedproduct, name='confirmedproduct'),
    url(r'^Graphs/(?:(?P<chart_type>.+))?/$',ind_views.graph, name='graph'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)