import copy
import datetime
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PlaceForm


PLACES = [
    {
        "id": 1,
        "name": "Іллінський сквер",
        "description": "У простолюді відоме як КМЦ. Ідеальне місце, якщо це п'ятниця і вечір. Затишна атмосфера для відпочинку після навчального тижня.",
        "place_type": "Розваги / Культура",
        "location": "вул. Іллінська, 9",
        "rating": 5,
        "created_at": "2026-09-15",
    },
    {
        "id": 2,
        "name": "ФіДо",
        "description": "Найкращий варіант перекусити, посидіти та поспілкуватися, коли ти знаходишся в університеті.",
        "place_type": "Розваги / Відпочинок",
        "location": "Підвал 4-го корпусу НаУКМА",
        "rating": 5,
        "created_at": "2026-09-15",
    },
    {
        "id": 3,
        "name": "Контрактова площа",
        "description": "Чудова локація, аби просто зустрітися і погуляти з друзями на Подолі.",
        "place_type": "Прогулянка",
        "location": "Контрактова площа",
        "rating": 5,
        "created_at": "2026-09-15",
    },
    {
        "id": 4,
        "name": "Парк «Наталка»",
        "description": "Гарне місце, щоб піти на вихідних самому: набережна, тиша, кава та краєвиди.",
        "place_type": "Парк / Релакс",
        "location": "Оболонська набережна",
        "rating": 5,
        "created_at": "2026-09-15",
    },
    {
        "id": 5,
        "name": "Хрещатик",
        "description": "Центр міста для динамічних вихідних з друзями, стріт-фуду та прогулянок.",
        "place_type": "Центр міста",
        "location": "вул. Хрещатик",
        "rating": 4,
        "created_at": "2026-09-15",
    },
    {
        "id": 6,
        "name": "Ліс та озеро на шашлики",
        "description": "Сімейний відпочинок на природі з батьками біля води та багаття.",
        "place_type": "Природа / Відпочинок",
        "location": "",
        "rating": 5,
        "created_at": "2026-09-15",
    }
]


def check_places_init(request):
    if "places" not in request.session:
        request.session["places"] = copy.deepcopy(PLACES)


def base(request):
    check_places_init(request)
    selected_place = None

    if "random" in request.GET:
        places = request.session.get("places", [])
        if places:
            weights = [p.get("rating", 1) for p in places]
            selected_place = random.choices(places, weights=weights)[0]

    return render(request, "places/main.html", {"selected_place": selected_place})


def list_places(request):
    check_places_init(request)
    places = request.session.get("places", [])
    return render(request, "places/list.html", {"places": places})


def place_info(request, num):
    check_places_init(request)
    places = request.session.get('places')
    try:
        return render(request, 'places/details.html', {'place': places[num - 1]})
    except IndexError:
        return render(request, 'places/details.html', {'place': None})


def add_place(request):
    check_places_init(request)
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            places = request.session.get("places", [])

            data['id'] = len(places) + 1
            data["created_at"] = str(datetime.date.today())

            places.append(data)
            request.session["places"] = places
            request.session.modified = True

            return HttpResponseRedirect(reverse('places_to_visit:places_list'))
        return render(request, 'places/add.html', {'form':form})
    return render(request, 'places/add.html', {'form': PlaceForm()})
