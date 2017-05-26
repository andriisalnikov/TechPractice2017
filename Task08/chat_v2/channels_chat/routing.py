# In routing.py
from channels import route
from channels import include

channel_routing = [
    include("chat.routing.websocket_routing"),
    include("chat.routing.custom_routing"),
]

