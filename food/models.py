from django.db import models
from django.utils import timezone
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    place_image = models.ImageField(upload_to='place_image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='places')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class PlaceOwner(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.place.name} by {self.owner.full_name}'

class PlaceComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    stars_given = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} gave {self.stars_given} to {self.place.name}'

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='meals')
    image = models.ImageField(upload_to='meal_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='meals')

    def __str__(self):
        return self.name

class UserFavoriteFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} likes {self.food.name}'