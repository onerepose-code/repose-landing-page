from django.db import models

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

YES_NO_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

DISCOVER_ART_CHOICES = [
    ('short-form content', 'Short-form Content'),
    ('other', 'Other'),
]


class ContactEnthusiasts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)          # no choices= here
    knows_emerging_artist = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    artist_details = models.CharField(max_length=500, blank=True, null=True)
    discover_art = models.CharField(max_length=500)    # no choices= here

    def __str__(self):
        return f"{self.name} ({self.email})"