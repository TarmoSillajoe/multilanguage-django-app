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
    lang_request = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
    if lang_request and translation.get_language() != lang_request:
        user_language = lang_request
        translation.activate(user_language)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    return response


def page(request):
    context = {"message": gettext("Message")}
    return render(request, "page.html", context=context)
