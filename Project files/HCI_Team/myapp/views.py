from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Events_List
# from .forms import BookingForm
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from .models import Events_List
# from .models import Booking
from .models import Participant




def index(request):
    return render(request, 'index.html')
def map_view(request):
    return render(request, 'map.html')
def support_view(request):
    return render(request, 'support.html')
def aboutus_view(request):
    return render(request, 'aboutus.html')
def events_view(request):
    return render(request, 'events_list.html')
def event_details(request):
    return render(request, 'event_details.html')
def register_now(request):
    return render(request, 'register_now.html')
def calender(request):
    return render(request, 'calender.html')
def payment(request):
    return render(request, 'payment.html')
def confirmation(request):
    return render(request, 'confirmation.html')
def my_bookings(request):
    return render(request, 'mybookings.html')

def event_details(request, event_id):
    events = get_object_or_404(Events_List, id=event_id)
    return render(request, 'event_details.html', {'event': events})
def booking_page(request):
    user = request.user
    events = Event.objects.filter(booking__user=user)
    return render(request, 'booking_page.html', {'events': events})


# def add_booking(request, event_id):
#     event = Event.objects.get(id=event_id)
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.event = event
#             booking.date = event.date
#             booking.time = event.time
#             booking.save()
#             return redirect('booking_confirmation')
#     else:
#         form = BookingForm()
#     return render(request, 'mybookings.html', {'form': form, 'event': event})
#     # return render(request, 'booking_form.html', {'form': form, 'event': event})

def event_list(request):
    events = Events_List.objects.all()
    print(events)
    print('hi')
    return render(request, 'events_list.html', {'events': events})

def booking_form(request, event_id):
    event = get_object_or_404(Events_List, pk=event_id)
    return render(request, 'booking_form.html', {'event': event})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Import the messages module for error messages

def submit_booking(request, event_id):
    event = get_object_or_404(Events_List, id=event_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        participant = Participant(event=event, name=name, email=email, phone=phone)
        participant.save()

        # Optionally, you can redirect to a success page
        return redirect('confirmation')

    context = {
        'event': event,
    }
    return render(request, 'booking_form.html', context)    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myapp/index')
        else:
            return HttpResponse("Invalid email or password")
    else:
        return render(request, 'login.html')
def signup_view(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_user=User.objects.create_user(name,email,password)
        my_user.save()
        return redirect('login')
        
       
    return render(request, 'signup.html')
def logout_view(request):
    logout(request)
    return redirect('index')

def my_bookings(request):
    participants = Participant.objects.all()
    return render(request, 'mybookings.html', {'participants': participants})
