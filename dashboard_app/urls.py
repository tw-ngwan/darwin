from django.urls import path
# from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url 

from . import views

# Url patterns to look out for 
urlpatterns = [
    path('', views.index, name='index'),
    path('stored', views.index, name='stored'),
    path('post_modelresults/', views.handle_model_results),
    path('upload/', views.upload_file, name='upload_file'),
]



urlpatterns += staticfiles_urlpatterns()
print("URLs:", urlpatterns)
