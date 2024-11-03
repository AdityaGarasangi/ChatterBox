from django.contrib import admin
from .models import *

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "room",
        "message_content",
        "date",
    )


admin.site.register(Chatroom)
admin.site.register(ChatMessage, MessageAdmin)
