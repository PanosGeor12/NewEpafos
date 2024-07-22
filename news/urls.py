from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'news'

urlpatterns = [
    path('manager/createpost/', views.CreatePost, name='Create_Post'),
    path('manager/editpost/<int:id>',views.EditPost, name='Edit_Post'),
    path('manager/post/<int:year>/<int:month>/<int:day>/<slug:post>', views.ManagerPostDetails, name='Manager_Post_Details'),
    path('schoolnews/post/<int:year>/<int:month>/<int:day>/<slug:post>', views.PostDetails, name='Post_Details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
