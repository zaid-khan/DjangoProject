from django.db import models

class Genre(models.Model):
    """Models representing a book genre"""
    name = models.CharField(max_length=200, help_text='Enter a book genre (eg. Science Fiction)')

    def __str__(self):
        """String for representing Genre object"""
        return self.name
        