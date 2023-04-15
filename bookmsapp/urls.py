from .views import *

urlpatterns=[
 path('register',register.as_view(),name='login'),
 path('login',login.as_view(),name='login'),
 path('index/',showindex),
 path('uploaddisplay',uploaddisplay.as_view(),name='uploaddisplay'),

 path('delete/<pk>',delete.as_view(),name='uploaddisplay'),
 path('editbook/<pk>',editbook.as_view(),name='uploaddisplay'),
 path('profile1/',profile1),
 path('download/',dowloadpage.as_view(),name='dowloadpage'),
 path('logout/',customlogout.as_view(),name='logout'),
 path('index/',showindex,name='index'),

 ]