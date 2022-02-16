from unicodedata import name
from django.urls import path
from . import views


# in Urls we make a our urls and we define what they refer too , in other words we connect our views with urls



# we are linking our views to our urls here
urlpatterns = [
    path('registeruser/', views.registeruser, name='registeruser'),
    path('home/',views.home_hospital,name='home-hospital'),
    path('register/', views.Register.as_view(), name='register'),
    path('search',views.search_patient, name='search'),
    path('patient/<str:id>', views.patientInfo, name='patientInfo'),
    path('queue/', views.add_queue, name='add_queue'),
    path('dequeue/<str:id>', views.dequeue, name = 'dequeue'),
    path('manage-queue/', views.queue_list, name = 'manage_queue'),
    path('delete-patient/<pk>', views.PatientDeleteView.as_view(), name= 'delete-patient'),
    path('edit-patient/<pk>', views.PatientUpdateView.as_view(), name='edit-patient'),
    path('edit-condition/<pk>', views.ConditionUpdateView.as_view(), name='edit-condition'),
    path('patient-history/<str:id>', views.CreateCondition.as_view(), name='patientHistory'),
    path('old-history/<str:id>', views.old_history, name='old_history'),
    path('history-info/<str:id>', views.history_info, name='history'),
    path('doctor/', views.doctor_home, name="doctorHome"),
    path('account/', views.account, name="account"),
]