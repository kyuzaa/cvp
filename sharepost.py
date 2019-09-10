from linepy import *

token = "u6216e3374e5168a4cf28ca5e9c90b18f:aWF0OiAxNTU0NzA5OTg3MzkyCg==..DlUUWa7cx8YzP5EmS9mGGIQ8n8s="
#mid = "uabfd0f876b3e50b9235e427ee67ac1a4"
#mid = "u808df60e6af41eda7e5d974f0bfe7612"
mid = "c2e68a806f238074e166a899411224ae5"
postId = "115628220030308"
postid = "115466764380405"

client = LINE(token,appType="IOS")
#client.acceptGroupInvitation("c2e68a806f238074e166a899411224ae5")
#client.sendMessage(mid,".")
#for i in range(10):
for i in range(1000):
    client.sendPostToTalk(mid,"1154667643804054434")
    client.sendPostToTalk(mid,"1156282200303080436")
    print("Share ke : {}".format(str(i)))

print("###########")
print("SUCCESS SEND !")
