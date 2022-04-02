from django.db import models

# Create your models here.
class Contact(models.Model):
    fullName = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.fullName