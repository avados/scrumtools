from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import logging


logger = logging.getLogger(__name__)


def index(request):
    try:
        return render(request, "index.html", {
        })
    except ObjectDoesNotExist:
        logger.error('ERROR')
        return render(request, 'index.html', {
        })