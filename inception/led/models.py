from __future__ import unicode_literals

from django.db import models

class Led(models.Model):
    LED_WATTAGES = (('S','Six_watt'),
                 ('N','Nine_watt'),
                 ('TW','Twelve_watt'),
                   )
    name = models.CharField(max_length=60)
    led_wattage = models.CharField(max_length=3, choices=LED_WATTAGES)
