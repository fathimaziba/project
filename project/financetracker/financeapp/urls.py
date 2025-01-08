from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/',views.login,name='login'),
    path('sign-up/',views.sign_up_view,name='sign-up'),
    path('support/',views.support_view,name='support'),
    path('admin/',views.admin,name='admin'),
    path('user/',views.user_view,name='view'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('accounts/login/',views.accounts,name='accounts/login'),
    path('/transaction/',views.transaction, name='transaction'),
    path('income_expense/',views.income_expense, name='income_expense'),
    path('Profile/',views.profile,name='profile'),
    path('new_transaction/',views.new_transaction,name='new_transaction'),
    path('income/',views.income,name='income'),
    path('expense/',views.expense,name='expense'),

]
