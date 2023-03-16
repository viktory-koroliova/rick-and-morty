from django.db import models

class Character(models.Model):

    class StatusChoices(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        UNKNOWN = "unknown"

    class GenderChoices(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        GENDERLESS = "Genderless"
        UNKNOWN = "unknown"

    api_id = models.IntegerField()
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=55,
        choices=StatusChoices.choices,
        default=StatusChoices.UNKNOWN
    )
    species = models.CharField(max_length=255)
    gender = models.CharField(max_length=55, choices=GenderChoices.choices)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name
