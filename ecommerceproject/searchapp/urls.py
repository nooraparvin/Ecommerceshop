from . import views
from django.urls import path
app_name='searchapp'
urlpatterns = [

    path('', views.SearchResult, name='SearchResult'),
    # path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    # path('<slug:c_slug>/<slug:product_slug>', views.proDetail, name='prodCatdetail')

]