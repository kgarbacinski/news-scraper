from django.test import TestCase, Client

class TestHomeView(TestCase):
    URL = "/"

    def setUp(self):
        self.client = Client()

    def test_should_return_200_when_app_is_running(self) -> None:
        response = self.client.get(TestHomeView.URL)

        self.assertEqual(response.status_code, 200)
