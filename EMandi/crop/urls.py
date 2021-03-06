from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views
from .views import PriceDataView
from crop.views import *


app_name = "crop"

urlpatterns = [
    path('pricedata/<crop>/<variety>/',PriceDataView.as_view()),
    path('crop/<cropName>/', CropVariety.as_view()),
    path('cropname/', CropTypes.as_view()),
    path('watchlist/',WatchListView.as_view()),
    path('watchlist/<crop>/<variety>/',WatchListCreate.as_view()),
    path('pricedata/<id>/',PriceDataView.as_view()),
    path('crop1/<cropid>/',getCropView.as_view()),
]