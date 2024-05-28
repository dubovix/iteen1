from api.models import ApplicationСourse


class ApplicationСourseSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(allow_blank=True, default="")
    patronymic_name = serializers.CharField(allow_blank=True)

    class Meta:
        model = ApplicationСourse
        fields = "__all__"