from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('personal/', views.personal,name='personal'), #personal form
     path('education/', views.educational,name='ed'),   #education form
     path('experiences/', views.experiences,name='ex'), #job form
     path('project/', views.project,name='project'),    #project form
     path('',views.createcv, name='create-cv-page'),    #createcv page
     path('resume/', views.resumes,name='resume'),      #resume form
     path('madecv/',views.cv,name='cv'),                #cv2
     path('export-pdf', views.export_pdf, name='export-pdf'),
     path('upload/', views.upload, name = 'upload'),
 ]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
