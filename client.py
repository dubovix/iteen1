def get_callback_request(self):
    response = self.session.get(f"{self.host}/api/callback-request/")
    return response


def post_callback_request(self, data):
    response = self.session.post(
        f"{self.host}/api/callback-request/", json=data
    )
    return response