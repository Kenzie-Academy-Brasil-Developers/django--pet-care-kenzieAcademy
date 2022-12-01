from django.db import models
import uuid


# Create your models here.
class Trait(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)

    pets = models.ManyToManyField("pets.Pet", related_name="traits")

    def __repr__(self) -> str:
        return f"<Trait {self.id} - {self.name}>"
