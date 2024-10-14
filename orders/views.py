from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Order

# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset = ...):
        return Order.objects.filter(user=self.request.user, is_active=True).first()