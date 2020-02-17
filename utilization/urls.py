from django.urls import path
from utilization import views
#template tagging
app_name = 'utilization'

urlpatterns = [
    path('',views.view_weekVarGet,name='view_weekVarGet'),
    path('newweek',views.view_utilization.as_view(),name='view_utilization'),
    path('edit-names',views.view_utilizationNames,name='view_utilizationNames'),
    path('edit-projects',views.view_utilizationProjects,name='view_utilizationProjects'),
]
