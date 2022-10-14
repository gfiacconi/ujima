from django.db import models

class Venue(models.Model):
    name = models.CharField('Venue name', max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField('Zip code', max_length=5)
    phone_number = models.CharField('Contact phone', max_length=13)
    email = models.EmailField('Contact email')
    website = models.URLField('Website Address')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    email = models.EmailField('Contact email')
    phone_number = models.CharField('Contact phone', max_length=13)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField('Zip code', max_length=5)

    def __str__(self):
        return self.first_name+ " " + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
