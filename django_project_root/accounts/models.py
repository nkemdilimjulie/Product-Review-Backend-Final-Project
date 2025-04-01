from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """One-to-many Model.
    Model is expands AbstractUser Model with additional boolean field 'is_marketer'.
    """
    # name field removed as not used
    
    is_marketer = models.BooleanField(
        default=False,
        help_text=("Designates whether the user's type is marketer.")
    )
    