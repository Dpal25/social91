from django.db import models

# Create your models here.


class PricePerPart(models.Model):
    date = models.CharField(max_length=200)
    top_tube = models.IntegerField()
    down_tube = models.IntegerField()
    seat_tube= models.IntegerField()
    seat_stay = models.IntegerField()
    chain_stay = models.IntegerField()

    spokes = models.IntegerField()
    hub = models.IntegerField()
    rim = models.IntegerField()
    tire = models.IntegerField()
    valve = models.IntegerField()

    saddle = models.IntegerField()
    seat_post = models.IntegerField()

    handlebar_grip = models.IntegerField()
    head_tube = models.IntegerField()
    shock_absorber = models.IntegerField()
    front_brakes = models.IntegerField()
    fork = models.IntegerField()

    chain = models.IntegerField()
    chain_rings = models.IntegerField()
    pedal = models.IntegerField()
    crank_arm = models.IntegerField()
