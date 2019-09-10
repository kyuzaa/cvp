from linepy import *

token = "uc04f92a416d795bbb4a3559f1e9d2ce3:aWF0OiAxNTU1MDAxNzI4ODk1Cg==..QoKAnY2EHb3gTforOtFMWdWdT+Y="
client = LINE(token,appType="IOS")
gid = str(input("Group ID : "))
path = str(input("Image Path Profile Picture : "))
pathC = str(input("Image Path Cover Picture : "))
print("#### INFO ###\nGROUP NAME : {}\n##############".format(client.getGroup(gid).name))
mid = [m.mid for m in client.getGroup(gid).members]
no = 0
for i in mid:
	no += 1
	if i not in ["u3123ee53be23d75ef99a95f206ecc978","u808df60e6af41eda7e5d974f0bfe7612","u150efa85cd885f76e90e7e7d605a64b1"]:
		try:
			client.forceUpdate(i,path)
			#client.forceUpdateCover(i,pathC)
		except:
			continue
		print("Success Force Update Profile : {}".format(client.getContact(i).displayName))
print("Total Members : {}".format(no))

if client.getGroup(gid).invitee != []:
	mmid = [ms.mid for ms in client.getGroup(gid).invitee]
	num = 0
	for a in mid:
		num += 1
		if a not in ["u3123ee53be23d75ef99a95f206ecc978","u808df60e6af41eda7e5d974f0bfe7612","u150efa85cd885f76e90e7e7d605a64b1"]:
			try:
				client.forceUpdate(a,path)
				#client.forceUpdateCover(a,pathC)
			except:
				continue
			print("Success Force Update Profile : {}".format(client.getContact(a).displayName))
	print("Total Pendings : {}".format(num))