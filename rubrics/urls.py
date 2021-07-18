from django.urls import path

from .views import RubricList, RubricDetail

urlpatterns = [
    path("", RubricList.as_view(), name="Rubric_list"),
    path("<int:pk>/", RubricDetail.as_view(), name="Rubric_detail"),
]
