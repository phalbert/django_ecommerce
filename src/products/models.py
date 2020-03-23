import os, random
from django.db import models

def get_file_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1000000, 999999999)
    name, ext = get_file_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{final_filename}'

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    image = models.FileField(upload_to=upload_image_path, null=True, blank=True) # uploaded to media root

    def __str__(self):
        return self.title
