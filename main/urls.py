from django.urls import path
from main.views import show_main
from main.views import create_product
from main.views import edit_product
from main.views import delete_product
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import show_xml
from main.views import show_json
from main.views import show_json_by_id
from main.views import show_xml_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('edit-product/uuid:id', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]