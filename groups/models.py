from django.db import models
from django.forms.models import model_to_dict
import uuid


# Create your models here.
class Group(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"<Group {self.id} - {self.scientific_name}>"

    def to_dict(self) -> dict:
        return model_to_dict(self)

    @classmethod
    def to_list_dict(cls) -> list[dict]:
        groups = cls.objects.all()
        group_list = [model_to_dict(group) for group in groups]
        return group_list
