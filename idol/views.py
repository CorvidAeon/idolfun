from django.http import HttpResponse
from django.template import loader

from .models import CardData

def index(request):
    dance_idols = CardData.objects.order_by('-dance_max')[:5]
    rarity = ['', 'N', 'N+', 'R', 'R+', 'SR', 'SR+', 'SSR', 'SSR+']
    template = loader.get_template('card.html')
    context = {
        'dance_idols': dance_idols,
        'rarity': rarity,
    }
    return HttpResponse(template.render(context, request))