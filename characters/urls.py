from django.urls import path
from characters.views import get_random_character


urlpatterns = [
    path("character/random/", get_random_character, name="character-random")
]

app_name = "character"
