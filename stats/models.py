from django.db import models


class BlitzUsers(models.Model):

    account_id = models.CharField(
        max_length=255,
    )
    nickname = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.nickname

