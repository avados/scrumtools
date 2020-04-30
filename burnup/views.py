from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import logging
from burnup.utils import *

from django.utils.encoding import uri_to_iri

logger = logging.getLogger(__name__)


# Create your views here.


# def index(request):
#     try:
#         return render(request, "index.html", {
#         })
#     except ObjectDoesNotExist:
#         logger.error('ERROR')
#         return render(request, 'index.html', {
#         })


def showburnup(request):
    # could use get parameter : param1 = request.GET.get("param1", None)
    values = request.GET.get("velocities", None)
    real = average = best = worst = error_message = None
    method = request.GET.get("method", None)
    scope = request.GET.get("scope", None)
    if method is not None:
        try:
            method = CalculusType(int(method))
        except:
            method = CalculusType.XBESTWORST
    else:
        method = CalculusType.XBESTWORST

    if method != CalculusType.XBESTWORST and method != CalculusType.STANDARDDEV:
        method = CalculusType.XBESTWORST

    try:
        if values is not None:
            real = get_real_progress(parse_list_of_number(values))
            average = get_average_forecast(parse_list_of_number(values), method)
            best = get_best_forecast(parse_list_of_number(values), method)
            worst = get_worst_forecast(parse_list_of_number(values), method)
        else:
            real = []
            average = []
            best = []
            worst = []
    except Exception as e:
        logger.error(e)
        error_message = "Invalid values, Please enter velocities values separated by comma or semicolon."

    ext_scope = None
    if scope is not None:
        ext_scope = get_extended_scope(scope, len(real) + len(average))

    return render(request, "showBurnUp.html", {
        'original_values': values,
        'real': real,
        'best': best,
        'worst': worst,
        'average': average,
        'scope': scope,
        'ext_scope': ext_scope,
        'error_message': error_message
    })


def register(request):
    try:
        return render(request, "register.html", {
        })
    except ObjectDoesNotExist:
        logger.error('ERROR')
        return render(request, 'register.html', {
        })
