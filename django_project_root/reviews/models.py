from django.db import models
from django.conf import settings


# Create your models here.
# Model used by non-Admin users for their reviews
class Reviews(models.Model):
    RATE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    phone = models.ForeignKey('mobiles.Mobiles', on_delete=models.CASCADE) # foreign key is 'ean' from Mobiles model
    body = models.TextField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL) # foreign key is 'id' from CustomUser model
    created_at = models.DateTimeField(auto_now_add=True, null=False) 
    updated_at = models.DateTimeField(auto_now=True) 
    rate = models.IntegerField(choices=RATE_CHOICES, default=1, help_text='Rate from 1 to 5') # if not chosen in range 1..5, default 1
    seller = models.CharField(max_length=50, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    
    # constraint to ensure that 1 user can't create more than 1 review per 1 phone model
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'phone'], name='unique_review_per_author')
        ]