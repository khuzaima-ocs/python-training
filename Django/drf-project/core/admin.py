from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Person

# Register your models here.
@admin.register(Person)
class AdminPerson(admin.ModelAdmin):

    list_display = ('full_name', 'username', 'delete_button')
    fields = ('first_name', 'last_name', 'username', 'email', 'dob')
    search_fields = ('first_name', 'last_name', 'username', 'email')

    list_display_links = ('full_name', )

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def delete_button(self, obj):
        return format_html(
            '<a class="button" href="{}">Delete</a>',
            reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        )
    delete_button.short_description = 'Delete'
    delete_button.allow_tags = True