from django import http
from django.shortcuts import render
from django.conf import settings

# from django.utils import translation
from django.utils.translation import gettext
from django.utils import translation


def language_switcher(func):
    """
    A decorator that wraps a view in a new function that checks for language-cookie presence in request.
    If a language-change was requested i.e cookie is present, the wrapper
    - activates the requested language,
    - creates the response bye rendering the view, using the new language,
    - sets the language cookie to be used in session,
    - returns the response

    Args:
        request

    Returns:
        django.http.HttpResponse
    """

    def wrapper(request: http.HttpRequest) -> http.HttpResponse:
        request_cookie_lang = request.COOKIES.get(
            settings.LANGUAGE_COOKIE_NAME,
            None,
        )
        if request_cookie_lang is None:
            return func(request)
        translation.activate(request_cookie_lang)
        response = func(request)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, request_cookie_lang)
        return response

    return wrapper


@language_switcher
def home_alone(request):
    title = gettext("Homepage")
    context = {
        "person": "John",
        "title": title,
    }

    return render(
        request,
        "home.html",
        context=context,
    )


@language_switcher
def page(request):
    context = {"message": gettext("Message")}
    return render(request, "page.html", context=context)


def myhtmx(request):
    return render(
        request,
        template_name="myhtmx.html",
        context={},
    )
