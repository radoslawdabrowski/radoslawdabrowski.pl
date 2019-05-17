from django.shortcuts import render

from attributes.models import Social


def navigation_view_context():
    return {}


def sidebar_view_context():
    return {}


def footer_view_context():
    return {}


def social_view_context():
    return {
        "social": Social.objects.all()
    }


def description_view_context():
    return {}


def mobile_view_context():
    return {}


def email_view_context():
    return {}


def header_view_context():
    return {}
