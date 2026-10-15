from django.db import models


class LostFoundItem(models.Model):
    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]

    ITEM_STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
        ('Claimed', 'Claimed'),
    ]

    item_name = models.CharField(max_length=100)
    item_photo = models.ImageField(upload_to='item_photos/', blank=True, null=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    lost_found_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )
    date_reported = models.DateField()
    location = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    reporter_name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    item_status = models.CharField(
        max_length=10,
        choices=ITEM_STATUS_CHOICES,
        default='Lost'
    )

    def __str__(self):
        return self.item_name