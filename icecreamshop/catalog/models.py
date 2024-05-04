from django.db import models

from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

# Create your models here.
class Flavor(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book flavor"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular flavor instance."""
        return reverse('flavor-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='flavor_case_insensitive_unique',
                violation_error_message = "Flavor already exists (case insensitive match)"
            ),
        ]
        
class Topping(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book topping"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular topping instance."""
        return reverse('topping-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='topping_case_insensitive_unique',
                violation_error_message = "Topping already exists (case insensitive match)"
            ),
        ]
class Cones(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book cones"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular cones instance."""
        return reverse('cones-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='cones_case_insensitive_unique',
                violation_error_message = "Cones already exists (case insensitive match)"
            ),
        ]

class Bowls(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a bowl size"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular bowl instance."""
        return reverse('bowls-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='bowls_case_insensitive_unique',
                violation_error_message = "Bowls already exists (case insensitive match)"
            ),
        ]