from django.db import models

class CustomUser(models.CustomUser):

    def __str__(self):
        return self.username
