from django.urls import path
from digiuserapp import views

urlpatterns=[
    path('home_pg/',views.home_pg,name="home_pg"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('prod_pg/<cat_name>',views.prod_pg,name="prod_pg"),
    path('single_pg/<int:singleid>/',views.single_pg,name="single_pg"),
    path('cart_pg/',views.cart_pg,name="cart_pg"),
    path('log_pg/',views.log_pg,name="log_pg"),
    path('user_login/',views.user_login,name="user_login"),
    path('add_user/',views.add_user,name="add_user"),
    path('del_user/', views.del_user, name="del_user"),
    path('cart_save/', views.cart_save, name="cart_save"),
    path('cartdlt/<int:dataid>/', views.cartdlt, name="cartdlt"),
    path('checkout_pg/', views.checkout_pg, name="checkout_pg"),

]
