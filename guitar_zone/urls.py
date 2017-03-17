from django.conf.urls import url, include
import sys
# sys.path.append("../")
from django.contrib import admin
from .views import customer_view, guitar_detail_view, guitar_view, home_view, guitar_category_view, order_view, payment_type_view
from .views.customer_view import RegisterViewSet, LoginViewSet
from .views.payment_type_view import add_payment
from .views.rent_out_guitar_view import rent_out_guitar


app_name = 'guitar_zone'

urlpatterns = [
    url(r'^register/', RegisterViewSet.as_view(), name='register'),
    url(r'^register_customer/', customer_view.register_customer, name='register_customer'),
    url(r'^login/', LoginViewSet.as_view(), name='login'),
    url(r'^login_customer/', customer_view.login_customer, name='login_customer'),
    url(r'^logout/', customer_view.logout_customer, name='logout'),
    url(r'^order/', customer_view.logout_customer, name='order'),
    url(r'^account/', customer_view.logout_customer, name='account'),
    url(r'^cart/', order_view.get_guitars_in_cart, name='cart'),
    url(r'^addpayment/', payment_type_view.add_payment, name='addpayment'),
]

urlpatterns += [  url(r'^home/', home_view.get_guitars_and_types, name='home'),
]

urlpatterns += [
    url(r'^guitars/', guitar_view.get_guitars_types_and_count, name='guitars'),
    url(r'^guitartype/(?P<pk>\d+)/', guitar_category_view.get_guitar_type_info, name='guitartype'),
    url(r'^guitardetail/(?P<pk>\d+)/', guitar_detail_view.GuitarDetailView.as_view(), name='guitardetail'),
    url(r'^add_guitar_to_order/(?P<pk>\d+)/', guitar_detail_view.add_guitar_to_order, name='add_guitar_to_order'),
    url(r'^addguitar/', create_a_product, name='addguitar'),
]