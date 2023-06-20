from django.urls import path
from .views import *

urlpatterns = [
    path('create_demo/',employee_creation_view,name='create_demo'),
    path('create/',em_create,name='create'),   
    path('contact/',contactus,name='contact'),   
    path('list/',em_list,name='list'),   
    path('update/<int:id>',em_update,name='update'),   
    path('detail/<int:id>',em_detail,name='detail'),   
    path('delete/<int:id>',em_delete,name='delete'),   
    # path('render1/',Rendering_data,name='render')
    path('render1/',Render_data.as_view(),name='render')
]