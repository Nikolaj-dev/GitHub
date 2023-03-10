from django.db import models
from django.template.defaultfilters import slugify


class Teacher(models.Model):
    fullname = models.CharField(
        "Teacher's full name",
        max_length=128,
    )

    bio = models.TextField(
        "Teacher's bio",
        max_length=5000,
    )

    lesson_price = models.PositiveIntegerField(
        "The price for one lesson",
        db_index=True,
    )

    url = models.SlugField()

    LANGUAGE_CHOICES = [
        ('English', 'ENG'),
        ('Spanish', 'ES'),
        ('French', 'FR'),
    ]
    language = models.CharField(
        max_length=32,
        choices=LANGUAGE_CHOICES,
        default='ENG'
    )

    def save(self, *args, **kwargs):
        self.url = slugify(self.fullname)
        super(Teacher, self).save(*args, **kwargs)

    class Meta:
        app_label = 'everyone_in_touch'
        ordering = ('-lesson_price',)
        verbose_name = 'a teacher'
        verbose_name_plural = 'teachers'

