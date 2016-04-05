from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import BlitzUsers
from WotBlitz import WotBlitz


def index(request):
    latest_account_list = BlitzUsers.objects.order_by('id')[:5]
    context = {'latest_account_list': latest_account_list}
    return render(request, 'stats/index.html', context)


def detail(request, account_id):
    c = WotBlitz()
    c.application_id = '6c8058cb8dadba5f30be5439d9d15490'
    stats = c.get_player_personal_data(account_id)
    return render(request, 'stats/detail.html', {'account_id': account_id, 'stats': stats})

'''
def detail(request, account_id):
    try:
        account = BlitzUsers.objects.get(pk=account_id)
    except BlitzUsers.DoesNotExist:
        raise Http404("Account does not exist")
    return render(request, 'stats/detail.html', {'account': account})
    #     account = get_object_or_404(BlitzUsers, pk=account_id)
    #     return render(request, 'stats/detail.html', {'account': account})
'''


def results(request, account_id):
    response = "You're looking at the results of account %s."
    return HttpResponse(response % account_id)


def vote(request, account_id):
    return HttpResponse("You're voting on question %s." % account_id)
