from django.db import models  # type: ignore[import]
from django.contrib.auth.models import AbstractUser  # type: ignore[import]

class User(AbstractUser):
    pass

class Run(models.Model):
     # This creates a many-to-one relationship.
    # One User can have many Runs.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # These fields will store the basic stats for each run.
    distance_meters = models.FloatField()
    duration_seconds = models.IntegerField()
    start_time = models.DateTimeField()

    # A JSONField is perfect for storing the list of GPS coordinates for the route.
    route_coordinates = models.JSONField(null=True, blank=True)

    def __str__(self):
        # This defines how a Run object is displayed in the Django admin area.
        return f"Run by {self.user.username} on {self.start_time.strftime('%Y-%m-%d')}"
