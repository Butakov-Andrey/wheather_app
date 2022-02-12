from unittest import mock

from django.test import TestCase
from django.urls import resolve, reverse

from .models import Wheather
from .views import WheatherView


class WheatherPageTest(TestCase):

    def setUp(self):
        url = reverse('wheather')
        self.response = self.client.get(url)

    def test_wheather_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_wheather_template(self):
        self.assertTemplateUsed(self.response, 'wheather.html')

    def test_wheather_contains_correct_html(self):
        self.assertContains(self.response, 'Wheather')

    def test_wheather_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Wrong text')

    def test_wheather_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            WheatherView.as_view().__name__
        )


class WheatherTest(TestCase):
    def setUp(self):
        mock_date = '2021-03-04 11:57:11.703055+00:00'
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            self.wheather = Wheather.objects.create(
                city='Minsk',
                temperature='10.00',
            )

    def test_wheather_listing(self):
        self.assertEqual(f'{self.wheather.city}', 'Minsk')
        self.assertEqual(f'{self.wheather.temperature}', '10.00')
        self.assertEqual(f'{self.wheather.created_at}', '2021-03-04 11:57:11.703055+00:00')
