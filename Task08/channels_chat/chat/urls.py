from django.conf.urls import url
from chat.views import home, get_messages, upload_photo, RoomEditView, GroupRoomEditView, get_group_messages, GroupChatCreateView, remove_group_chat, report_message, invite_friends, reports_mangement


urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^(?P<roomID>\d+)/$', home, name="home_with_id"),
    url(r'^group/(?P<group_roomID>\d+)/$', home, name="group_with_id"),
    url(r'^get_messages/(?P<room>.+)/$', get_messages, name="get_messages"),
    url(r'^get_group_messages/(?P<group>.+)/$', get_group_messages, name="get_group_messages"),
    url(r'^upload_photo/$', upload_photo, name="upload_photo"),
    url(r'^room-edit/(?P<room>.+)/$', RoomEditView.as_view(), name="edit_room"),
    url(r'^edit-group-room/(?P<room>.+)/$', GroupRoomEditView.as_view(), name="edit_group_room"),
    url(r'^create-group-chat/', GroupChatCreateView.as_view(), name="create_group_chat"),
    url(r'^remove-group-chat/(?P<room>.+)/$', remove_group_chat, name="remove_group_chat"),
    url(r'^invite_friends/$', invite_friends, name="invite_friends"),
    url(r'^report_message/(?P<type>.+)/(?P<id>.+)/$', report_message, name="report_message"),
    url(r'^reports-management/$', reports_mangement, name="reports_management"),
]
