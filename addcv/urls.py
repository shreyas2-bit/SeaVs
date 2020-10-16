from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('personal/', views.personal,name='personal'),
     path('education/', views.educational,name='ed'),
     path('experiences/', views.experiences,name='ex'),
     path('',views.createcv, name='create-cv-page'),
     path('madecv/',views.cv,name='cv'),
     path('export-pdf', views.export_pdf, name='export-pdf'),
     path('upload/', views.upload, name = 'upload'),
 ]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
