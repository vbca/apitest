from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from . import views, api_views
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# router = DefaultRouter()
# router.register(r'persons', api_views.PersonViewset)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    # url(r'^persons/$', api_views.PersonView.as_view()),
    # url(r'^persons/(?P<pk>[0-9]+)/$', api_views.PersonView.as_view()),
    # url(r'^upload/(?P<filename>[^/]+)$', api_views.FileUploadView.as_view()),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    
    #################################################################

    url(r'^complaint_category/$', api_views.Complaint_Category.as_view()),  
    url(r'^complaint/$', api_views.Complaint.as_view()),  
    url(r'^article/$', api_views.Article.as_view()), 
    url(r'^login/$', api_views.Login.as_view()),  
    url(r'^register/$', api_views.Register.as_view()),  
    
    #company
    #List
    url(r'^company/$', api_views.CompanyView.as_view()),
    url(r'^company_create/$', api_views.CompanyCreate.as_view()),
    
]