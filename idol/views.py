from django.http import HttpResponse
from django.template import loader

from .models import CardData

def index(request):
    dance_idols = CardData.objects.exclude(name__endswith="＋").order_by('-dance_max')[:20]
    rarity = ['P', 'N', 'N+', 'R', 'R+', 'SR', 'SR+', 'SSR', 'SSR+']
    attribute = {1: "Cute", 2: "Cool", 3: "Passion", 4: "Office"}
    template = loader.get_template('card.html')
    context = {
        'dance_idols': dance_idols,
        'rarity': rarity,
        'type_attribute': attribute,
    }
    return HttpResponse(template.render(context, request))