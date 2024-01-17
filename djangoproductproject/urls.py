"""djangoproductproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import productview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('productinterface/', productview.ProductInterface),
    path('fetchallproducttypes/',productview.FetchAllProductTypes),
    path('fetchallproductitems/',productview.FetchAllProductItems),
    path('productsubmit',productview.ProductSubmit),
    path('fetchallproducts/',productview.FetchAllProducts),
    path('displayallproduct/',productview.DisplayAllProduct),
    path('displaybyid/',productview.DisplayById),
    path('edit_product_data',productview.Edit_Product_Data),
    path('displaypicture',productview.DisplayPicture),
    path('edit_picture',productview.Edit_Picture),
]

