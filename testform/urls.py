from django.urls import path
from testform import views
#template tagging
app_name = 'testform'

urlpatterns = [
    path('',views.view_testform.as_view(),name='view_testform'),
    path('blocks',views.view_testformTable.as_view(),name='view_testformList'),
    path('delete',views.view_testformTableDelete.as_view(),name='view_testformListDelete'),
    # path('blocks/<int:pk>',views.view_testformDetail.as_view(),name='view_testformDetail'),
    path('blocks/<int:pk>',views.view_testformUpdate.as_view(),name='view_testformUpdate'),
    path('blocks/<int:pk>/delete',views.view_testformDelete.as_view(),name='view_testformDelete'),
]
