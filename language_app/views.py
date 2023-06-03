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

    language_chosen = request.COOKIES.get(
        settings.LANGUAGE_COOKIE_NAME, settings.LANGUAGE_CODE
    )
    if language_chosen:
        translation.activate(language_chosen)
    response = render(
        request,
        "home.html",
        context=context,
    )

    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_chosen)
    return response


def page(request):
    context = {"message": gettext("Message")}
    return render(request, "page.html", context=context)
