from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView, CreateView
from webapp.models import Review
from webapp.forms import ReviewForm
from webapp.models import Product


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ReviewDeleteView(GroupPermission, LoginRequiredMixin, DeleteView):
    model = Review
    success_url = '/'
    template_name = 'reviews/review_confirm_delete.html'
    groups = ['Moderators']

    def dispatch(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        if self.request.user != review.author:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ReviewEditView(GroupPermission, LoginRequiredMixin, UpdateView):
    template_name = 'reviews/review_edit.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'review'
    permission_required = 'webapp.delete_review'
    success_url = '/'
    groups = ['Moderators']

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class ReviewAddView(LoginRequiredMixin, CreateView):
    template_name = 'reviews/create_review.html'
    form_class = ReviewForm
    model = Review
    success_url = '/'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_detail', pk=product.pk)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
