from django.db import models


class Sex(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DEFAULT = "Not informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=20, default=Sex.DEFAULT, choices=Sex.choices)

    group = models.ForeignKey(
        "groups.Group", on_delete=models.CASCADE, related_name="animals", null=True
    )
    traits = models.ManyToManyField("traits.Trait", related_name="pets")

    def __repr__(self) -> str:
        return f"<Pet {self.id} - {self.name}>"
