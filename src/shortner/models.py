from sqlite3 import IntegrityError
from django.db import models
import random
import string


def code_generator():
    letters = string.ascii_letters
    digits = string.digits
    character = letters+digits
    sample_character = ''.join(random.sample(character, 4))
    return sample_character


# Create your models here.

class Link(models.Model):
    url = models.CharField(max_length=1000)
    code = models.CharField(max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return self.url
    
    def save(self, *args , **kwargs):
        if not self.code:
            while True:
                try:
                    self.code = code_generator()
                except IntegrityError:
                    continue
                break

        return super().save(*args, **kwargs)    