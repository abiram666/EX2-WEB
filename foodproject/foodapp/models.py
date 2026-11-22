from django.db import models

class FoodOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    dish_name = models.CharField(max_length=150)
    cost = models.DecimalField(max_digits=8, decimal_places=5)

    class Meta:
        db_table = 'food_delivery_orders'

    def __str__(self):
        return f"{self.customer_name} - {self.dish_name}"
