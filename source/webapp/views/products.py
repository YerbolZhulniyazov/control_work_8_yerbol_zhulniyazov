from django.contrib.auth.mixins import UserPassesTestMixin
from webapp.models import Product
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from webapp.forms import ProductForm
from django.urls import reverse
from django.urls import reverse_lazy
from webapp.models import Review
from django.db.models import Avg


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ProductView(DetailView):
    template_name = 'products/product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        avg_rate = Review.objects.filter(product=product).aggregate(avg=Avg('grade'))
        reviews = Review.objects.filter(product=product)
        context['reviews'] = reviews
        context['avg_rate'] = avg_rate
        return context


class ProductCreateView(GroupPermission, CreateView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    model = Product
    groups = ['Moderators']

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(GroupPermission, UpdateView):
    template_name = 'products/product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    groups = ['Moderators']

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(GroupPermission, DeleteView):
    template_name = 'products/confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    groups = ['Moderators']

