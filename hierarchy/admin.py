from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import File_or_Folder

admin.site.register(
    File_or_Folder, DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title'
    ),
    list_display_links=(
        'indented_title',
    ),
)
