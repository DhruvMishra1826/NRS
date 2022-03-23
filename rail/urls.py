from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("pnrstatus/", views.pnrstatus, name="PNRStatus"),
    path("searchtrain/", views.searchtrain, name="SearchTrain"),
    path("searchresult/", views.searchresult, name="SearchResult"),
    path("booktrain/", views.booktrain, name="BookTrain"),
    path("pnrstatus/", views.pnrstatus, name="PnrResult"),
    path("getpnrstatus/", views.getpnrstatus, name="getPnrStatus"),
    path("searchtrainresult/", views.searchtrainresult, name="SearchTrainResult"),
    path("contact/",views.contact,name="ContactUs"),
]