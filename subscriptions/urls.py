from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='subscriptions-home'),
    path('config/', views.stripe_config),  # new
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success),  # new
    path('cancel/', views.cancel),  # new
    path('webhook/', views.stripe_webhook),
    path('logout/', views.logout_view, name='logout'),
]