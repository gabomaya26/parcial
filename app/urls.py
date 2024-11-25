from django.urls import path
from . import views

urlpatterns = [
    path('messages/', view=views.get_messages, name="get-messages"),
    path('messages/create/', view=views.create_message, name="create-message"),
    
]
