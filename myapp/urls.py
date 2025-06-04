from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("signup/", views.signup, name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logoutPage, name="logout"),
    path("login/", views.loginPage, name="login"),
    path("dashboard/cattle/", views.cattle, name="cattle"),
    path("dashboard/cattle/add/", views.addCattle, name="addCattle"),
    path("dashboard/cattle/<int:id>/", views.cattleInfo, name="cattleInfo"),
    path("dashboard/cattle/<int:id>/erase", views.eraseCattle, name="eraseCattle"),
    path("dashboard/statistics/", views.statistics, name="statistics"),
    path("dashboard/statistics/graph/race", views.graphRace, name="graphRace"),
    path("dashboard/statistics/graph/sex", views.graphSex, name="graphSex"),
    path("dashboard/statistics/graph/price-by-kg", views.graphPriceByKg, name="graphPriceByKg"),
]