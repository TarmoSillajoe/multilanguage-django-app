from django.shortcuts import render
from django.conf import settings

# from django.utils import translation
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import gettext
from django.utils import translation


def home(request):
    title = gettext("Homepage")
    context = {
        "person": "John",
        "title": title,
    }

    response = render(
        request,
        "home.html",
        context=context,
    )
    if request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME):
        user_language = request.COOKIES[settings.LANGUAGE_COOKIE_NAME]
        translation.activate(user_language)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    return response
