from django.contrib import admin
from django.urls import path, include
from apps.tickets.views import no_framework, FBV_list, FBV_pk

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # no rest framework
    path('test/', no_framework),
    # rest framework get & post
    path('rest/', FBV_list),
    # rest framework get & put & delete
    path('rest/<int:id>', FBV_pk),
]
