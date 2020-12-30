from django.db import models


class Food(models.Model):
    food_name = models.CharField(max_length=100)
    food_description = models.TextField()
    food_price = models.CharField(max_length=20)
    food_slug = models.CharField(max_length=50)

    def __str__(self):
        return self.food_name
