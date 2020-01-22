from django.urls import path
from demo_app import views

urlpatterns=[
    path('contact_us/', views.contact_us, name='contact'),
    path('list_students/', views.list_students, name="list_students"),
    path('add_student/', views.add_student, name="add_student"),
    path('delete_student/<int:id>/', views.delete_student, name="delete_student"),
    path('edit_student/<int:id>/', views.EditStudent.as_view(), name="edit_student"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name="user_register"),
    path('list_rooms/', views.ListRooms.as_view(), name='list_rooms'),
    path('detail_room/<int:id>/', views.RoomDetail.as_view(), name='detail_room'),
    path('contact_us/', views.ContactView.as_view(), name='contact'),
    path('add_room/', views.RoomCreateView.as_view(), name='add_room'),
    path('edit_room/<int:id>/', views.RoomUpdateView.as_view(), name='edit_room'),
    path('delete_room/<int:id>/', views.RoomDeleteView.as_view(), name='delete_room')
]