from django.db import models
from django.utils.html import mark_safe
from datetime import date

# Create your models here.
class Course(models.Model):
    COURSE_STATUS = (
        ('draft', "Draft"),
        ("published", "Publised")
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateTimeField()
    price = models.FloatField()
    author = models.CharField(max_length=72)
    status = models.CharField(default="draft", choices=COURSE_STATUS, max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"
    

class Lesson(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video_url = models.URLField("Video URL")


class Person(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    image = models.ImageField(upload_to="media/images/")

    def UserImage(self):
        return mark_safe(f'<img src={self.image.url} alt="DP" style="width: 30px; height: 30px; border-radius: 50%; border: 1px solid black" />')

    UserImage.short_description = 'Image'
    UserImage.admin_order_field = 'image'

    
    def Age(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return f"{age} Y/O"