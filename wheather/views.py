from django.views.generic import ListView
from django.shortcuts import render

from .models import Wheather
from .get_weather import GetWeather


class WheatherView(ListView):
    template_name = 'wheather.html'
    default_city = 'Moscow'

    def get(self, request, *args, **kwargs):
        try:
            city = request.GET['city']
            if not city:
                city = self.default_city
        except:
            city = self.default_city
        g = GetWeather(city)
        g.insert_data()
        weather = Wheather.objects.latest('created_at')
        return render(request, self.template_name, {'wheather': weather})
