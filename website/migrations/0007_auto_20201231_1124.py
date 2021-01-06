# Generated by Django 3.1.4 on 2020-12-31 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_category', models.CharField(max_length=100)),
                ('category_slug', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'category',
            },
        ),
        migrations.AddField(
            model_name='food',
            name='food_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.foodcategory', verbose_name='category'),
        ),
    ]