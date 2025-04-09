from django.db import models

# Create your models here.
class Character(models.Model):
    """
    Represents a character in the One Piece universe.

    Attributes:
        name (CharField): The name of the character.
        bounty (IntegerField): The bounty amount of the character.
        character_image (ImageField): An image representing the character.
        devil_fruit (CharField): The name of the Devil Fruit the character possesses, if any.
    """
    
    name = models.CharField(max_length=100)
    bounty = models.IntegerField()  # Example: "Straw Hat Pirate"
    character_image = models.ImageField(upload_to='character_images/', blank=False, default=None)
    devil_fruit = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the character.

        Returns:
            str: The name of the character.
        """
        return self.name