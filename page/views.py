from django.shortcuts import render
from django.http import HttpResponse
from page.models import Players, Teams

def index(request, id):
    players = Players.objects.all()

    if id == None:
        s = '<h1>Параметр  НЕ получен</h1>'
    else:
        s = '<h1>Параметр получен</h1>'
    # players = Players.objects.filter(team=team).order_by('name')
    s = s + 'Команда: <br><br>'
    for player in players:
        s = s + '(' + str(player.pk) + ') ' + player.name + '<br>'
    return HttpResponse(s)

def player(request):
    return ''