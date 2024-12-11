from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    bounty = models.IntegerField()  # Example: "Straw Hat Pirate"
    character_image = models.ImageField(upload_to='character_images/', blank=False, default=None)
    devil_fruit = models.CharField(max_length=100)

    def __str__(self):
        return self.name