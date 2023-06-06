from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register),
    path('', login_view, name='login'),
    path('maqolalar/', blog_view),
    path('logout/', logout_view),
    path('bitta_maqola/<int:son>/', bitta_maqola),
]
