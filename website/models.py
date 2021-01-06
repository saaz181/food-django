from django.db import models

class FoodCategory(models.Model):
    food_category = models.CharField(max_length=100)
    category_slug = models.CharField(max_length=10)

    class Meta:
        verbose_name = "category"

    def __str__(self):
        return self.food_category


class Food(models.Model):
    food_name = models.CharField(max_length=100)
    food_description = models.TextField()
    food_price = models.CharField(max_length=20)

    food_category = models.ForeignKey(FoodCategory, verbose_name="category", on_delete=models.SET_NULL, null=True)

    food_slug = models.CharField(max_length=50)

    class Meta:
        verbose_name = "food"

    def __str__(self):
        return self.food_name








