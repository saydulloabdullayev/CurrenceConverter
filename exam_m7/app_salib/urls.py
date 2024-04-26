from django.urls import path


from .views import (
    SalibListAPIView,
    SalibDetailAPIView,
    SalibCreateAPIView,
    SalibDeleteAPIView, 
    SalibUpdateAPIView,
)

urlpatterns=[
    path('', SalibListAPIView.as_view()),
    path('create/', SalibCreateAPIView.as_view()),
    path('update/<int:pk>',SalibUpdateAPIView.as_view()),
    path('delete/<int:pk>', SalibDeleteAPIView.as_view()),
    path('<int:pk>/', SalibDetailAPIView.as_view()),  

]


