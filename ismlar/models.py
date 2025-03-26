from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class Letter(models.Model):
    letter = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.letter


class Name(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(max_length=255, unique=True)
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name="names_letter")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="names_category")
    meaning = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Likes(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE, related_name="likes_name")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_user")

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name.name
    