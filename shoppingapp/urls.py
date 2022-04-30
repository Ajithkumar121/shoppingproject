from . import views
from django.urls import path
app_name='shoppingapp'
urlpatterns = [
    path('',views.allprocat,name="allprocat"),
    path('<slug:c_slug>/',views.allprocat,name="product_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name="prodcatdetail"),

]
