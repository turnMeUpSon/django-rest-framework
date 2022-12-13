from django.urls import reverse, resolve


class TestUrls:

    def test_api_v1_indicators_url(self):
        path = reverse('indicators')
        assert (resolve(path).view_name == 'indicators')
