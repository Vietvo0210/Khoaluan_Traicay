from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.ShowAll, name='product-list'),
    path('product-detail/<int:pk>/', views.ViewProduct, name='product-detail'),
    path('product-create/', views.CreateProduct, name='product-create'),
    path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>/', views.deleteProduct, name='product-delete'),
    path('search/<str:title>',views.SeachProduct,name='search'),

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

    path('galery-list/', views.ShowAll_Galery, name='galery-list'),
    path('galery-detail/<int:pk>/', views.ViewGalery, name='galery-detail'),
    path('galery-create/', views.CreateGalery, name='galery-create'),
    path('galery-update/<int:pk>/', views.updateGalery, name='galery-update'),
    path('galery-delete/<int:pk>/', views.deleteGalery, name='galery-delete'),


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
    path('login/',views.login),

]
