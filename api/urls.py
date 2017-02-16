from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'hackathon/get/countdowns$', views.hackathon.get.CountdownsView.as_view()),
    url(r'hackathon/get/maps$', views.hackathon.get.MapsView.as_view()),
    url(r'hackathon/get/schedule_items$', views.hackathon.get.ScheduleItemsView.as_view()),
    url(r'hackathon/get/sponsors$', views.hackathon.get.SponsorsView.as_view()),
    url(r'hackathon/get/updates$', views.hackathon.get.UpdatesView.as_view()),
    url(r'hackathon/get/stats$', views.hackathon.get.StatsView.as_view()),

    url(r'user/login$', views.user.LogInView.as_view(), name='user-login'),
    url(r'user/register$', views.user.RegisterView.as_view(), name='user-register'),
    url(r'user/get/profile$', views.user.get.ProfileView.as_view(), name='user-get-profile'),
    url(r'user/get/groups', views.user.get.GroupsView.as_view(), name='user-get-groups'),
    url(r'user/password/reset/complete', views.user.password.CompleteResetView.as_view()),
    url(r'user/password/reset/start', views.user.password.StartResetView.as_view()),

    url(r'hacker/register$', views.hacker.RegisterView.as_view(), name='hacker-register'),
    url(r'hacker/get/profile$', views.hacker.get.ProfileView.as_view(), name='hacker-get-profile'),
    url(r'hacker/csv/by_school', views.hacker.csv.BySchoolCsv.as_view()),

    url(r'judge/register$', views.judge.RegisterView.as_view(), name='judge-register'),
    url(r'judge/get/profile$', views.judge.get.ProfileView.as_view(), name='judge-get-profile'),

    url(r'mentor/register$', views.mentor.RegisterView.as_view(), name='mentor-register'),
    url(r'mentor/get/profile$', views.mentor.get.ProfileView.as_view(), name='mentor-get-profile'),
    url(r'mentor/request/create$', views.mentor.request.CreateView.as_view()),
    url(r'mentor/request/claim$', views.mentor.request.ClaimView.as_view()),
    url(r'mentor/request/release_claim$', views.mentor.request.ReleaseClaimView.as_view()),
    url(r'mentor/request/get/all$', views.mentor.request.get.AllView.as_view()),

    url(r'organizer/register$', views.organizer.RegisterView.as_view(), name='organizer-register'),
    url(r'organizer/get/profile$', views.organizer.get.ProfileView.as_view(), name='organizer-get-profile'),

    url(r'school/get$', views.school.GetView.as_view(), name='organizer-register'),

    url(r'attendee/rsvp$', views.attendee.RsvpView.as_view())
]

if settings.DEBUG:
    urlpatterns.extend([

    ])
