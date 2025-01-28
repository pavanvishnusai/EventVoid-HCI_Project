from django import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from myapp.views import aboutus_view, calender, confirmation, event_list,events_view, index, login_view, logout_view, map_view, my_bookings, payment, register_now,support_view, signup_view, event_details, booking_form, submit_booking
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('index/', index, name='index'),
    path('myapp/', include('myapp.urls')),
    
    # Other URL patterns
    path('event/details/<int:event_id>/',event_details, name='event_details'),

    path('map/', map_view, name='map'),
    path('support/', support_view, name='support'),
    path('aboutus/', aboutus_view, name='aboutus'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('events_list/', event_list, name='events_list'),
    path('event_details/',event_details, name='event_details'),
    path('register_now/',register_now, name='register_now'),
    path('calender/',calender, name='calender'),
    path('payment/',payment, name='payment'),
    path('my_bookings/',my_bookings, name='my_bookings'),

    path('confirmation/',confirmation, name='confirmation'),
    # path('booking/', booking_form, name='booking'),
    
    path('booking/form/<int:event_id>', booking_form, name='booking_form'),
    # path('submit_booking/<int:event_id>/', submit_booking, name='submit_booking'),
    path('submit_booking/<int:event_id>/', submit_booking, name='submit_booking'),
    # path('submit-booking/', views.submit_booking, name='submit_booking'),
    # path('booking/', booking_view, name='booking'),
    # path('booking/add/', add_booking, name='add_booking')
    
  ]

