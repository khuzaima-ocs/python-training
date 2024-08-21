from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .models import Person



class DomainFilter(admin.SimpleListFilter):

    title = _('Domain')
    parameter_name = "domain"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        domains = set([obj.email.split('@')[1] for obj in model_admin.model.objects.all()])
        return [(domain, domain) for domain in domains]
    
    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        
        if self.value():
            return queryset.filter(email__endswith = "@" + self.value())
        
        return queryset


# Register your models here.
@admin.register(Person)
class AdminPerson(admin.ModelAdmin):

    list_display = ('full_name', 'username', 'delete_button', 'domain')
    fields = ('first_name', 'last_name', 'username', 'email', 'dob')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    list_filter = (DomainFilter,)

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

    def domain(self, obj):
        return obj.email.split('@')[1]