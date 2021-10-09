# import accounts.views
# import accounts.templates
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('accounts.urls')),
    #추가
    path('accounts/auth', include("knox.urls"))

]




# from django.urls import path, include
# from django.contrib import admin
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("api/", include("api.urls")),
#     path("api/auth", include("knox.urls")),
# ]