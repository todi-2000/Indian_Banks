from django.urls import path
from .views import DetailView,BranchView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('city/<str:city>/<str:bankname>/',BranchView.as_view()),
    path('ifsc/<str:ifsc1>/',DetailView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])