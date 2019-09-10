from linepy import *

token = "EIeSHzDNEddznvFuSxe2.Gi32dMR0hTP/xzDpc+52eG.PB5BFO1eBIwlkAS7gWrAUeSR4mhe1lKUvT2A0U32ECs="
client = LINE(token,appType="WIN10")
typee = int(input("Type\n1.) Joined\n2.) Invited\n3.) Joined And Invited\nYour Input : "))
if typee == 1:
	grp = client.getGroupIdsJoined()
	no = 0
	for g in grp:
		no += 1
		print("\n{}.\tGroup : {}\n\tID : {}".format(no,client.getGroup(g).name,g))
	print("Total Group Joined : {}".format(no))
if typee == 2:
	grp = client.getGroupIdsInvited()
	no = 0
	for g in grp:
		no += 1
		print("\n{}.\tGroup : {}\n\tID : {}".format(no,client.getGroup(g).name,g))
	print("Total Group Invited : {}".format(no))
if typee == 3:
	grp = client.getGroupIdsJoined()
	grup = client.getGroupIdsJoined()
	no = 0
	num = 0
	for g in grp:
		no += 1
		print("\n{}.\tGroup : {}\n\tID : {}".format(no,client.getGroup(g).name,g))
	print("Total Group Joined : {}".format(no))
	for h in grup:
		num += 1
		print("\n{}.\tGroup : {}\n\tID : {}".format(no,client.getGroup(h).name,h))
	print("Total Group Invited : {}".format(num))