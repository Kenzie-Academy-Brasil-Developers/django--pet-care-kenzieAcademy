from django.db import models
from django.forms.models import model_to_dict


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

    def to_dict(self) -> dict:
        return model_to_dict(self)

    @classmethod
    def to_list_dict(cls) -> list[dict]:
        pets = cls.objects.all()

        pet_list = []
        for i, pet in enumerate(pets):
            if i == 0:
                print(model_to_dict(pet).keys)
            pet = model_to_dict(pet)
            pet["traits"] = [model_to_dict(trait) for trait in pet["traits"]]

            pet_list.append(pet)
        return pet_list
