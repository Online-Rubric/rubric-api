from django.urls import path

from .views import RubricList, RubricDetail, StudentList, ProctorList

urlpatterns = [
    path("", RubricList.as_view(), name="Rubric_list"), 
    path("<int:pk>/", RubricDetail.as_view(), name="Rubric_detail"),
    path("students/", StudentList.as_view(), name="Student_detail"),
    path("proctors/", ProctorList.as_view(), name="Proctor_detail"),
]
