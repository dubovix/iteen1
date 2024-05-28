class Direction(models.Model):
    class_level = models.CharField(
        null=True,
        blank=True,
    )
    direction_name = models.CharField(null=True, blank=True)
    url = models.CharField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Direction"
        verbose_name_plural = "Directions"
        ordering = [
            "class_level",
        ]

    def __str__(self) -> str:
        return f"{self.direction_name}"


class RecommendedCourse(models.Model):
    class_level: Any = models.IntegerField(
        "Class",
        null=True,
        blank=True,
    )
    num = models.IntegerField(
        "№",
        null=True,
        blank=True,
    )
    code_courses = models.CharField(
        null=True,
        blank=True,
    )
    course_direction = models.ForeignKey(
        to=Direction, null=True, blank=True, on_delete=models.CASCADE
    )
    course_name: Any = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    course_url = models.CharField(
        "URL",
        null=True,
        blank=True,
    )
    course_start = models.DateField(
        null=True,
        blank=True,
    )
    number_hours = models.CharField(
        "Amount of hours",
        null=True,
        blank=True,
    )
    price = models.CharField(
        null=True,
        blank=True,
    )
    recommended_courses = models.CharField(
        null=True,
        blank=True,
    )
    recommended_courses_num = models.IntegerField(
        "Recommended №",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Recommended Course"
        verbose_name_plural = "Recommended Courses"
        ordering = [
            "class_level",
            "num",
        ]

class ApplicationСourse(models.Model):
    username_phone = models.CharField(
        max_length=20,
    )
    first_name: Any = models.CharField(
        max_length=50,
    )

    class Meta:
        verbose_name = "Application for the Course"
        verbose_name_plural = "Applications for the Course"
