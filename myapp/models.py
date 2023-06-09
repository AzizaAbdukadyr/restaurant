from django.db import models

# Create your models here.

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default=" ")

    def __str__(self):
        return self.name


# class Reservation(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     booking_time = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.first_name








# class Reservation(models.Model):
#     name = models.CharField(max_length=100, blank=True)
#     contact = models.CharField("Phone number", max_length=300)
#     time = models.TimeField()
#     count = models.IntegerField()
#     notes = models.CharField(max_length=300, blank=True)

#     def __str__(self):
#         return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
