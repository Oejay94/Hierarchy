from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from customuser.models import CustomUser

class File_or_Folder(MPTTModel):
    name = models.CharField(max_length=150)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name