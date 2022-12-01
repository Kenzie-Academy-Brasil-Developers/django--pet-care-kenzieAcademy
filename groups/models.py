from django.db import models
from django.forms.models import model_to_dict


# Create your models here.
class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"<Group {self.id} - {self.scientific_name}>"
