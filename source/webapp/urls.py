from webapp.views.base import IndexView
from webapp.views.products import ProductCreateView, ProductView, ProductUpdateView, ProductDeleteView
from webapp.views.reviews import ReviewAddView, ReviewDeleteView, ReviewEditView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name="product_update"),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='confirm_delete'),
    path('products/<int:pk>/review/add/', ReviewAddView.as_view(), name='review_create'),
    path('reviews/edit/<int:pk>', ReviewEditView.as_view(), name='review_edit'),
    path('reviews/delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('reviews/delete/<int:pk>', ReviewDeleteView.as_view(), name='confirm_delete_review'),
    path('reviews/add/', ReviewAddView.as_view(), name='review_create')
]
