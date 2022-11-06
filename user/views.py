from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomAdminCreationForm, EditProfileForm, CreateRankForm
from django.contrib.auth.models import User
from .models import CompRank, Profile

# Create your views here.
def profiles(request):
    #SELECT * FROM user_profile
    all_profiles = Profile.objects.all()
    context = {'all_profiles': all_profiles}
    return render(request, 'user/profiles.html', context)

def userProfile(request, pk):
    #SELECT * FROM user_profile WHERE id = pk
    my_profile = Profile.objects.get(id=pk)
    #SELECT * FROM base_room INNER JOIN user_profile on base_room.host = user_profile.id
    all_rooms = my_profile.room_set.all()
    print(my_profile)
    #SELECT * FROM base_message INNER JOIN user_profile on base_message.user = user_profile.id
    activity_messages = my_profile.message_set.all()
    #SELECT count(*) from base_room where base_room.host = request.user
    room_count = all_rooms.count()
    context = {
        'my_profile':my_profile,
        'all_rooms':all_rooms,
        'room_count':room_count,
        'activity_messages':activity_messages
    }
    return render(request, 'user/userprofile.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # INSERT INTO user_user VALUES (username,password)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is wrong')

    return render(request, 'user/login.html')

def user_registration(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            print(user.is_staff)
            user.save()

            messages.success(request, "User Account was created")

            return redirect('login')
        else:
            messages.success(request, "An error has occurred during registration")

    context = {'form':form}
    return render(request, 'user/user_registration.html', context)

def admin_registration(request):
    form = CustomAdminCreationForm()
    
    if request.method == "POST":
        form = CustomAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_staff = True
            user.is_superuser = True
            user.save()

            messages.success(request, "Admin Account was created")

            return redirect('login')
        else:
            messages.success(request, "An error has occurred during registration")

    context = {'form':form}
    
    return render(request, 'user/admin_registration.html', context)

def logoutPage(request):
    logout(request)
    messages.error(request, 'User logged out successfully')
    return redirect('login')

def edit_user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = EditProfileForm(instance=profile)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=profile.id)

    context = {'form':form}
    return render(request, 'user/edit_user_profile.html', context)

def create_rank(request):
    form = CreateRankForm()
    # INSERT INTO user_comprank(owner,game_name,rank) VALUES (request.user.username, request.get('gameName'), request.get('rank))
    if request.method == "POST":
        sender = Profile.objects.get(username=request.user.username)
        form = CreateRankForm(request.POST)
        if form.is_valid():
            rank = form.save(commit=False)
            rank.owner = sender
            rank.save()
            return redirect('user-profile', pk=sender.id)


    context = {'form':form}
    return render(request, 'user/create_rank.html', context)

def delete_rank(request, pk):
    rank = CompRank.objects.get(id=pk)
    # DELETE FROM user_comprank WHERE id=pk
    if request.method == "POST":
        rank.delete()
        return redirect('profiles')
    return render(request, 'base/delete_room.html')