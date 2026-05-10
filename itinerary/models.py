from django.db import models


class Trip(models.Model):

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Stop(models.Model):

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE
    )

    city = models.CharField(max_length=100)

    start_date = models.DateField()

    end_date = models.DateField()

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.city


class Activity(models.Model):

    stop = models.ForeignKey(
        Stop,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)

    time = models.CharField(max_length=50)

    cost = models.IntegerField()

    def __str__(self):
        return self.name