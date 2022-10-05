from django.db import models

# creates model
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # model manager
    object = models.Manager()

    def __str__(self):
        display_course = '{0.campus_name}: {0.state}'
        return display_course.format(self)

    # deletes second s
    class Meta:
        verbose_name_plural: "University Campus"





