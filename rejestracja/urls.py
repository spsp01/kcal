from django.urls import path
from rejestracja.views import DietetykView, RejestracjaView, success

app_name = 'rejestracja'
urlpatterns = [
    path('', RejestracjaView.as_view(), name='index' ),
    path('jan-kowalski',DietetykView.as_view(), name='jan-kowalski'),
    path('ada-wspaniala', DietetykView.as_view(), name='ada-wspaniala'),
    path('success', success, name='success'),
   # path('test', views.detail, name='test' )
]