from sys import dllhandle
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Item, Message, Room, Topic
from user.models import Profile
from .forms import CreateRoomForm, CreateItemForm, SoldItem
import datetime

# Create your views here.
def home(request):

    return render(request,'base/landing.html')

def dashboard(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    all_rooms = Room.objects.filter(
        Q(topic__name__icontains=query) | # SELECT * FROM base_room WHERE topic LIKE '%query%'
        Q(host__name__icontains = query) | # SELECT * FROM base_room WHERE host LIKE '%query%'
        Q(title__icontains = query) | # SELECT * FROM base_room WHERE title LIKE '%query%'
        Q(description__icontains = query) # SELECT * FROM base_room WHERE description LIKE '%query%'
    ) #Not case sensitive
    # SELECT * FROM base_topic
    all_topics = Topic.objects.all()
    activity_messages = Message.objects.filter(
        Q(room__title__icontains=query)
    )

    # SELECT count(*) FROM base_room
    room_count = all_rooms.count()

    context = {
        'all_rooms':all_rooms,
        'all_topics':all_topics,
        'room_count':room_count,
        'activity_messages':activity_messages,
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    # SELECT * FROM base_room where id = pk
    room = Room.objects.get(id=pk)
    # SELECT * FROM base_message where room = room
    room_messages = room.message_set.all()

    participants = room.participants.all()
    if request.method == "POST":
        sender = Profile.objects.get(username = request.user.username)

        user_message = Message.objects.create(
            user = sender,
            room = room,
            body = request.POST.get('message-body')
        )
        room.participants.add(sender)
        return redirect('room',pk=room.id)

    context = {
        'room':room,
        'room_messages':room_messages,
        'participants':participants,
    }
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def create_room(request):
    form = CreateRoomForm()

    if request.method == "POST":
        form = CreateRoomForm(request.POST, request.FILES)
        sender = Profile.objects.get(username=request.user.username)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = sender
            room.save()
            messages.success(request, 'Room Created successfully')
            return redirect('home')
        else:
            messages.error(request, 'ERROR')

    context = {'form':form}
    return render(request, 'base/create_room.html', context)

@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = CreateRoomForm(instance=room)

    # if request.user.username != room.host.username or request.user.is_superuser:
    #     return HttpResponse("You are not allowed")

    if request.method == "POST":
        form = CreateRoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room Updated successfully')
            return redirect('home')
        else:
            messages.error(request, 'ERROR')
            

    context = {'form':form}
    return render(request, 'base/update_room.html', context)

@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    # if request.user.username != room.host.username or request.user.is_superuser:
    #     return HttpResponse("You are not allowed")

    if request.method == "POST":
        room.delete()
        return redirect('home')
    
    context = {'room':room}
    return render(request, 'base/delete_room.html', context)

@login_required(login_url='login')
def delete_message(request, pk):
    my_message = Message.objects.get(id=pk)

    # if request.user.username != room.host.username or request.user.is_superuser:
    #     return HttpResponse("You are not allowed")

    if request.method == "POST":
        my_message.delete()
        return redirect('home')
    
    context = {'my_message':my_message}
    return render(request, 'base/delete_room.html', context)

@login_required(login_url='login')
def shop(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'base/shop.html',context)

@login_required(login_url='login')
def post_item(request):
    form = CreateItemForm()
    if request.method == "POST":
        form = CreateItemForm(request.POST)
        owner = Profile.objects.get(username=request.user.username)
        if form.is_valid():
            item = form.save(commit=False)
            item.creator = owner
            item.save()
            messages.success(request, 'Item Posted successfully')
            return redirect('shop')
        else:
            messages.error(request, 'ERROR')

    context = {'form':form}
    return render(request, 'base/post_item.html',context)

@login_required(login_url='login')
def buy_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.sold = True
        item.buyer = request.user.username
        print(item.buyer)
        item.save()
        return redirect('shop')

    return render(request, 'base/buy_item.html')

def visualize(request):
    d = {}

    topics = Topic.objects.all()

    for i in topics:
        d[i] = []

    for i in topics:
        rooms = Room.objects.filter(topic = i)
        for j in rooms:
            if j.topic == i:
                d[i].append(j.title)
    data = []
    lable = []

    for i in d:
        lable.append(i.name)
        data.append(len(d[i]))

    print(lable)
    print(data)

    context = {
        'lable':lable,
        'data':data
    }

    return render(request, 'base/visualize.html', context)