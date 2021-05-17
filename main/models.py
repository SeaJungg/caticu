from django.db import models


class new(models.Model):
    url = models.CharField(max_length=254, null=False, primary_key=True)
    title = models.CharField(max_length=1023, blank=True)
    pnrate = models.FloatField(default=1)
    comment = models.TextField(blank=True)
    day0 = models.IntegerField(null=False, default=0)
    day1 = models.IntegerField(null=False, default=0)
    day2 = models.IntegerField(null=False, default=0)
    day3 = models.IntegerField(null=False, default=0)
    day4 = models.IntegerField(null=False, default=0)
    day5 = models.IntegerField(null=False, default=0)
    predict = models.IntegerField(null=True, default='0')
