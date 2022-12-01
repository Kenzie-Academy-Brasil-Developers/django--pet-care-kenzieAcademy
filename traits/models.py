from django.db import models
from django.forms.models import model_to_dict


# Create your models here.
class Trait(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"<Trait {self.id} - {self.name}>"

    def to_dict(self) -> dict:
        return model_to_dict(self)

    @classmethod
    def to_list_dict(cls) -> list[dict]:
        traits = cls.objects.all()
        trait_list = [model_to_dict(trait) for trait in traits]
        return trait_list
