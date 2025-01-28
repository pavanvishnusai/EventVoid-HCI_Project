from django.urls import path
from myapp.views import event_details, index, signup_view, login_view,event_list, submit_booking, booking_form,confirmation

urlpatterns = [
    path('', index, name='myapp/index'),
    path('signup/', signup_view, name='myapp/signup'),
    path('login/', login_view, name='myapp/login'),
    path('events/',event_list, name='event_view'),
    path('event/<int:event_id>/', event_details, name='event_details'),
    # path('submit-booking/<int:event_id>/',submit_booking, name='submit_booking'),
    path('booking/form/<int:event_id>/', booking_form, name='booking_form'),
    path('submit_booking/<int:event_id>/', submit_booking, name='submit_booking'),
    #   path('mybookings/', bookings, name='bookings'),
    # Other URL patterns for your app
]
