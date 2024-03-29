from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('admin-create/', views.CreateAdmin, name='admin-create'),

    path('new-list/', views.NewList, name='new-list'),
    path('new-create/', views.CreateNew, name='new-create'),

    path('vietnam-fruits/', views.Vietnamesespecialtyfruit, name='vietnam-fruits'),
    path('product-list/', views.ShowAll, name='product-list'),
    path('product-detail/<int:pk>/', views.ViewProduct, name='product-detail'),
    path('product-create/', views.CreateProduct, name='product-create'),
    path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>/', views.deleteProduct, name='product-delete'),
    path('search/<str:title>',views.SearchProduct,name='search'),

    path('customer-list/', views.ShowAll_Customer, name='customer-list'),
    path('customer-detail/<int:pk>/', views.ViewCustomer, name='customer-detail'),
    path('customer-create/', views.CreateCustomer, name='customer-create'),
    path('customer-update/<int:pk>/', views.updateCustomer, name='customer-update'),
    path('customer-delete/<int:pk>/', views.deleteCustomer, name='customer-delete'),

    path('feedback-list/', views.ShowAll_Feedback, name='feedback-list'),
    path('feedback-detail/<int:pk>/', views.ViewFeedback, name='feedback-detail'),
    path('feedback-create/', views.CreateFeedback, name='feedback-create'),
    path('feedback-update/<int:pk>/', views.updateFeedback, name='feedback-update'),
    path('feedback-delete/<int:pk>/', views.deleteFeedback, name='feedback-delete'),

    path('orders-list/', views.ShowAll_Orders, name='orders-list'),
    path('orders-detail/<int:pk>/', views.ViewOrders, name='orders-detail'),
    path('orders-create/', views.CreateOrders, name='orders-create'),
    path('orders-update/<int:pk>/', views.updateOrders, name='orders-update'),
    path('orders-delete/<int:pk>/', views.deleteOrders, name='orders-delete'),

    path('order_details-list/', views.ShowAll_Order_details, name='order_details-list'),
    path('order_details-detail/<int:pk>/', views.Vieworder_details, name='order_details-detail'),
    path('order_details-create/', views.Createorder_details, name='order_details-create'),
    path('order_details-update/<int:pk>/', views.updateorder_details, name='order_details-update'),
    path('order_details-delete/<int:pk>/', views.deleteorder_details, name='order_details-delete'),

    path('predict/', views.GetPredictedResult.as_view()),
    path('login/<str:pk>/<str:gk>',views.CheckLogin,name='login'),

    path('otp', views.sendOTP, name='sendOTP'),
    path('verify-otp', views.verifyOTP, name='verifyOTP')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
