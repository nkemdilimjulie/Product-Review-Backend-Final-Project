from django.db import models
from django.conf import settings
from accounts.models import CustomUser
from mobiles.models import Mobiles

# Create your models here.
class Marketer(models.Model):
    """Marketers: Many-to-many with Mobiles, CustomUsers.
    Only user with attribute 'is_marketer' can create/update an entry.
    Table entry stores a link to webstore where a given phone model can be purschased.
    Restrictions and authorization: 
    - 1 user can add only 1 link per phone model,
    - links are unique,
    - only the same author can delete/update the entry.
    """
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    phone = models.ForeignKey(Mobiles, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, blank=False, null=False)
    link = models.URLField(max_length=255, unique=True, blank=False, null=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["author", "phone"], name="1_author_per_phone_model", violation_error_message= "Author already added this phone!"
            )
        ]
        
    def __str__(self):
        return f"{self.company} {self.link}"
