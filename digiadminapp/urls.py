from django.urls import path

from digiadminapp import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('add_category/',views.add_category,name="add_category"),
    path('cat_add/',views.cat_add,name="cat_add"),
    path('display_category/',views.display_category,name="display_category"),
    path('update_cate/<int:catid>/',views.update_cate,name="update_cate"),
    path('editcateg/<int:catid>/',views.editcateg,name="editcateg"),
    path('delete_cate/<int:catid>/',views.delete_cate,name="delete_cate"),
    path('productadd/',views.productadd,name="productadd"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:productid>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:productid>/',views.updateproduct,name="updateproduct"),
    path('delproduct/<int:productid>/',views.delproduct,name="delproduct"),
    path('ad_login/',views.ad_login,name="ad_login"),
    path('admin_log/',views.admin_log,name="admin_log"),
    path('log_out/',views.log_out,name="log_out")
]
