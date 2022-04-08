from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ui.urls'), name='home'),
    path('history/', include('history.urls'), name='history')
]
