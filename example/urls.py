
from django.urls import include, path

from . import views

from rest_framework import routers

from example.views import PersonViewSet, SpeciesViewSet




router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)
# router.register(r'dislike', dislikeset)

urlpatterns=[
    path("", views.index, name="index"),
   
   path('', include(router.urls)),
   
]




























# # import routers
#  
# # import everything from views
#  
# # define the router
#  
# # define the router path and viewset to be used
#  
# # specify URL Path for rest_framework
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls'))
# ]