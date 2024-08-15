from django.urls import include, path

# USING APPROACH 1

# from .views import PersonDetailView, PersonListView, PersonDeleteView, PersonUpdateView, PersonCreateView
# urlpatterns = [
#      path('', index),
#      path('all/', PersonListView.as_view(), name='Get All'),
#      path('person/<int:pk>/', PersonDetailView.as_view(), name='Person Details'),
#      path('person/create/', PersonCreateView.as_view(), name='person-create'),
#      path('person/<int:pk>/update/', PersonUpdateView.as_view(), name='person-update'),
#      path('person/<int:pk>/delete/', PersonDeleteView.as_view(), name='person-delete'),
# ]

# ----------------------------------------

# USING APPROACH 2

from .views import PersonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

