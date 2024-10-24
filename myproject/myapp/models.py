from django.db import models
from django.contrib.auth.models import User  # Import User model

class Tweet(models.Model):  # It's a good practice to use CamelCase for model names
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Corrected field name

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'