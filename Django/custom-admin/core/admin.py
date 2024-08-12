from django.contrib import admin
from .models import Course, Lesson, Person
import math
from django.contrib import admin

admin.AdminSite.site_header = "Custom Admin Panel"

class LessonTabularInline(admin.TabularInline):
    model = Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', "price", 'discounted_price', 'status')           # Edit View Area
    list_display_links = ('title', )                                                    # Links in View Area
    list_editable = ('price', 'status')                                                 # Editable Fields in View Area
    # ordering = ('title', )                                                            # Order in ASCENDING order in View Area
    ordering = ('-title', )                                                             # Order in DESCENDING order in View Area

    # fields = ('title', 'publish_date', 'price', 'author', 'status')                     # Fields to show/edit in Add Area
    # exclude = ('title', 'description', )                                              # Fields that you want to exlude from show/Edit Area
    fieldsets = (                                                                       # Make 2 groups inside the form 
        ("Course Data", {
            "fields": ('title', 'publish_date', 'price')
        }),
        ("Author Data", {
            "fields": ("author", 'status')
        })
    )
    readonly_fields = ('publish_date', 'status')                                        # Prohibit Editing in Add Area

    list_filter = ('status', 'author')                                                  # You can now filter by these columns.
    search_fields = ('title', 'price')                                             # You can now perform search on these fields

    inlines = [LessonTabularInline]

    @admin.display(description="Discounted Price (5%)")                                 # Add a new column
    def discounted_price(self, obj):
        return f"${math.ceil(obj.price * 0.9)}"
    

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('course__status',)
    # autocomplete_fields = ('course',)                                                   # Add searchbar to select widget
    raw_id_fields = ('course', )                                                        # pagination, search, filtering (Best for big data) 
    
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('UserImage', 'name', 'dob', 'Age')
    list_display_links = ('name',)