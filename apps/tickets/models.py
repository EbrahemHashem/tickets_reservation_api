from django.db import models


# movie
class Movie(models.Model):
    hall = models.CharField(max_length= 10)
    name = models.CharField(max_length=15)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# guest
class Guest(models.Model):
    name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name="guest_reservation", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="movie_reservation", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


