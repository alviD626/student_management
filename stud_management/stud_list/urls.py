from django.urls import path
from . import views

urlpatterns = [
    path('',views.ApiOverview,name='home'),
    path('create/',views.add_items,name='add-items'),
    path('all/',views.view_items, name='view_items'),
    path('update/<int:pk>/',views.update_items,name='update-items'),
    path('item/<int:pk>/delete/',views.delete_items,name='delete-items'),
]
# {
#     "category":"food",
#     "subcategory":"vegetables",
#     "name":"potato",
#     "amount":25
# }
# {
#     "name":"alvi",
#     "roll":15,
#     "email":"alimostakim68@gmail.com",
#     "group":"engineer"
# }