from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# ------------------ CATEGORY ------------------

class Category(models.Model):
    Category_name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Category_name


# ------------------ ITEMS ------------------

class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    description = models.TextField()
    Price = models.IntegerField()
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.Item_name


# ------------------ ABOUT US ------------------

class AboutUs(models.Model):
    Description = models.TextField()

    def __str__(self):
        return "About Us Content"


# ------------------ FEEDBACK ------------------

class Feedback(models.Model):
    User_name = models.CharField(max_length=50)
    Description = models.TextField()
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='feedback/', blank=True, null=True)

    def __str__(self):
        return self.User_name


# ------------------ BOOK TABLE ------------------

class BookTable(models.Model):
    Name = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=15)  # better than IntegerField
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name


# ------------------ CART ------------------

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    item = models.ForeignKey(Items, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.item.Item_name}"
