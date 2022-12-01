from django.db import models
from django.forms.models import model_to_dict
import uuid


class Sex(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DEFAULT = "Not informed"


class Pet(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=20, default=Sex.DEFAULT, choices=Sex.choices)

    group = models.ForeignKey("groups.Group", on_delete=models.CASCADE, related_name="animals")

    def __repr__(self) -> str:
        return f"<Pet {self.id} - {self.name}>"

    def to_dict(self) -> dict:
        return model_to_dict(self)

    @classmethod
    def to_list_dict(cls) -> list[dict]:
        pets = cls.objects.all()
        pet_list = [model_to_dict(pet) for pet in pets]
        return pet_list
