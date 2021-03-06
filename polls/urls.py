from django.urls import path

from . import views

urlpatterns=[
    path('', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'), # AJAX
    path('all_data',views.all_data,name='all_data')

]