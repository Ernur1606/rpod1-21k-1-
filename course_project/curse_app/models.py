from django.db import models
from pytils.translit import slugify

class Course(models.Model):
    name = models.CharField("Course Name", max_length=255)
    description = models.TextField("Course description")
    slug = models.SlugField(unique=True, blank=True, editable=False)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def save(self, *ards, **kwargs):
        self.slug = slugify(self.name)
        super().save(*ards, **kwargs)

    def __str__(self):
       return self.name
    
class Lesson(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Choose Course")
    theme = models.CharField("Lesson theme", max_length=255)
    content = models.TextField("Description", blank=True, null=True)
    youtube_url = models.CharField("Youtube URL", max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return f"{self.course.name} - {self.theme}"