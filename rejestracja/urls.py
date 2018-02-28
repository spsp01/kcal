from django.urls import path
import rejestracja.views as views

app_name = 'rejestracja'
urlpatterns = [
    path('', views.RejestracjaView.as_view(), name='index' ),
    path('jan-kowalski', views.DietetykView.as_view(), name='jan-kowalki'),
    path('ada-wspaniala', views.DietetykView.as_view(), name='ada-wspaniala')
]