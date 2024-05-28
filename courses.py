@extend_schema(
    description="The endpoint returns the sent message to the  "
    "email address if the data is entered correctly",
    responses={
        "200": examples.ExampleResponseOK(
            value={
                "status": "[bool] True",
                "message": "[str] The application has been sent",
            }
        ),
        "401": examples.ExampleResponseClientError(
            examples=[
                examples.send_email_example,
            ]
        ),
    },
    summary="The sent email",
)
class ApplicationСourse(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request) -> Response:
        data = request.data
        try:
            writing = ApplicationСourseSerializer(data=data)
            if writing.is_valid(raise_exception=True):
                writing.save()
        except Exception:
            return Response(status=500)

        result_send = helpers.send_preferred_course(data=data)
        check_status_email_send(status=result_send, data=data)

        if result_send:
            return Response(status=200)
        else:
            return Response(status=500)


def check_status_email_send(status, data):
    if status:
        search = Application.objects.filter(
            Q(username_phone=data["username_phone"])
            & Q(first_name=data["first_name"])
            & Q(last_name=data["last_name"])
            & Q(course_name=data["course_name"])
        ).last()
        if search:
            search.application_sent_email = True
            search.save()