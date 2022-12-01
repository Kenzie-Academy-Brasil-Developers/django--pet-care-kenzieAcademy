from django.db import models
import uuid


# Create your models here.
class Group(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"<Group {self.id} - {self.scientific_name}>"
