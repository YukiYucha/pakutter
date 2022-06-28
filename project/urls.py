from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pakutter/',include('pakutter.urls')),
    path('admin/', admin.site.urls),
    # auth
    path('account/', include('allauth.urls')),
]
