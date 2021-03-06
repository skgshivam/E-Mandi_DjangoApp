from django.urls import path, include
from .import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from accounts import views as user_views
from rest_framework import routers
# from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "transaction"


urlpatterns = [
   path('bank/',BankList.as_view()),
   path('bank/<username>/',Update.as_view()),
   path('balance/',BalanceView.as_view()),
   path('balances/<username>/',BalanceUpdate.as_view()),
   path('transaction/',MakeTransactionView.as_view()),
]   

# router = DefaultRouter()
# router.register(r'BankHolder', UserViewSet,base_name="list")
# urlpatterns = router.urls
