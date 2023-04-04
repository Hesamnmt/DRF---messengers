from django.urls import path, include
from messenger_app.views import MessageView

urlpatterns = [
    path("api/messages/", MessageView.as_view(), name="message_list"),
]