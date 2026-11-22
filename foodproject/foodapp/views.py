from django.http import HttpResponse
from .models import FoodOrder

def order_list(request):
    orders = FoodOrder.objects.all()
    output = "<h2>Orders</h2><ul>"
    for order in orders:
        output += f"<li>{order.customer_name} | {order.dish_name} | ₹{order.cost}</li>"
    output += "</ul>"
    return HttpResponse(output)
