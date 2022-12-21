from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import F

from .models import Player, Code, Transaction

def index(request):
    player_list = Player.objects.order_by('-points')
    context = {'player_list': player_list,}
    return render(request, 'qrcomp/index.html', context)


def registration(request):
    return render(request, 'qrcomp/registration.html')


def register(request):
    if not (request.POST["username"] and request.POST["fullname"]):
        return render(request, 'qrcomp/registration.html', {'error_message': "Hiányos felhasználónév vagy teljes név."})
    try:
        Player.objects.get(username=request.POST["username"])

        return render(request, 'qrcomp/registration.html', {'error_message': "A felhasználónév már foglalt."})
    except Player.DoesNotExist:
        player = Player(full_name=request.POST["fullname"], username=request.POST["username"])
        player.save()

        return HttpResponseRedirect(reverse('qrcomp:successful_registration'))


def successful_registration(request):
    return render(request, 'qrcomp/successful_registration.html')


def code(request, name):
    c = get_object_or_404(Code, name=name)
    return render(request, 'qrcomp/code.html', {'code': c})


def code_entry(request):
    code_id = request.POST["code"]
    code = Code.objects.get(pk=code_id)
    if not request.POST["username"]:
        return render(request, 'qrcomp/code.html', {'code': code, 'error_message': "Hiányos felhasználónév"})
    try:
        player = Player.objects.get(username=request.POST["username"])
        if code.achievers_left and not Transaction.objects.filter(player=player, code=code):
            points = code.achievers_left*2
            code.achievers_left = F('achievers_left') - 1
            code.save(update_fields=['achievers_left'])
        else:
            points = 0

        tr_a = Transaction(player=player, code=code, points=points)
        tr_a.save()

        player.points += points
        player.save()

        return HttpResponseRedirect(reverse('qrcomp:successful_scan', args=(tr_a.id,)))

    except Player.DoesNotExist:
        return render(request, 'qrcomp/code.html', {'code': code, 'error_message': "Nem létező felhasználónév"})


def successful_scan(request, transaction_id):
    tr_a = get_object_or_404(Transaction, pk=transaction_id)
    code = tr_a.code
    message = code.message
    points = tr_a.points

    return render(request, 'qrcomp/successful_scan.html', {'message': message, 'points': points})

