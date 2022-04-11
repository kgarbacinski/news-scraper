from django.test import TestCase, Client


class TestHistoryView(TestCase):
    URL = "/"

    def setUp(self):
        self.client = Client()

    def test_should_return_200_when_app_is_running(self) -> None:
        response = self.client.get(TestHistoryView.URL)

        self.assertEqual(response.status_code, 200)
