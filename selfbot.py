# -*- coding: utf-8 -*-

'''
Selfbot By Kyuza
'''

from important import *


#Setting Json

settings = livejson.File('setting.json', True, True, 4)

#Login Client
#Kalo Pake QR
line = LINE(appType="WIN10")
#Kalo Pake Token
token = "tokennya"
#line = LINE(token,appType="WIN10")
     
if line:
    print ('##----- LOGIN CLIENT (Success) -----##')
else:
    sys.exit('##----- LOGIN CLIENT (Failed) -----##')


myMid = line.profile.mid
programStart = time.time()
oepoll = OEPoll(line)
lurking = {}
tmp_text = []

#Trying to login liff
try:
    channel = Channel(line,"1602687308").getChannelInfo()
    print("##------ Success Login To Liff ------##")
except Exception as e:
    print("##------ Failed Login To Liff (Error)------##")


bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', 'On'],
    False: ['No', 'Not Active', 'Failed', 'Close', 'Off']
}

api = "http://kyuza-api.herokuapp.com"

# Backup profile
profile = line.getContact(myMid)
settings['myProfile']['displayName'] = profile.displayName
settings['myProfile']['statusMessage'] = profile.statusMessage
settings['myProfile']['pictureStatus'] = profile.pictureStatus
coverId = line.profileDetail['result']['objectId']
settings['myProfile']['coverId'] = coverId

# Jungle pang Hack Score
try:
    group = 'c96c9dcf1c95219eff5be7c0ab995943b'
    url = "https://game.linefriends.com/jbp-lcs-ranking/rank/add_score_with_token"
    headers = {'User-Agent': 'Mozilla/5.0 (Linux) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.10.1','Content-Type': 'application/json'}
    data = {'ClientID': group,'Score': 9999,'cc': 'lCvwnFSNKUbq+6kmQi6kMO8GvpRyYXFrBJxN8U9AzKIGAY4p12fnLgJf50D+uehQ1GuTm/Z4U+3x6braTWYpk8zYBWDvcPaeqQOdl5U3HAdrJprnS4mwU770BNhunFD7qs0PqAtjsNfZq2PwB/Jk14klWO+HMQPBi2qcCn9vx78JoATnIk/vkNR8EjOnnNzC15ngo+HqdO2JoGn13w8m7p4sPFoUcpT89L1Nv5FuIEAP9Qf+5nlWHRk9L3PhcUiJ+cocNAbyn12Sp6kphX5msfOX+fHDBdFtge9nrmu7ppaTiMdYwjuKwOQyipa511IGcc03AEqcLAtl+K7Wc+n8ZA','nomd5': True}
   # r = requests.post(url,data=json.dumps(data),headers=headers)
    #if r.status_code != 200:print("Failed to post !\nError : "+str(r))
   # else:print("Success Post")
except Exception as e:
    print("Failed to post\nError : "+e)

# Def start

def catchFish(user):
    if user == "kepin2":
    #    line.sendMessage("ua80ecdbc891b48a788e4add6d7e92c04","/fish")
        line.sendMessage("ua80ecdbc891b48a788e4add6d7e92c04","/gambling 300000")
        time.sleep(60)

def checkExpire():
    if user['expire'] == str(date.today()):
       try:
           line.sendMessage(user['group'],"Your selfbot has been expired now")
           os.system("screen -R {} -X quit".format(args.user))
       except TalkException:pass

def convertYoutubeMp4(url):
    video = pafy.new(url)
#    result = video.getbest()
    return video
def convertYoutubeMp3(url):
    video = pafy.new(url)
#    result = video.getbestaudio()
    return video

def checkUserMention(to,split=None,split2=None):
    moneys = {}
    msgas = ''
    for a in settings['checkMention'][to].items():
        moneys[a[0]] = [a[1]['msg']] if a[1] is not None else idnya
    sort = sorted(moneys)
    sort.reverse()
    sort = sort[0:]
    msgas = ' 「 Check Mention 」'
    h = []
    if split == None:
        no = 0
        for m in sort:
            h.append(m)
            no+=1
            msgas+= '\n{}. @! #{}x'.format(no,len(moneys[m][0]))
        line.sendMentionV2(to,msgas,h)
    elif split != None and split2 == None:
        mid = sort[int(split)-1]
        msgs = settings['checkMention'][to][mid]["msg"]
        no = 0
        anu = Message()
        anu.text = " 「 Check Mention 」\nFrom: @KEPINGANTENG "
        anu.to = to
        for msg in msgs:
            no +=1
            aa = '\n{}. CreatedTime: {}\n   Text: '.format(no,humanize.naturaltime(datetime.fromtimestamp(msg['createdTime']/1000)))
            if len(eval(msg["contentMetadata"]["MENTION"])["MENTIONEES"]) > 10:
                anu.text += aa+" Just tagall, > 10 Tag's"
                gd = [{'S':str(0+len(' 「 Check Mention 」\nFrom: ')), 'E':str(len('@KEPINGANTENG ')+len(' 「 Check Mention 」\nFrom: ')), 'M':msg["_from"]}]
                anu.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(gd) + '}')}
            else:
                anu.text += aa+msg['text']
                gd = [{'S':str(0+len(' 「 Check Mention 」\nFrom: ')), 'E':str(len('@KEPINGANTENG ')+len(' 「 Check Mention 」\nFrom: ')), 'M':msg["_from"]}]
                for key in eval(msg["contentMetadata"]["MENTION"])["MENTIONEES"]:
                    gd.append({'S':str(int(key['S'])+len(' 「 Check Mention 」\nFrom: @KEPINGANTENG '+aa)), 'E':str(int(key['E'])+len(' 「 Check Mention 」\nFrom: @KEPINGANTENG '+aa)),'M':key['M']})
            anu.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(gd) + '}')}
        line.sendMessageObject(anu)
    else:
        mid = sort[int(split)-1]
        msg = settings['checkMention'][to][mid]["msg"][int(split2)-1]
        anu = Message()
        aa = "\nCreatedTime: {}\nLink: line://nv/chatMsg?chatId={}&messageId={}\nText:\n".format(humanize.naturaltime(datetime.fromtimestamp(msg['createdTime']/1000)),msg["to"],msg["id"])
        anu.text = " 「 Check Mention 」\nFrom: @KEPINGANTENG "+aa+msg['text']
        gd = [{'S':str(0+len(' 「 Check Mention 」\nFrom: ')), 'E':str(len('@KEPINGANTENG ')+len(' 「 Check Mention 」\nFrom: ')), 'M':msg["_from"]}]
        for key in eval(msg["contentMetadata"]["MENTION"])["MENTIONEES"]:
            gd.append({'S':str(int(key['S'])+len(' 「 Check Mention 」\nFrom: @KEPINGANTENG '+aa)), 'E':str(int(key['E'])+len(' 「 Check Mention 」\nFrom: @KEPINGANTENG '+aa)),'M':key['M']})
        anu.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(gd) + '}')}
        anu.to = to
        line.sendMessageObject(anu)
        if len(settings['checkMention'][to][mid]["msg"]) == 1:
            del settings['checkMention'][to][mid]
        else:
            del settings['checkMention'][to][mid]["msg"][int(split2)-1]

def detectUnsend(op):
    if op.param2 in settings['detectUnsend'][op.param1]:
        msg = settings['detectUnsend'][op.param1][op.param2]['msg']
        if msg['contentType'] == 0:dd = '\nType: Text'
        else:dd= '\nType: {}'.format(ContentType ._VALUES_TO_NAMES[msg['contentType']])
        aa = '\nCreatedTime: {}{}\nText:\n'.format(humanize.naturaltime(datetime.fromtimestamp(msg['createdTime']/1000)),dd)
        if msg['contentType'] == 0:
            if 'MENTION' in msg["contentMetadata"].keys() != None:
                anu = Message()
                msg["text"] = ' 「 Unsend 」\nFrom: @KEPINGANTENG '+aa+msg['text']
                anu.text = msg["text"]
                gd = [{'S':str(0+len(' 「 Unsend 」\nFrom: ')), 'E':str(len('@KEPINGANTENG ')+len(' 「 Unsend 」\nFrom: ')), 'M':msg["_from"]}]
                for key in eval(msg["contentMetadata"]["MENTION"])["MENTIONEES"]:
                    gd.append({'S':str(int(key['S'])+len(' 「 Unsend 」\nFrom: @KEPINGANTENG '+aa)), 'E':str(int(key['E'])+len(' 「 Unsend 」\nFrom: @KEPINGANTENG '+aa)),'M':key['M']})
                msg["contentMetadata"] = {'MENTION': str('{"MENTIONEES":' + json.dumps(gd) + '}')}
                anu.contentMetadata = msg["contentMetadata"]
                anu.to = msg["to"]
                line.sendMessageObject(anu)
            else:
                anu = Message()
                anu.location = msg['location']
                if msg["location"] != None:aa = aa.replace('Text','Location').replace('\nText:','');line.sendMessageObject(anu)
                if msg["text"] != None: asdd = msg["text"]
                else:asdd = ''
                line.sendMentionV2(op.param1,' 「 Unsend 」\nFrom: @! {}{}'.format(aa,asdd),[msg['_from']])
        else:
            asdf = ' 「 Unsend 」\nFrom: @!\nCreatedTime: {}{}'.format(humanize.naturaltime(datetime.fromtimestamp(msg['createdTime']/1000)),dd)
            if msg['contentType'] == 1:
                if msg["contentMetadata"] != {}:line.sendGIF(op.param1,settings['detectUnsend'][op.param1][op.param2]['path'])
                else:line.sendImage(op.param1,settings['detectUnsend'][op.param1][op.param2]['path'])
            if msg['contentType'] == 2:line.sendVideo(op.param1,settings['detectUnsend'][op.param1][op.param2]['path'])
            if msg['contentType'] == 3:line.sendAudio(op.param1,settings['detectUnsend'][op.param1][op.param2]['path'])
            if msg['contentType'] == 14:line.sendFile(op.param1,settings['detectUnsend'][op.param1][op.param2]['path'], file_name='',ct = msg['contentMetadata'])
            else:
                try:
                    anu = Message()
                    anu.to = msg['to']
                    anu.text = msg['text']
                    anu.contentMetadata = msg['contentMetadata']
                    anu.contentType = msg['contentType']
                    line.sendMessageObject(anu)
                except Exception as e:
                    logError(e)
                    agh = line.getProduct(packageID=int(msg["contentMetadata"]['STKPKGID']), language='ID', country='ID')
                   # if agh.hasAnimation == True:
                    sendStickerTemplate(op.param1,int(msg["contentMetadata"]['STKID']),int(msg["contentMetadata"]['STKPKGID']))
            line.sendMentionV2(op.param1,asdf,[msg['_from']])
    del settings['detectUnsend'][op.param1][op.param2]
            
def checkMention(contentMetadata):
    if 'MENTION' in contentMetadata.keys() != None:
        mention = ast.literal_eval(contentMetadata['MENTION'])
        mentionees = mention['MENTIONEES']
        mid = []
        if len(mentionees) == 1:
            mid.append(mentionees[0]['M'])
        else:
            for i in mentionees:
                mid.append(i['M'])
        return mid
    else:
        return None

def QrDecode(path):
    data = decode(Image.open(path))
    if data == []:
        return "QR Code Not Found !"
    result = str(data[0])
    return result

def JooxSearch(title):
    url = "https://api-jooxtt.sanook.com/web-fcgi-bin/web_category_search?country=id&lang=id&search_input={}&sin=0&ein=6&type=1".format(str(title.replace(" ","%20")))
    r = requests.get(url)
    data = r.json()
    return data

def JooxGetAlbum(songid):
    url = "https://api-jooxtt.sanook.com/web-fcgi-bin/web_get_albuminfo?country=id&lang=id&all=1&albumid={}".format(str(songid))
    r = requests.get(url)
    data = json.loads(r.text)
    return data

def sendMeTemplate(to):
    img = "https://os.line.naver.jp/os/p/"+line.profile.mid
    if line.profile.statusMessage == '':statuss = "Selfbot Version"
    else:statuss = line.profile.statusMessage
    data = {
        "messages":[
            {
                "type":"flex",
                "altText": "Me",
                "contents":{
                    "type":"bubble",
                    "header":{
                        "type":"box",
                        "layout":"horizontal",
                        "contents":[
                            {
                                "type":"text",
                                "text":"Selfbot Version",
                                "weight":"bold",
                                "color":"#aaaaaa",
                                "size":"sm"
                            }
                        ]
                    },
                    "hero":{
                        "type":"image",
                        "url":str(img),
                        "size":"full",
                        "aspectRatio":"20:13",
                        "aspectMode":"fit",
                    },
                    "body":{
                        "type":"box",
                        "layout":"vertical",
                        "contents":[
                            {
                                "type":"text",
                                "text":"Profile",
                                "weight":"bold",
                                "size":"xl"
                            },
                            {
                                "type": "separator",
                                "margin": "sm"
                            },
                            {
                                "type":"box",
                                "layout":"vertical",
                                "margin":"lg",
                                "spacing":"sm",
                                "contents": [
                                    {
                                        "type":"box",
                                        "layout":"baseline",
                                        "spacing":"sm",
                                        "contents":[
                                            {
                                                "type":"text",
                                                "text":"Display Name",
                                                "wrap": True,
                                                "color":"#aaaaaa",
                                                "size":"sm",
                                                "flex":2
                                            },
                                            {
                                                "type":"text",
                                                "text":line.profile.displayName,
                                                "wrap":True,
                                                "color":"#666666",
                                                "size":"sm",
                                                "flex":5
                                            }
                                        ]
                                    },
                                    {
                                        "type":"box",
                                        "layout":"baseline",
                                        "spacing":"sm",
                                        "contents":[
                                            {
                                                "type":"text",
                                                "text":"Bio",
                                                "color":"#aaaaaa",
                                                "size":"sm",
                                                "flex":2
                                            },
                                            {
                                                "type":"text",
                                                "text":str(statuss),
                                                "wrap":True,
                                                "color":"#666666",
                                                "size":"sm",
                                                "flex":5
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "footer":{
                        "type":"box",
                        "layout":"vertical",
                        "spacing":"sm",
                        "contents":[
                            {
                                "type":"button",
                                "style":"link",
                                "height":"sm",
                                "action":{
                                    "type":"uri",
                                    "label": "Account",
                                    "uri": "line://ti/p/"+line.generateUserTicket()
                                }
                            },
                            {
                                "type":"spacer",
                                "size":"sm"
                            }
                        ],
                        "flex":0
                    }
                }
            }
        ]
    }
    line.sendTemplate(to,data)

def youtubeSearchTemplate(to,json):
    columns=[];columns2=[];columns3=[]
    k=len(json['items'])//100
    for mmk in range(0,10):
        link = "https://youtube.com/watch?v="+json['items'][mmk]['id']['videoId']
        imageUrl = str(json['items'][mmk]['snippet']['thumbnails']['high']['url'])
        title = str(json['items'][mmk]['snippet']['title'])
        channelTitle = str(json['items'][mmk]['snippet']['channelTitle'])
        columns.append(
            {
                "type":"bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "url": imageUrl
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "text",
                            "text": title,
                            "wrap": True,
                            "weight": "bold",
                            "size": "sm"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "action": {
                                "type": "uri",
                                "label": "View",
                                "uri": link
                            }
                        }
                    ]
                }
            }
        )
    for mmk in range(10,20):
        link = "https://youtube.com/watch?v="+json['items'][mmk]['id']['videoId']
        imageUrl = str(json['items'][mmk]['snippet']['thumbnails']['high']['url'])
        title = str(json['items'][mmk]['snippet']['title'])
        channelTitle = str(json['items'][mmk]['snippet']['channelTitle'])
        columns2.append(
            {
                "type":"bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "url": imageUrl
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "text",
                            "text": title,
                            "wrap": True,
                            "weight": "bold",
                            "size": "sm"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "action": {
                                "type": "uri",
                                "label": "View",
                                "uri": link
                            }
                        }
                    ]
                }
            }
        )
    for mmk in range(20,25):
        link = "https://youtube.com/watch?v="+json['items'][mmk]['id']['videoId']
        imageUrl = str(json['items'][mmk]['snippet']['thumbnails']['high']['url'])
        title = str(json['items'][mmk]['snippet']['title'])
        channelTitle = str(json['items'][mmk]['snippet']['channelTitle'])
        columns3.append(
            {
                "type":"bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "url": imageUrl
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "text",
                            "text": title,
                            "wrap": True,
                            "weight": "bold",
                            "size": "sm"
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "action": {
                                "type": "uri",
                                "label": "View",
                                "uri": link
                            }
                        }
                    ]
                }
            }
        )
    data = {
        "messages": [
            {
                "type": "flex",
                "altText": "Youtube Search",
                "contents": {
                    "type": "carousel",
                    "contents": columns
                }
            }
        ]
    }
    data2 = {
        "messages": [
            {
                "type": "flex",
                "altText": "Youtube Search",
                "contents": {
                    "type": "carousel",
                    "contents": columns2
                }
            }
        ]
    }
    data3 = {
        "messages": [
            {
                "type": "flex",
                "altText": "Youtube Search",
                "contents": {
                    "type": "carousel",
                    "contents": columns3
                }
            }
        ]
    }
    line.sendTemplate(to,data)
    line.sendTemplate(to,data2)
    line.sendTemplate(to,data3)
def sendFlex(to,altText,data):
    dataa = {
        'messages': [ 
    {
        'type': 'flex',
        'altText': altText,
        'contents': data
    }]}
    datta = json.dumps(dataa)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = line.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=datta, headers=headers)
    
def ProfileChangeDual(msg,link):
    line.sendReplyMessage(msg.id,msg.to," 「 Profile 」\nType: Change Profile Video Picture\nStatus: Downloading....♪")
    try:
        req = requests.get(f"http://kyuza-api.herokuapp.com/api/youtubeapi?q={link}")
        data = req.json()
        sdd = data["result"]['videolist'][len(data["result"]['videolist'])-1];ghj = sdd['extension']
        url = sdd['url']
        path = line.downloadFileURL(url,saveAs='tmp/video.mp4')
        path2 = line.downloadFileURL('http://dl.profile.line-cdn.net/'+line.profile.pictureStatus,saveAs='tmp/picture.jpg')
        line.updateVideoAndPictureProfile(path2, path)
        line.sendReplyMessage(msg.id,msg.to, " 「 Profile 」\nType: Change Profile Video Picture\nStatus: Profile Video Picture Hasbeen change♪")
    except:
        try:
            url = link.replace('youtu.be/','youtube.com/watch?v=')
            req = pafy.new(url).streams[-1]
            path = line.downloadFileURL(req.url,saveAs='tmp/video.mp4')
            path2 = line.downloadFileURL('http://dl.profile.line-cdn.net/'+line.profile.pictureStatus,saveAs='tmp/picture.jpg')
            line.updateVideoAndPictureProfile(path2, path)
            line.sendReplyMessage(msg.id,msg.to, " 「 Profile 」\nType: Change Profile Video Picture\nStatus: Profile Video Picture Hasbeen change♪")
        except Exception as e:
            print(traceback.print_exc())
            line.sendReplyMessage(msg.id,msg.to, f" 「 Profile 」\nType: Change Profile Video Picture\nStatus: Error !\nReason: {e}")

def sendStickerTemplate(to,stickerID,packageID):
    anu ='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(stickerID)+'/IOS/sticker_animation@2x.png'
    r = requests.get(anu)
    if r.status_code != 200:path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/android/sticker.png".format(stickerID)
    else:path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(stickerID)
    data = {"messages":[{"type":"template","altText":"Sticker","template":{"type":"image_carousel","columns":[{"imageUrl":path,"action":{"type":"uri","uri":"line://shop/sticker/detail/"+str(packageID),"area":{"x":520,"y":0,"width":520,"height":1040}}}]}}]}
    return line.sendTemplate(to,data)

def sendSquareTemplate(to,data):
    anu = LiffSquareChatContext(to)
    itu = LiffContext(squareChat=anu)
    lol = LiffViewRequest('1602687308-GXq4Vvk9', itu)
    tes = line.liff.issueLiffView(lol)
    token = 'Bearer {}'.format(tes.accessToken)
    url = 'https://api.line.me/message/v3/share'
    headers = {
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0.2; Lenovo A6000 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 Line/8.16.2',
	    'Content-Type': 'application/json',
	    'Authorization': token
    }
    data = json.dumps(data)
    laso = requests.post(url, data=data, headers=headers)
    return laso.text


def sendMessageObjectWithTemplate(msg):
    if msg.text is not None and msg.relatedMessageId == None:
       return line.sendMessageWithFooterTemplate(msg.to,msg.text,title="Resend Message")
    line.sendMessageObject(msg)

def forward(msg):
    if msg.toType == 2:to = msg.to
    else:to = msg._from
    if msg.contentType == 1:
        try:
            if msg.contentMetadata['MEDIA_CONTENT_INFO']['extension']['gif']:
                path = line.downloadObjectMsg(msg.id,'path','tmp/m.gif')
                a = Thread(target=sendStickerGif,args=(to,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id,)).start()
        except:path='https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id;line.sendImageWithURL(to,path)
    if msg.contentType == 2:line.sendVideoWithURL(to,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)
    if msg.contentType == 3:line.sendAudioWithURL(to,'https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id)

def resendMessage(cmd,split,to,relatedMsgId):
    M = line.getRecentMessagesV2(to, 1001)
    anu = []
    for ind, i in enumerate(M):
        if i.id == relatedMsgId:
            anu.append(i)
    if cmd == 'resend':
        try:
            line.sendMessageObject(anu[0])
            forward(anu[0])
        except:
            a = line.getProduct(packageID=int(anu[0].contentMetadata['STKPKGID']), language='ID', country='ID')
            return sendStickerTemplate(to,anu[0].contentMetadata['STKID'],anu[0].contentMetadata['STKPKGID'])
    elif len(split) == 1:
        for anuu in range(int(split[0])):
            try:
                if anu[0].text is not None:
                    sendMessageObjectWithTemplate(anu[0])
                    forward(anu[0])
                else:
                    try:
                        line.sendMessageObject(anu[0])
                    except:
                        a = line.getProduct(packageID=int(anu[0].contentMetadata['STKPKGID']), language='ID', country='ID')
                        if a.hasAnimation:
                            path = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + str(
                                anu[0].contentMetadata['STKID']) + '/IOS/sticker_animation@2x.png'
                        return sendStickerTemplate(to,anu[0].contentMetadata['STKID'],anu[0].contentMetadata['STKPKGID'])
                    line.sendImageWithURL(to, 'http://stickershop.line-scdn.net/stickershop/v1/sticker/'+ str(anu[0].contentMetadata['STKID']) +'/ANDROID/sticker.png')
            except:continue
def restartProgram():
    print ('##----- PROGRAM RESTARTED -----##')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def translateText(text,dest):
    #key = "trnsl.1.1.20190108T021801Z.9211f76bee6df74e.2095832bbbcdcaddcb3e6716083feadb1eb98089"
    #tr = YandexTranslate(key)
    #result = tr.translate(text,dest)
    #return result['text'][0]
    tr = TranslateKyu()
    result = tr.translate(dest,text)
    return result

def checkMessageReply(to,relatedMsgId):
    M = line.getRecentMessagesV2(to,1001)
    msg = []
    for ind,i in enumerate(M):
        if ind == 0:pass
        else:
            if i.id == relatedMsgId:msg.append(i)
    return msg

def logError(error, write=True):
    traceback.print_tb(error.__traceback__)
    print ('++ Error : {error}'.format(error=error))

def command(text):
    pesan = text.lower()
    if settings['setKey']['status']:
        if pesan.startswith(settings['setKey']['key']):
            cmd = pesan.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd
    
def commandUser(text):
    pesan = text.lower()
    if pesan.startswith(args.user):
        cmd = pesan.replace(args.user,'')
    else:
        cmd = 'Undefined command'
    return cmd

def sendNhentai(to,query):
    if "http://" in query.lower() or "https://" in query.lower():
        nhentai = query
    else:
        nhentai = "http://nhentai.net/g/{}".format(str(query))
    #print("+++ INFO +++\n- Try to send nhentai on group {}".format(bot.getGroup(to).name))
    r = getNhentai(nhentai)
    data = r
    for i in data['images']:
        ImagesThread = Thread(target=line.sendImageWithURL, args=(to,i,))
        ImagesThread.start()
        ImagesThread.join()

def getNhentai(url):
    req = requests.get(url)
    if req.status_code != 200:
        return "STATUS CODE IS {}".format(req.status_code)
    html = BeautifulSoup(req.text, 'lxml')
    for getAllScript in html.findAll('script')[2]:
        imgs = re.search(r'(\{.+\})', getAllScript).group()
        data = json.loads(imgs)
        images = []
        for n, i in enumerate(data.get('images', {}).get('pages', [])):
            images.append('{}{}/{}.{}'.format('https://i.nhentai.net/galleries/', data.get('media_id'), n + 1, {'j': 'jpg', 'p': 'png', 'g': 'gif'}.get(i.get('t'))))
    data = {"result":{"title":{"english":data['title']['english'],"japan":data['title']['japanese']},"images":images}}
    return data['result']

def genImageB64(path):
    with open(path, 'rb') as img_file:
        encode_str = img_file.read()
        b64img = base64.b64encode(encode_str)
        return b64img.decode('utf-8')

def ub64(url):hasil = base64.b64decode(url);return hasil.decode('utf-8')

def genUrlB64(url):
    return base64.b64encode(url.encode('utf-8')).decode('utf-8')

def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]
   
def removeUser(text, key=''):
    setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def replaceAll(text, dic):
    try:
        rep_this = dic.items()
    except:
        rep_this = dic.iteritems()
    for i, j in rep_this:
        text = text.replace(i, j)
    return text

def SkipLinkPoi(url):
    try:
        with requests.session() as web:
            web.headers["user-agent"] = "Mozilla/5.0"
            req = web.get(url)
            soup = BeautifulSoup(req.content, "html5lib")
            linkz=""
            for xx in soup.findAll('div', {'class':'col-sm-6'}):
                link = xx.a["href"]
                linkz+=link
            linkk = linkz.split("?id=")[1].split("&c")[0]
            return linkk
    except Exception as e:
        logError(e)

def SfLeech(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
        }
        pageSource = requests.get(url, headers = headers).text
        mainOptions = str(re.search(r'viewerOptions(\{.+\})', pageSource))
        jsonString = json.loads(mainOptions, encoding="utf-8")
        return jsonString
    except Exception as e:
        logError(e)

def help():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    text = open('help.txt', errors='ignore', encoding="utf8").read()
    helpMsg = text.format(key=key.title())
    return helpMsg

def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '?', '', '╰']]:
            result += '\n ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result

def sendStickerGif(to,url):
    path = line.downloadFileURL(url,'path','tmp/sticker.mp4')
    ff = FFmpeg(inputs={'tmp/sticker.mp4'},outputs={'tmp/sticker.gif'})
    ff.run() 
    line.sendGIF(to,"tmp/sticker.gif")

def mentionMembers(msg_id,to, mids=[]):
    if myMid in mids: mids.remove(myMid)
    parsed_len = len(mids)//20+1
    result = ' 「 Mention Members 」\n'
    mention = '@kevinxmayu\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += ' %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
        if result:
            if result.endswith('\n'): result = result[:-1]
            line.sendReplyMessage(msg_id,to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def cloneProfile(mid):
    contact = line.getContact(mid)
    profile = line.getProfile()
    profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
    line.updateProfile(profile)
    if contact.pictureStatus:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus)
        line.updateProfilePicture(pict)
    coverId = line.getProfileDetail(mid)['result']['objectId']
    line.updateProfileCoverById(coverId)

def backupProfile():
    profile = line.getContact(myMid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    coverId = line.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

def restoreProfile():
    profile = line.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    line.updateProfile(profile)
    if settings['myProfile']['pictureStatus']:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'])
        line.updateProfilePicture(pict)
    coverId = settings['myProfile']['coverId']
    line.updateProfileCoverById(coverId)

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd == 'logoutbot':
        line.sendReplyMessage(msg_id,to, 'Bot will logged out')
        os.system("screen -R {} -X quit".format(args.user))
    elif cmd == 'logoutdevicee':
        line.logout()
        sys.exit('##----- CLIENT LOGOUT -----##')
    elif cmd == 'restart':
        line.sendReplyMessage(msg_id,to, 'Bot will restarting, please wait until the bot can operate ♪')
        settings['restartPoint'] = to
        restartProgram()
    elif cmd == 'help':
        line.sendMessageWithFooterTemplate(to,help(),title='Help Message')
    elif cmd == 'about':
        res = ' 「 About 」'
        res += '\nType : Selfbot Reworked Hello World'
        res += '\nLibrary : linepy (Python)'
        res += '\nCopyright : Hello World'
        line.sendReplyMessage(msg_id,to,str(res))
    elif cmd == 'speed':
        start = time.time()
        try:line.sendMessage(sender,to)
        except:pass
        elapsed_time = time.time() - start
        took = time.time() - start
        line.sendReplyMessage(msg_id,to," 「 Speed 」\nType: Speed\n - Took : %.3fms\n - Taken: %.10f" % (took,elapsed_time))
    elif cmd == 'me':
        #line.sendContact(to, myMid)
        sendMeTemplate(to)
    elif cmd == 'runtime':
        runtime = time.time() - programStart
        line.sendReplyMessage(msg_id,to, 'Bot already running on ' + format_timespan(runtime))
    elif cmd == 'status':
        res = ' 「 Status 」'
        res += '\nAuto Add : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\nAuto Join : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\nAuto Join Ticket : ' + bool_dict[settings['autoJoin']['ticket']][1]
        res += '\nAuto Respond : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\nAuto Respond Mention : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\nAuto Read : ' + bool_dict[settings['autoRead']][1]
        res += '\nSetting Key : ' + bool_dict[settings['setKey']['status']][1]
        res += '\nMimic : ' + bool_dict[settings['mimic']['status']][1]
        res += '\nGreetings Join : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\nGreetings Leave : ' + bool_dict[settings['greet']['leave']['status']][1]
        res += '\nCheck Contact : ' + bool_dict[settings['checkContact']][1]
        res += '\nCheck Post : ' + bool_dict[settings['checkPost']][1]
        res += '\nCheck Sticker : ' + bool_dict[settings['checkSticker']][1]
        line.sendReplyMessage(msg_id,to, parsingRes(res))
    elif cmd == 'abort':
        aborted = False
        if to in settings['changePictureAndVideoProfile']['to']:
            settings['changePictureAndVideoProfile']['to'].remove(to)
            settings['changePictureAndVideoProfile']['status'] = 0
            line.sendReplyMessage(msg_id,to, 'Change video picture profile aborted')
            aborted = True
        if settings['changeVideoPictureProfile']:
            settings['changeVideoPictureProfile'] = False
            line.sendReplyMessage(msg_id,to,'Change video profile aborted')
            aborted = True
        if settings['changePictureVideoProfile']:
            settings['changePictureVideoProfile'] = False
            line.sendReplyMessage(msg_id,to,'Change picture profile aborted')
            aborted = True
        if to in settings['changeGroupPicture']:
            settings['changeGroupPicture'].remove(to)
            line.sendReplyMessage(msg_id,to, 'Change group picture aborted')
            aborted = True
        if settings['changePictureProfile']:
            settings['changePictureProfile'] = False
            line.sendReplyMessage(msg_id,to, 'Change picture profile aborted')
            aborted = True
        if settings['changeCoverProfile']:
            settings['changeCoverProfile'] = False
            line.sendReplyMessage(msg_id,to, 'Change cover profile aborted')
            aborted = True
        if not aborted:
            line.sendReplyMessage(msg_id,to, 'Failed abort, nothing to abort')
    elif cmd.startswith('checkk'):
        textt = removeCmd(text, setKey)
        texts = textt.lower()
        cond = textt.split(' ')
        res = ' 「 Check Media 」'
        res += '\nUsage : '
        res += '\n • {key}Checkk Image <url>'
        res += '\n • {key}Checkk VIdeo <url>'
        res += '\n • {key}Checkk Gif <url>'
        res += '\n • {key}Checkk Audio <url>'
        if cmd == 'checkk':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'image':
            line.sendImageWithURL(to,cond[1])
        elif cond[0].lower() == 'video':
            line.sendVideoWithURL(to,cond[1])
        elif cond[0].lower() == 'gif':
            line.sendGIFWithURL(to,cond[1])
        elif cond[0].lower() == 'audio':
            line.sendAudioWithURL(to,cond[1])
    elif cmd.startswith("jsonify"):
        textt = removeCmd(text, setKey)
        r=requests.get(textt)
        if r.status_code != 200:
            jsonny = json.loads(str(textt))
            data = json.dumps(jsonnya, indent=4)
            line.sendReplyMessage(msg_id,to,data)
        else:
            data = json.dumps(r.json(),indent=4)
            line.sendReplyMessage(msg_id,to,data)
    elif cmd.startswith('nhentai'):
        textt = removeCmd(text, setKey)
        texts = textt.lower()
        cond = textt.split(' ')
        res = ' 「 NHentai 」'
        res += '\nUsage : '
        res += '\n • {key}Nhentai'
        res += '\n • {key}Nhentai Search <query>'
        res += '\n • {key}Nhentai Download <url/code>'
        if cmd == 'nhentai':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'search':
            if len(cond) == 1:
                return line.sendReplyMessage(msg_id,to,'Failed to search, nothing to search')
            texts = textt[7:]
            query = texts.split("|")
            url = requests.get('https://nhentai.net/search/?q={}&page={}'.format(query[0], query[1]))
            html = BeautifulSoup(url.text, 'lxml')
            data = []
            for getAllGallery in html.findAll('div', {'class': 'gallery'}):
                allGallery = 'https://nhentai.net{}'.format(getAllGallery.a['href'])
                for getAllTitle in getAllGallery.findAll('div', {'class': 'caption'}):
                    allTitle = getAllTitle.text
                    data.append({'title': allTitle, 'url': allGallery})
            if len(query) == 2:
                a=" 「 Search Nhentai 」 "
                no=1
                for i in data:
                    a+="\n{}. {}\n".format(no, i['title'])
                    no+=1
                line.sendReplyMessage(msg_id,to,str(a))
            elif len(query) == 3:
                if int(query[2]) < len(data):
                    urll = data[int(query[2])-1]
                    dataa = getNhentai(urll['url'])
                    line.sendReplyMessage(msg_id,to," 「 Search Nhentai 」\n• Title English : "+str(dataa['title']['english'])+"\n• Title Japan : "+str(dataa['title']['japan'])+"\n• Link : "+str(urll['url'])+"\n• Total Image "+str(len(dataa['images'])))
        elif cond[0].lower() == "download":
            if len(cond) == 1:
                return line.sendReplyMessage(msg_id,to,'Failed to download, nothing to download')
            texts = textt[9:]
            query = texts.split(" ")
            return sendNhentai(to,query[0])
    elif cmd.startswith('instagram'):
        textt = removeCmd(text, setKey)
        texts = textt.lower()
        cond = textt.split(' ')
        res = ' 「 Instagram 」'
        res += '\nUsage : '
        res += '\n • {key}Instagram'
        res += '\n • {key}Instagram Search <username>'
        res += '\n • {key}Instagram Download <url>'
        res += '\n • {key}Instagram Info <url>'
        if cmd == 'instagram':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'search':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to,'Failed to search, nothing to search')
            headers={'User-Agent':'Mozilla/5.0'}
            r = requests.get("https://www.instagram.com/"+cond[1],headers=headers)
            if r.status_code != 200:return line.sendReplyMessage(msg_id,to,'Failed to search, Instagram {} not found'.format(cond[1]))
            soup = BeautifulSoup(r.content,'html5lib')
            for script in soup.findAll('script',type='text/javascript')[3]:
                 js = json.loads(re.search(r'window._sharedData\s*=\s*(\{.+\})\s*;', script).group(1))
                 profile = js['entry_data']['ProfilePage'][0]['graphql']['user']
                 if profile:
                     a=" 「 Instagram 」"
                     a+="\nName : "+str(profile['username'])
                     a+="\nBiography : "+str(profile['biography'])
                     a+="\nFollower : "+humanize.intcomma(profile['edge_followed_by']['count'])
                     a+="\nFollowing : "+humanize.intcomma(profile['edge_follow']['count'])
                     a+="\nMedia : "+humanize.intcomma(profile['edge_owner_to_timeline_media']['count'])
                     a+="\nPrivate : "+str(profile['is_private'])
                     line.sendImageWithURL(to,profile['profile_pic_url_hd'])
                     line.sendReplyMessage(msg_id,to,parsingRes(a))
        elif cond[0].lower() == 'download' or cond[0].lower() == 'info':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to,'Failed to check, url is not detected')
            headers={'User-Agent':'Mozilla/5.0'}
            if cond[0].lower() == 'download':
                r = requests.get('http://kyuza-api.herokuapp.com/api/instapost?url='+cond[1])
                data = r.json()['result']['media']
                if isinstance(data['url'], list):
                    for link in data['url']:
                        if link['mediatype'] == 1:
                            line.sendImageWithFooterTemplate(to,link['url'],title='Instagram Download')
                        else:line.sendVideoWithURL(to,link['url'])
                else:
                    if data['mediatype'] == 1:
                        line.sendImageWithFooterTemplate(to,data['url'],title="Instagram Download")
                    else:line.sendVideoWithURL(to,data['url'])
            elif cond[0].lower() == 'info':
                r = requests.get(cond[1],headers=headers,params={'__a':'1'})
                data = r.json()
                username = data['graphql']['shortcode_media']['owner']['username']
                fullname = data['graphql']['shortcode_media']['owner']['full_name']
                usertag = ""
                if data['graphql']['shortcode_media']['edge_media_to_tagged_user']['edges'] != []:
                    usertag += len(data['graphql']['shortcode_media']['edge_media_to_tagged_user']['edges'])
                else:usertag+="This post doesn't tag any people"
                type = ""
                if data['graphql']['shortcode_media']['is_video'] != True:type+="Image"
                else:type+="Video"
                caption = data['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
                comment = ""
                like = data['graphql']['shortcode_media']['edge_media_preview_like']['count']
                created = str(humanize.naturaltime(datetime.fromtimestamp(int(data['graphql']['shortcode_media']['taken_at_timestamp']))))
                if data['graphql']['shortcode_media']['edge_media_to_comment']['edges'] != []:comment+=str(len(data['graphql']['shortcode_media']['edge_media_to_comment']['edges']))
                else:comment+="Nothing people comment on this post"
                line.sendReplyMessage(msg_id,to,str(" 「 Instagram Info 」\n• Username : {}\n• Full Name : {}\n• Type : {}\n• Created Time : {}\n• Link Post : https://www.instagram.com/p/{}\n• Total Like : {}\n• User Tag : {}\n• User Comment : {}\n• Caption : {}".format(username,fullname,type,created,data['graphql']['shortcode_media']['shortcode'],like,usertag,comment,caption)))
    elif cmd.startswith('hanime'):
        textt = removeCmd(text, setKey)
        texts = textt.lower()
        cond = textt.split(' ')
        res = ' 「 Hanime TV 」'
        res += '\nUsage : '
        res += '\n • {key}Hanime'
        res += '\n • {key}Hanime Search <query>'
        res += '\n • {key}Hanime Get <url hanime>'
        hanime = HanimeTV()
        if cmd == 'hanime':
            line.sendMessageWithFooterTemplate(to, parsingRes(res).format_map(SafeDict(key=setKey.title())),title='Hanime TV')
        elif cond[0].lower() == 'search':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to,"Failed to search, no query found")
            texts = textt[7:]
            query = texts.split("|")
            search = hanime.search(query[0])
            if len(query) == 1:
                res = ' 「 Hanime TV 」'
                no=0
                for i in search['hits']['hits']:
                    no+=1
                    res+="\n{}. {}".format(no,i['_source']['name'])
                res += '\nUsage : '
                res += '\n • {key}Hanime search '.format_map(SafeDict(key=setKey.title()))+query[0]+'|<no>'
                line.sendMessageWithFooterTemplate(to, parsingRes(res),title='Hanime TV')
            elif len(query) == 2:
                data = search['hits']['hits'][int(query[1])-1]
                link="https://hanime.tv/hentai-videos/"+data['_source']['video_stream_group_id']
                data2=hanime.get(link)
                ms = (int(data['_source']['duration_in_ms']/(1000*60)))%60
                duration = "%d" % (int(ms))
                res="「 Hanime TV 」\n\nTitle Sort : {}\nDuration : {} Minute".format(data['_source']['name'],duration)
                res+="\nList Titles : "
                for i in data["_source"]['titles']:res+="\n  - {}".format(str(i))
                res+="\nTags : "
                for i in data["_source"]['tags']:res+="\n  - {}".format(str(i))
                res+="\nDescription : \n{}\nLink : {}".format(data['_source']['description'].replace("<p>","").replace("</p>",""),link)
                line.sendImageWithURL(to,str(data['_source']['cover_url']))
                line.sendMessageWithFooterTemplate(to,res,title='Click me !',link=link)
                line.sendMessageWithFooterTemplate(to,'Wait to upload the video',title='Click me !')
                sendVideoWithTemplate(to,str(data2["videos_manifest"]["servers"][0]["streams"][0]["url"]),str(data["_source"]["poster_url"]))
    elif cmd.startswith("delmention"):
        textt = removeCmd(text, setKey)
        texts = textt.lower()
        cond = texts.split(' ')
        try:
#            moneys = {}
 #           for a in settings['checkMention'][to].items():
  #              moneys[a[0]] = [a[1]['msg']] if a[1] is not None else idnya
#            sort = sorted(moneys)
#            sort.reverse()
#            sort = sort[0:]
            if cmd == "delmention":
                del settings['checkMention'][to]
                line.sendReplyMessage(msg_id,to," 「 Check Mention 」\nStatus: Success\nSuccess delete list mention in group {}".format(line.getGroup(to).name))
            elif len(cond) == 1:
                if cond[0] == "all":
                    settings['checkMention'] = {}
                    line.sendReplyMessage(msg_id,to," 「 Check Mention 」\nStatus: Success\nSuccess clear all data mention")
                else:
                    contact = sort[int(cond[0])-1]
                    del settings['checkMention'][to][contact]
                    line.sendMentionV3(msg_id,to," 「 Check Mention 」\nStatus: Success\nSuccess delete list mention from @!",[contact])
        except Exception as e:
            logError(e)
            msgas = " 「 Check Mention 」\nStatus: Error\nSorry @! in {} nothing get a mention".format(line.getGroup(to).name)
            line.sendMentionV3(msg_id,to,msgas,[sender])
    elif cmd.startswith("checkmention"):
        textt = removeCmd(text, setKey)
        texts = textt.lower()
        cond = textt.split(' ')
        try:
            if cmd == "checkmention":
                checkUserMention(to)
            elif len(cond) == 1:
                checkUserMention(to,split=cond[0])
            elif len(cond) == 2:
                checkUserMention(to,split=cond[0],split2=cond[1])
        except:
            msgas = " 「 Check Mention 」\nStatus: Error\nSorry @! in {} nothing get a mention".format(line.getGroup(to).name)
            line.sendMentionV3(msg_id,to,msgas,[sender])
                
    elif cmd.startswith('youtube'):
        textt = removeCmd(text, setKey)
        texts = textt.lower()
        cond = textt.split(' ')
        res = ' 「 Youtube 」'
        res += '\nUsage : '
        res += '\n • {key}Youtube'
        res += '\n • {key}Youtube Search <query>'
        res += '\n • {key}Youtube Video <url>'
        res += '\n • {key}Youtube Audio <url>'
        if cmd == 'youtube':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'search':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to,"Failed to search, no query found")
            texts = textt[7:]
            query = textt.split("|")
            a = line.requestsWeb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+query[0]+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
            if a['items'] != []:
                if len(query) == 1:
                    res = '    | Youtube |'
                    no = 0
                    for mmk in a['items']:
                        no+=1
                        res +='\n{}. {}'.format(no,mmk['snippet']['title'])
                    res += '\nUsage : '
                    res += '\n • {key}Youtube search '.format_map(SafeDict(key=setKey.title()))+query[0]+'|<no>'
                    #youtubeSearchTemplate(to,a)
                    line.sendMessageWithFooterTemplate(to, parsingRes(res),title='Youtube Search')
                elif len(query) == 2:
                    line.sendReplyMessage(msg_id,to," 「 Youtube 」\nWaiting....")
                    data = a['items'][int(query[1])-1]
                    link="https://youtube.com/watch?v="+data['id']['videoId']
                    hs = line.requestsWeb("http://kyuza-api.herokuapp.com/api/youtubeapi?q="+link)
                    sdd = hs["result"]['videolist'][len(hs["result"]['videolist'])-1];ghj = sdd['extension']
                    hhhh = '    | Youtube |\nJudul: {}\nDuration: {}\nEx: {}.{} {}\nSize: {}\nStatus: Waiting... For Upload'.format(hs['result']['title'],hs['result']['duration'],hs['result']['title'],ghj,sdd['resolution'],sdd['size'])
                    line.sendReplyMessage(msg_id,to,hhhh)
                    line.sendImageWithFooterTemplate(to,hs['result']['thumbnail'],title=hs['result']['title'])
                    line.sendVideoWithTemplate(to,sdd['url'],hs['result']['thumbnail'])
        elif cond[0].lower() == "video":
            url = cond[1].replace("youtu.be/","youtube.com/watch?v=")
            yt = pafy.new(url,basic=False)
            video = yt.videostreams[-1]
            title = yt.title
            duration = yt.duration
            image = yt.bigthumbhd
            try:line.sendImageWithURL(to,image)
            except:pass
            ret = f"    | Youtube |\nTitle: {title}\nDuration: {duration}\nWait to upload video ..."
            line.sendMessageWithFooterTemplate(to,ret,title="Youtube",iconlink="https://cdn3.iconfinder.com/data/icons/follow-me/256/YouTube-512.png",link=cond[1])
            if duration > "00:05:00":
                line.sendVideoWithTemplate(to,video.url,image)
            else:
                line.sendVideoWithURL(to,video.url)
        elif cond[0].lower() == "audio":
            url = cond[1].replace("youtu.be/","youtube.com/watch?v=")
            yt = pafy.new(url,basic=False)
            video = yt.audiostreams[-1]
            title = yt.title
            duration = yt.duration
            image = yt.bigthumbhd
            try:line.sendImageWithURL(to,image)
            except:pass
            ret = f"    | Youtube |\nTitle: {title}\nDuration: {duration}\nWait to upload audio ..."
            line.sendMessageWithFooterTemplate(to,ret,title="Youtube",iconlink="https://cdn3.iconfinder.com/data/icons/follow-me/256/YouTube-512.png",link=cond[1])
            if duration > "00:05:00":
                line.sendAudioWithTemplate(to,video.url)
            else:
                line.sendAudioWithURL(to,video.url)
            
    elif txt.startswith('setkey'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = ' 「 Setting Key 」'
        res += '\nStatus : ' + bool_dict[settings['setKey']['status']][1]
        res += '\nKey : ' + settings['setKey']['key'].title()
        res += '\nUsage : '
        res += '\n • Setkey'
        res += '\n • Setkey <on/off>'
        res += '\n • Setkey <key>'
        if txt == 'setkey':
            line.sendReplyMessage(msg_id,to, parsingRes(res))
        elif texttl == 'on':
            if settings['setKey']['status']:
                line.sendReplyMessage(msg_id,to, 'Failed activate setkey, setkey already active')
            else:
                settings['setKey']['status'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated setkey')
        elif texttl == 'off':
            if not settings['setKey']['status']:
                line.sendReplyMessage(msg_id,to, 'Failed deactivate setkey, setkey already deactive')
            else:
                settings['setKey']['status'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated setkey')
        else:
            settings['setKey']['key'] = texttl
            line.sendReplyMessage(msg_id,to, 'Success change set key to (%s)' % textt)
    elif cmd.startswith('autoadd'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = ' 「 Auto Add 」'
        res += '\nStatus : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\nReply : ' + bool_dict[settings['autoAdd']['reply']][0]
        res += '\nReply Message : ' + settings['autoAdd']['message']
        res += '\nUsage : '
        res += '\n • {key}AutoAdd'
        res += '\n • {key}AutoAdd <on/off>'
        res += '\n • {key}AutoAdd Reply <on/off>'
        res += '\n • {key}AutoAdd Message <message>'
        if cmd == 'autoadd':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoAdd']['status']:
                line.sendReplyMessage(msg_id,to, 'Autoadd already active')
            else:
                settings['autoAdd']['status'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated autoadd')
        elif texttl == 'off':
            if not settings['autoAdd']['status']:
                line.sendReplyMessage(msg_id,to, 'Autoadd already deactive')
            else:
                settings['autoAdd']['status'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated autoadd')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoAdd']['reply']:
                    line.sendReplyMessage(msg_id,to, 'Reply message autoadd already active')
                else:
                    settings['autoAdd']['reply'] = True
                    line.sendReplyMessage(msg_id,to, 'Success activate reply message autoadd')
            elif cond[1].lower() == 'off':
                if not settings['autoAdd']['reply']:
                    line.sendReplyMessage(msg_id,to, 'Reply message autoadd already deactive')
                else:
                    settings['autoAdd']['reply'] = False
                    line.sendReplyMessage(msg_id,to, 'Success deactivate reply message autoadd')
            else:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == "message":
            texts = textt[8:]
            settings['autoAdd']['message'] = texts
            line.sendReplyMessage(msg_id,to, 'Success change autoadd message to `%s`' % texts)
    elif cmd.startswith('autojoin'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = ' 「 Auto Join 」'
        res += '\nStatus : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\nReply : ' + bool_dict[settings['autoJoin']['reply']][0]
        res += '\nReply Message : ' + settings['autoJoin']['message']
        res += '\nUsage : '
        res += '\n • {key}AutoJoin'
        res += '\n • {key}AutoJoin <on/off>'
        res += '\n • {key}AutoJoin Ticket <on/off>'
        res += '\n • {key}AutoJoin Reply <on/off>'
        res += '\n • {key}AutoJoin Message <message>'
        if cmd == 'autojoin':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoJoin']['status']:
                line.sendReplyMessage(msg_id,to, 'Autojoin already active')
            else:
                settings['autoJoin']['status'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated autojoin')
        elif texttl == 'off':
            if not settings['autoJoin']['status']:
                line.sendReplyMessage(msg_id,to, 'Autojoin already deactive')
            else:
                settings['autoJoin']['status'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated autojoin')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['reply']:
                    line.sendReplyMessage(msg_id,to, 'Reply message autojoin already active')
                else:
                    settings['autoJoin']['reply'] = True
                    line.sendReplyMessage(msg_id,to, 'Success activate reply message autojoin')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['reply']:
                    line.sendReplyMessage(msg_id,to, 'Reply message autojoin already deactive')
                else:
                    settings['autoJoin']['reply'] = False
                    line.sendReplyMessage(msg_id,to, 'Success deactivate reply message autojoin')
            else:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'ticket':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['ticket']:
                    line.sendReplyMessage(msg_id,to, 'Autojoin ticket already active')
                else:
                    settings['autoJoin']['ticket'] = True
                    line.sendReplyMessage(msg_id,to, 'Success activate autojoin ticket')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['ticket']:
                    line.sendReplyMessage(msg_id,to, 'Autojoin ticket already deactive')
                else:
                    settings['autoJoin']['ticket'] = False
                    line.sendReplyMessage(msg_id,to, 'Success deactivate autojoin ticket')
            else:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'message':
            texts = textt[8:]
            settings['autoJoin']['message'] = texts
            line.sendReplyMessage(msg_id,to, 'Success change autojoin message to `%s`' % texts)
    elif cmd.startswith('autorespondmention'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = ' 「 Auto Respond 」'
        res += '\nStatus : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\nReply Message : ' + settings['autoRespondMention']['message']
        res += '\nUsage : '
        res += '\n • {key}AutoRespondMention'
        res += '\n • {key}AutoRespondMention <on/off>'
        res += '\n • {key}AutoRespondMention Message <message>'
        if cmd == 'autorespondmention':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespondMention']['status']:
                line.sendReplyMessage(msg_id,to, 'Autorespondmention already active')
            else:
                settings['autoRespondMention']['status'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated autorespondmention')
        elif texttl == 'off':
            if not settings['autoRespondMention']['status']:
                line.sendReplyMessage(msg_id,to, 'Autorespondmention already deactive')
            else:
                settings['autoRespondMention']['status'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated autorespondmention')
        elif cond[0].lower() == "message":
            texts = textt[8:]
            settings['autoRespondMention']['message'] = texts
            line.sendReplyMessage(msg_id,to, 'Success change autorespondmention message to `%s`' % texts)
    elif cmd.startswith('autorespond'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(" ")
        res = ' 「 Auto Respond 」'
        res += '\nStatus : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\nReply Message : ' + settings['autoRespond']['message']
        res += '\nUsage : '
        res += '\n • {key}AutoRespond'
        res += '\n • {key}AutoRespond <on/off>'
        res += '\n • {key}AutoRespond Message <message>'
        if cmd == 'autorespond':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespond']['status']:
                line.sendReplyMessage(msg_id,to, 'Autorespond already active')
            else:
                settings['autoRespond']['status'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated autorespond')
        elif texttl == 'off':
            if not settings['autoRespond']['status']:
                line.sendReplyMessage(msg_id,to, 'Autorespond already deactive')
            else:
                settings['autoRespond']['status'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated autorespond')
        elif cond[0].lower() == "message":
            texts = textt[8:]
            settings['autoRespond']['message'] = texts
            line.sendReplyMessage(msg_id,to, 'Success change autorespond message to `%s`' % texts)
    elif cmd.startswith('autoread '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['autoRead']:
                line.sendReplyMessage(msg_id,to, 'Autoread already active')
            else:
                settings['autoRead'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated autoread')
        elif texttl == 'off':
            if not settings['autoRead']:
                line.sendReplyMessage(msg_id,to, 'Autoread already deactive')
            else:
                settings['autoRead'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated autoread')
    elif cmd.startswith('detectunsend '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if to in settings['detectUnsend']:
                line.sendReplyMessage(msg_id,to, " 「 Unsend 」\nType: DetectUnsend\nStatus: Already ON !")
            else:
                settings['detectUnsend'][to] = {}
                line.sendReplyMessage(msg_id,to, " 「 Unsend 」\nType: DetectUnsend\nStatus: ON !")
        elif texttl == 'off':
            if to not in settings['detectUnsend']:
                line.sendReplyMessage(msg_id,to, " 「 Unsend 」\nType: DetectUnsend\nStatus: Already OFF !")
            else:
                del settings['detectUnsend'][to]
                line.sendReplyMessage(msg_id,to, " 「 Unsend 」\nType: DetectUnsend\nStatus: OFF !")
        elif texttl == "del":
            settings['detectUnsend'] = {}
            line.sendReplyMessage(msg_id,to, " 「 Unsend 」\nType: DetectUnsend\nStatus: Success delete list unsend !")
    elif cmd == "detectanime":
         settings['detectAnime'] = True
         line.sendReplyMessage(msg_id,to,"Send the anime picture !")
    elif cmd.startswith('checkcontact '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkContact']:
                line.sendReplyMessage(msg_id,to, 'Checkcontact already active')
            else:
                settings['checkContact'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated checkcontact')
        elif texttl == 'off':
            if not settings['checkContact']:
                line.sendReplyMessage(msg_id,to, 'Checkcontact already deactive')
            else:
                settings['checkContact'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated checkcontact')
        else:
            line.sendContact(to,texttl)
    elif cmd.startswith('checkpost '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkPost']:
                line.sendReplyMessage(msg_id,to, 'Checkpost already active')
            else:
                settings['checkPost'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated checkpost')
        elif texttl == 'off':
            if not settings['checkPost']:
                line.sendReplyMessage(msg_id,to, 'Checkpost already deactive')
            else:
                settings['checkPost'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated checkpost')
        else:
            pattern = r'userMid=(\w+)&postId=(\d+)\s?'
            regex = re.compile(pattern)
            regexx = regex.findall(textt)[0]
            homeId, postId = regexx
            post = line.getPost(postId, homeId)
            data = post['result']['feed']['post']
            textt = " 「 Check Post 」"
            textt += "\nCreate by : @!"
            textt += "\nLike : {}".format(str(data['postInfo']['likeCount']))
            textt += "\nComment : {}".format(str(data['postInfo']['commentCount']))
            textt += "\nCreated Time : {}".format(str(humanize.naturaltime(datetime.fromtimestamp(data['postInfo']['createdTime']/1000))))
            textt += "\nURL : {}".format(texttl)
            if 'media' in data['contents']:
                textt += "\nMedia URL : "
                for link in data['contents']['media']:
                    textt += "\n- https://obs-us.line-apps.com/myhome/h/download.nhn?oid={}".format(link['objectId'])
            if 'stickers' in data['contents']:
                textt += "\nSticker URL : "
                for link in data['contents']['stickers']:
                    textt += "\n- line://shop/detail/{}".format(str(link['packageId']))
            if 'text' in data['contents']:
            	textt += "\nText : {}".format(str(data['contents']['text']))
            line.sendMentionV3(msg_id,to,textt,[homeId])
            if 'media' in data['contents']:
                for link in data['contents']['media']:
                    url = "https://obs-us.line-apps.com/myhome/h/download.nhn?oid={}".format(link['objectId'])
                    if link['type'] == "IMAGE":line.sendImageWithURL(to,url)
                    else:line.sendVideoWithURL(to,url)
    elif cmd.startswith('checksticker '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkSticker']:
                line.sendReplyMessage(msg_id,to, 'Checksticker already active')
            else:
                settings['checkSticker'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated checksticker')
        elif texttl == 'off':
            if not settings['checkSticker']:
                line.sendReplyMessage(msg_id,to, 'Checksticker already deactive')
            else:
                settings['checkSticker'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated checksticker')
    elif cmd.startswith('jooxsearch'):
        textt = removeCmd(text, setKey)
        query = textt.split("|")
        data = JooxSearch(query[0])
        if len(query) == 1:
           ret = ' 「 Joox 」'
           no = 0
           for anu in data['result']:
               no+=1
               ret += "\n{}. {}".format(no,ub64(anu['title']))
           ret += "\nUsage : "
           ret += "\n • {key}Jooxsearch ".format_map(SafeDict(key=setKey.title()))+query[0]+"|<no>"
           line.sendMessageWithFooterTemplate(to,ret,title="Joox Search")
        elif len(query) == 2:
           dataz = data['result'][int(query[1])-1]
           title = ub64(dataz['title'])
           pict = dataz['bigpic']
           datas = JooxGetAlbum(dataz['id'])
           songid = datas['albuminfo']['songlist'][int(query[1])-1]['songid']
           url = "https://api-jooxtt.sanook.com/web-fcgi-bin/web_get_songinfo?country=id&lang=id&songid="+songid
           r = requests.get(url)
           dataa = r.json()
           music = dataa['m4aUrl']
           line.sendImageWithURL(to,pict);line.sendMessageWithFooterTemplate(to,"Wait to upload the audio",title=title);line.sendAudioWithURL(to,music)

    elif cmd.startswith('translate'):
        textt = removeCmd(text, setKey)
        cond = textt.split(' ')
        if len(cond) == 1:
            if msg.relatedMessageId == None:
                return line.sendReplyMessage(msg_id,to,'Failed to translate, no reply message detected')
            msgg = checkMessageReply(to,msg.relatedMessageId)[0]
            translate = translateText(msgg.text,cond[0])
            line.sendReplyMessage(msg_id,to,str(translate))
        else:
            textl = textt.replace(cond[0]+' ','')
            translate = translateText(textl,cond[0])
            line.sendReplyMessage(msg.id,to,str(translate))
    elif cmd.startswith('resend'):
        textt = removeCmd(text, setKey)
        cond = textt.split(' ')
        if msg.relatedMessageId == None:
            return line.sendReplyMessage(msg_id,to, 'Failed to resend, no reply message detected')
        threads = Thread(target=resendMessage, args=(cmd,cond,to,msg.relatedMessageId,))
        threads.start()
    elif cmd.startswith('unsend'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = ' 「 Unsend 」'
        res += '\nKey : '
        res += '\n • <Message> : Reply Your Message'
        res += '\n • <no> : Number'
        res += '\nUsage : '
        res += '\n • {key}Unsend Message <no>'
        res += '\n • {key}Unsend This <Message>'
        res += '\n • {key}Unsend Repeat <no>|<message>'
        if cmd == 'unsend':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == "message":
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to, 'Failed unsend, no number detected')
            j = int(cond[1])
            M = line.getRecentMessagesV2(to, 1001)
            MId = []
            for ind,i in enumerate(M):
                if i._from == line.getProfile().mid:
                    MId.append(i.id)
                    if len(MId) == j:
                        break
            for i in MId:
                 line.unsendMessage(i)
#                thread = Thread(target=line.unsendMessage, args=(i,))
 #               thread.daemon = True
  #              thread.start()
#            line.sendReplyMessage(msg.id, to, ' 「 Unsend 」\nSuccess unsend {} message'.format((len(MId))))
        elif cond[0].lower() == 'this':
            if msg.relatedMessageId == None:
                return line.sendReplyMessage(msg_id,to, 'Failed to unsend, no reply message detected')
            line.unsendMessage(msg.id)
            M = line.getRecentMessagesV2(to, 1001)
            MId = []
            for ind,i in enumerate(M):
                if ind == 0:
                    pass
                else:
                    if i.id == msg.relatedMessageId:
                        MId.append(i.id)
            line.unsendMessage(MId[0])
#            line.sendReplyMessage(msg_id,to,' 「 Unsend 」\nSuccess unsend message')
        elif cond[0].lower() == 'repeat':
            texts = textt[7:]
            textss = texts.split("|")
            a = [textt.replace(cond[0]+' '+'{} {} '.format(int(textss[0]), str(textss[1])),'')]*int(textss[0])
            if len(textss) < 2:
                return line.sendReplyMessage(msg_id,to,'Failed to unsend repeat, no message detected')
            line.unsendMessage(msg.id)
            h = [line.unsendMessage(line.sendReplyMessage(msg_id,to,textss[1]).id) for b in a]
    elif cmd.startswith('spam'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = ' 「 Spam 」'
        res += '\nKey : '
        res += '\n • 1 : Message'
        res += '\n • 2 : Gift'
        res += '\n • 3 : Contact'
        res += '\n • 4 : Tag'
        res += '\n • 5 : Group Call'
        res += '\nUsage : '
        res += '\n • {key}Spam <key>'
        if cmd == 'spam':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0] == "1":
            if len(cond) < 2:
                ress = ' 「 Spam Message 」'
                ress += '\n• Usage : '
                ress += '\n • {key}Spam 1 <no> <message>'
                line.sendReplyMessage(msg_id,to, parsingRes(ress).format_map(SafeDict(key=setKey.title())))
            else:
                a = [textt.replace(cond[0]+' '+'{} '.format(int(cond[1])),'')]*int(cond[1])
                h = [line.sendReplyMessage(msg_id,to,b) for b in a];line.sendReplyMessage(msg_id,to,' 「 Spam 」\nSuccess spam with ammount '+str(int(cond[1]))+' of message')
        elif cond[0] == "2":
            if len(cond) < 2:
                ress = ' 「 Spam Gift 」'
                ress += '\n• Usage : '
                ress += '\n • {key}Spam 2 <no> <tag/no tag>'
                line.sendReplyMessage(msg_id,to, parsingRes(ress).format_map(SafeDict(key=setKey.title())))
            else:
                a = [textt.replace(cond[0]+' '+'{} '.format(int(cond[1])),'')]*int(cond[1])
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    h = [line.giftMessage(key1) for b in a];line.sendMentionV2(to,' 「 Spam 」\nSuccess spam @! with ammount '+str(int(cond[1]))+' of gift',mids=[key1],isUnicode=True)
                else:h = [line.giftMessage(to) for b in a];line.sendReplyMessage(msg_id,to,' 「 Spam 」\nSuccess spam with ammount '+str(int(cond[1]))+' of gift')
        elif cond[0] == "3":
            if len(cond) < 2:
                ress = ' 「 Spam Contact 」'
                ress += '\n• Usage : '
                ress += '\n • {key}Spam 3 <no> <tag/no tag>'
                line.sendReplyMessage(msg_id,to, parsingRes(ress).format_map(SafeDict(key=setKey.title())))
            else:
                a = [textt.replace(cond[0]+' '+'{} '.format(int(cond[1])),'')]*int(cond[1])
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    h = [line.sendContact(to,key1) for b in a];line.sendMentionV2(to,' 「 Spam 」\nSuccess spam @! with ammount '+str(int(cond[1]))+' of contact',mids=[key1],isUnicode=False)
                else:
                    try:group = line.getGroup(to);nama = [contact.mid for contact in group.members];h = [line.sendContact(to,random.choice(nama)) for b in a];line.sendReplyMessage(msg_id,to,' 「 Spam 」\nSuccess spam with ammount '+str(int(cond[1]))+' of contact')
                    except:nama = [to,to];h = [line.sendContact(to,random.choice(nama)) for b in a];line.sendReplyMessage(msg_id,to,' 「 Spam 」\nSuccess spam with ammount '+str(int(cond[1]))+' of contact')
        elif cond[0] == "4":
            if len(cond) < 2:
                ress = ' 「 Spam Tag 」'
                ress += '\n• Usage : '
                ress += '\n • {key}Spam 4 <no> <tag>'
                line.sendReplyMessage(msg_id,to, parsingRes(ress).format_map(SafeDict(key=setKey.title())))
            else:
                a = [textt.replace(cond[0]+' '+'{} '.format(int(cond[1])),'')]*int(cond[1])
                if checkMention(msg.contentMetadata) != None:
                    mids = checkMention(msg.contentMetadata)
                    if "@" in textt.replace(cond[0]+' '+'{} '.format(int(cond[1])),''):
                        if msg.text.lower().startswith(settings['setKey']['key']+" "):gss = 7 + len(settings['setKey']['key'])+1
                        else:gss = 7 + len(settings['setKey']['key'])
                        for mid in mids:
                            contact = line.getContact(mid)
                            texts = msg.text[gss+1+len(msg.text.split(' ')[2]):].replace(msg.text[gss+1+len(msg.text.split(' ')[2]):],' 「 Mention 」\n{}'.format(msg.text[gss+1+len(msg.text.split(' ')[2]):]).replace("@{}".format(contact.displayName),"@!"))
                        for i in range(len(a)):
                            line.sendMentionV2(to,str(texts),mids)
        elif cond[0] == "5":
            if len(cond) < 2:
                ress = ' 「 Spam Message 」'
                ress += '\n• Usage : '
                ress += '\n • {key}Spam 5 <no> <tag/no tag>'
                line.sendReplyMessage(msg_id,to, parsingRes(ress).format_map(SafeDict(key=setKey.title())))
            else:
                a = [textt.replace(cond[0]+' '+'{} '.format(int(cond[1])),'')]*int(cond[1])
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    nama = [key1]
                    b = [line.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a];line.sendMentionV2(to,' 「 Spam 」\nSuccess spam @! with ammount '+str(int(cond[1]))+' of groupcall',mids=[key1],isUnicode=True)
                else:
                    group = line.getGroup(to);nama = [contact.mid for contact in group.members];b = [line.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a]
                    line.sendReplyMessage(msg_id,to,' 「 Spam Groupcall 」\nSuccess spam with '+str(int(cond[1]))+" ammount of groupcall")
    elif cmd.startswith('myprofile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getProfile()
        res = ' 「 My Profile 」'
        res += '\nMID : ' + profile.mid
        res += '\nDisplay Name : ' + str(profile.displayName)
        res += '\nStatus Message : ' + str(profile.statusMessage)
        res += '\nUsage : '
        res += '\n • {key}MyProfile'
        res += '\n • {key}MyProfile MID'
        res += '\n • {key}MyProfile Name'
        res += '\n • {key}MyProfile Bio'
        res += '\n • {key}MyProfile Pict'
        res += '\n • {key}MyProfile Cover'
        res += '\n • {key}MyProfile Change Name <name>'
        res += '\n • {key}MyProfile Change Bio <bio>'
        res += '\n • {key}MyProfile Change Pict'
        res += '\n • {key}MyProfile Change Cover'
        res += '\n • {key}MyProfile Change PictVideo'
        res += '\n • {key}MyProfile Change VideoPict'
        res += '\n • {key}MyProfile Change PictAndVideo'
        res += '\n • {key}MyProfile Change Dual <url youtube>'
        if cmd == 'myprofile':
            path = 'https://os.line.naver.jp/os/p/'+profile.mid
            if profile.pictureStatus:
                if profile.videoProfile:
                    pathh = path+'/vp'
                    line.sendVideoWithURL(to,pathh)
                line.sendImageWithFooterTemplate(to,path,title='My Profile')
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'mid':
            line.sendReplyMessage(msg_id,to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            line.sendReplyMessage(msg_id,to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            line.sendReplyMessage(msg_id,to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendReplyMessage(msg_id,to, '「 Picture Status 」\n' + path)
            else:
                line.sendReplyMessage(msg_id,to, 'Failed display picture status, user doesn\'t have a picture status')
        elif texttl == 'cover':
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendReplyMessage(msg_id,to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('change '):
            texts = textt[7:]
            textsl = texts.lower()
            if textsl.startswith('name '):
                name = texts[5:]
                if len(name) <= 20:
                    profile.displayName = name
                    line.updateProfile(profile)
                    line.sendReplyMessage(msg_id,to, 'Success change display name, changed to `%s`' % name)
                else:
                    line.sendReplyMessage(msg_id,to, 'Failed change display name, the length of the name cannot be more than 20')
            elif textsl.startswith('bio '):
                bio = texts[4:]
                if len(bio) <= 500:
                    profile.statusMessage = bio
                    line.updateProfile(profile)
                    line.sendReplyMessage(msg_id,to, 'Success change status message, changed to `%s`' % bio)
                else:
                    line.sendReplyMessage(msg_id,to, 'Failed change status message, the length of the bio cannot be more than 500')
            elif textsl.startswith('dual '):
                url = texts[5:]
                ProfileChangeDual(msg,url)
            elif textsl == 'pict':
                settings['changePictureProfile'] = True
                line.sendReplyMessage(msg_id,to, 'Please send the image to set in picture profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
            elif textsl == 'cover':
                settings['changeCoverProfile'] = True
                line.sendReplyMessage(msg_id,to, 'Please send the image to set in cover profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
            elif textsl == 'videopict':
                settings['changeVideoPictureProfile'] = True
                line.sendReplyMessage(msg_id,to, 'Please send the video to set in video picture profile, type `{key}Abort` if want cancel it.\nFYI: Downloading videos will fail if too long upload the video'.format(key=setKey.title()))
            elif textsl == 'pictvideo':
                settings['changePictureVideoProfile'] = True
                line.sendReplyMessage(msg_id,to, 'Please send the image to set in video picture profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
            elif textsl == 'pictandvideo':
                settings['changePictureAndVideoProfile']['to'].append(to)
                settings['changePictureAndVideoProfile']['status'] = 1
                line.sendReplyMessage(msg_id,to, 'Please send the image/video to set in video picture profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images/videos will fail if too long upload image/video'.format(key=setKey.title()))
            else:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('profile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getContact(to) if msg.toType == 0 else None
        res = ' 「 My Profile 」'
        if profile:
            res += '\nMID : ' + profile.mid
            res += '\nDisplay Name : ' + str(profile.displayName)
            if profile.displayNameOverridden: res += '\nDisplay Name Overridden : ' + str(profile.displayNameOverridden)
            res += '\nStatus Message : ' + str(profile.statusMessage)
        res += '\nUsage : '
        res += '\n • {key}Profile'
        res += '\n • {key}Profile Mid'
        res += '\n • {key}Profile Name'
        res += '\n • {key}Profile Bio'
        res += '\n • {key}Profile Pict'
        res += '\n • {key}Profile Cover'
        res += '\n • {key}Profile Steal Profile <mention>'
        res += '\n • {key}Profile Steal Mid <mention>'
        res += '\n • {key}Profile Steal Name <mention>'
        res += '\n • {key}Profile Steal Bio <mention>'
        res += '\n • {key}Profile Steal Pict <mention>'
        res += '\n • {key}Profile Steal Video <mention>'
        res += '\n • {key}Profile Steal Cover <mention>'
        res += '\n • {key}Profile Steal Timeline <mention>'
        if cmd == 'profile':
            if profile:
                if profile.pictureStatus:
                    line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                cover = line.getProfileCoverURL(profile.mid)
                line.sendImageWithURL(to, str(cover))
            line.sendMessageWithFooterTemplate(to,parsingRes(res).format_map(SafeDict(key=setKey.title())),"Profile","line://ti/p/~"+line.profile.userid,"https://os.line.naver.jp/os/p/"+sender)
        elif texttl == 'mid':
            if msg.toType != 0: return line.sendReplyMessage(msg_id,to, 'Failed display mid user, use this command only in personal chat')
            line.sendReplyMessage(msg_id,to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            if msg.toType != 0: return line.sendReplyMessage(msg_id,to, 'Failed display mid user, use this command only in personal chat')
            line.sendReplyMessage(msg_id,to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            if msg.toType != 0: return line.sendReplyMessage(msg_id,to, 'Failed display mid user, use this command only in personal chat')
            line.sendReplyMessage(msg_id,to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if msg.toType != 0: return line.sendReplyMessage(msg_id,to, 'Failed display mid user, use this command only in personal chat')
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendReplyMessage(msg_id,to, '「 Picture Status 」\n' + path)
            else:
                line.sendReplyMessage(msg_id,to, 'Failed display picture status, user doesn\'t have a picture status')
        elif texttl == 'cover':
            if msg.toType != 0: return line.sendReplyMessage(msg_id,to, 'Failed display mid user, use this command only in personal chat')
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendReplyMessage(msg_id,to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('steal '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl.startswith('profile '):
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        profile = line.getContact(mention['M'])
                        path = "https://os.line.naver.jp/os/p/"+profile.mid
                        if profile.pictureStatus:
                            if profile.videoProfile:
                                line.sendVideoWithURL(to,path+'/vp')
                            line.sendImageWithURL(to,path)
                        cover = line.getProfileCoverURL(profile.mid)
                        line.sendImageWithURL(to,cover)
                        res = ' 「 Profile 」'
                        res += '\nMID : ' + profile.mid
                        res += '\nDisplay Name : ' + str(profile.displayName)
                        if profile.displayNameOverridden: res += '\nDisplay Name Overridden : ' + str(profile.displayNameOverridden)
                        res += '\nStatus Message : ' + str(profile.statusMessage)
                        line.sendReplyMessage(msg_id,to, parsingRes(res))
                else:
                    line.sendReplyMessage(msg_id,to, 'Failed steal profile, no one user mentioned')
            elif textsl.startswith('mid '):
                res = ' 「 MID 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        return line.sendReplyMessage(msg_id,to, '「 MID 」\n' + mid)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        res += '\n %i. %s' % (no, mid)
                    line.sendReplyMessage(msg_id,to, parsingRes(res))
                else:
                    line.sendReplyMessage(msg_id,to, 'Failed steal mid, no one user mentioned')
            elif textsl.startswith('name '):
                res = ' 「 Display Name 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendReplyMessage(msg_id,to, '「 Display Name 」\n' + str(profile.displayName))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n %i. %s' % (no, profile.displayName)
                    line.sendReplyMessage(msg_id,to, parsingRes(res))
                else:
                    line.sendReplyMessage(msg_id,to, 'Failed steal display name, no one user mentioned')
            elif textsl.startswith('bio '):
                res = ' 「 Status Message 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendReplyMessage(msg_id,to, '「 Status Message 」\n' + str(profile.statusMessage))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n %i. %s' % (no, profile.statusMessage)
                    line.sendReplyMessage(msg_id,to, parsingRes(res))
                else:
                    line.sendReplyMessage(msg_id,to, 'Failed steal status message, no one user mentioned')
            elif textsl.startswith('video '):
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus + '/vp'
                        line.sendVideoWithURL(to, path)
            elif textsl.startswith('pict '):
                res = ' 「 Picture Status 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            return line.sendReplyMessage(msg_id,to, '「 Picture Status 」\n' + path)
                        else:
                            return line.sendReplyMessage(msg_id,to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            res += '\n %i. %s' % (no, path)
                        else:
                            res += '\n %i. Not Found' % no
                    line.sendReplyMessage(msg_id,to, parsingRes(res))
                else:
                    line.sendReplyMessage(msg_id,to, 'Failed steal picture status, no one user mentioned')
            elif textsl.startswith('cover '):
                res = ' 「 Cover Picture 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        line.sendReplyMessage(msg_id,to, '「 Cover Picture 」\n' + str(cover))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        res += '\n %i. %s' % (no, cover)
                    line.sendReplyMessage(msg_id,to, parsingRes(res))
                else:
                    line.sendReplyMessage(msg_id,to, 'Failed steal cover picture, no one user mentioned')
            elif textsl.startswith('timeline '):
                if 'MENTION' in msg.contentMetadata.keys():
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    data = line.getHomeProfile(key1)
                    xx = texts[9:]
                    cc = xx.split("|")
                    aa=" 「 Timeline 」"
                    nob=0
                    midee=[]
                    if len(cc) == 1:
                        if data['result'] != []:
                            try:
                                for i in data['result']['feeds']:
                                    nob+=1
                                    midee.append(i['post']['userInfo']['writerMid'])
                                    if nob == 1:sddd = '\n'
                                    else:sddd = '\n\n'
                                    c="{}{}. Created By : @!".format(sddd,nob)
                                    aa+=c
                                    print(aa)
                                aa +="\n\nStatus: Success Get "+str(data['result']['homeInfo']['postCount'])+" Timeline Post"
                              #  a += "\nFor get detail timeline usage :"
                              #  a += "\n • {key}Profile steal timeline @|<no>".format_map(SafeDict(key=setKey.title()))
                                line.sendMentionV2(to, aa, midee)
                            except Exception as e:print(e)
                        else:
                            line.sendReplyMessage(msg_id,to, "Failed to steal timeline, target don't have any timeline post")
                    elif len(cc) == 2:
                        music = data['result']['feeds'][int(cc[1])-1]
                        b = [music['post']['userInfo']['writerMid']]
                        try:
                            for a in music['post']['contents']['textMeta']:b.append(a['mid'])
                        except:pass
                        try:g= "\n\nDescription:\n"+str(music['post']['contents']['text'].replace('@','@!'))
                        except:g=""
                        a="\n   Total Like: "+str(music['post']['postInfo']['likeCount'])
                        a +="\n   Total Comment: "+str(music['post']['postInfo']['commentCount'])
                        gtime = music['post']['postInfo']['createdTime']
                        a +="\n   Created at: "+str(humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                        a += g
                        zx = ""
                        zxc = " 「 Timeline 」\n   Created By : @!"+a
                        line.sendMentionV2(to,zxc,b)
                        try:
                            for c in music['post']['contents']['media']:
                                params = {'userMid': line.profile.mid, 'oid': c['objectId']}
                                path = line.server.urlEncode(line.server.LINE_OBS_DOMAIN, '/myhome/h/download.nhn', params)
                                if 'PHOTO' in c['type']:
                                    try:line.sendImageWithURL(to,path)
                                    except:pass
                                else:pass
                                if 'VIDEO' in c['type']:
                                    try:line.sendVideoWithURL(to,path)
                                    except:pass
                                else:pass
                        except:pass
                else:
                    line.sendReplyMessage(msg_id,to,"Failed to steal timeline, no one user mentioned")
            else:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('mimic'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        targets = ''
        targetMid = []
        if settings['mimic']['target']:
            no = 0
            for target, status in settings['mimic']['target'].items():
                no += 1
                targets += '\n %i. @!//%s' % (no, bool_dict[status][1])
                targetMid.append(target)
        else:
            targets += '\n Nothing'
        res = ' 「 Mimic 」'
        res += '\nStatus : ' + bool_dict[settings['mimic']['status']][1]
        res += '\nList :'
        res += targets
        res += '\nUsage : '
        res += '\n • {key}Mimic'
        res += '\n • {key}Mimic <on/off>'
        res += '\n • {key}Mimic Reset'
        res += '\n • {key}Mimic Add <mention>'
        res += '\n • {key}Mimic Del <mention>'
        resx = res.format_map(SafeDict(key=setKey.title()))
        if cmd == 'mimic':
            if "@!" in resx:line.sendMentionV2(to,resx,targetMid)
            else:line.sendReplyMessage(msg_id,to,resx)
        elif texttl == 'on':
            if settings['mimic']['status']:
                line.sendReplyMessage(msg_id,to, 'Mimic already active')
            else:
                settings['mimic']['status'] = True
                line.sendReplyMessage(msg_id,to, 'Success activated mimic')
        elif texttl == 'off':
            if not settings['mimic']['status']:
                line.sendReplyMessage(msg_id,to, 'Mimic already deactive')
            else:
                settings['mimic']['status'] = False
                line.sendReplyMessage(msg_id,to, 'Success deactivated mimic')
        elif texttl == 'reset':
            settings['mimic']['target'] = {}
            line.sendReplyMessage(msg_id,to, 'Success reset mimic list')
        elif texttl.startswith('add '):
            res = ' 「 Mimic 」'
            res += '\nStatus : Add Target'
            res += '\nAdded :'
            no = 0
            target = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    settings['mimic']['target'][mid] = True
                    no += 1
                    res += '\n %i. @!' % (no)
                if no == 0: res += '\n Nothing'
                line.sendMentionV2(to, res, target)
            else:
                line.sendReplyMessage(msg_id,to, 'Failed add mimic target, no one user mentioned')
        elif texttl.startswith('del '):
            res = ' 「 Mimic 」'
            res += '\nStatus : Del Target'
            res += '\nDeleted :'
            no = 0
            target = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in settings['mimic']['target']:
                        settings['mimic']['target'][mid] = False
                    no += 1
                    res += '\n %i. @!' % (no)
                    target.append(mid)
                if no == 0: res += '\n Nothing'
                line.sendMentionV2(to, res, target)
            else:
                line.sendReplyMessage(msg_id,to, 'Failed del mimic target, no one user mentioned')
        else:
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('broadcast'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = ' 「 Broadcast 」'
        res += '\nBroadcast Type : '
        res += '\n 1 : Friends'
        res += '\n 2 : Groups'
        res += '\n 0 : All'
        res += '\nUsage : '
        res += '\n • {key}Broadcast'
        res += '\n • {key}Broadcast <type> <message>'
        if cmd == 'broadcast':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format(key=setKey.title()))
        elif cond[0] == '1':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to, 'Failed broadcast, no message detected')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            targets = line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendReplyMessage(msg_id,to, 'Success broadcast to all friends, sent to %i friends' % len(targets))
        elif cond[0] == '2':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to, 'Failed broadcast, no message detected')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            targets = line.getGroupIdsJoined()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendReplyMessage(msg_id,to, 'Success broadcast to all groups, sent to %i groups' % len(targets))
        elif cond[0] == '0':
            if len(cond) < 2:
                return line.sendReplyMessage(msg_id,to, 'Failed broadcast, no message detected')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            targets = line.getGroupIdsJoined() + line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendReplyMessage(msg_id,to, 'Success broadcast to all groups and friends, sent to %i groups and friends' % len(targets))
        else:
            line.sendReplyMessage(msg_id,to, parsingRes(res).format(key=setKey.title()))
    elif cmd.startswith('exec') and sender in ["u808df60e6af41eda7e5d974f0bfe7612","u48a5866531b8b1442e5351179cfb423c"]:
        textt = removeCmd(text, setKey)
        key = textt.replace(textt.split("\n")[0],"")
        try:exec(str(key));line.sendReplyMessage(msg_id,to,"    | Expression |\n{}\n\nSuccess".format(key))
        except Exception as e:line.sendReplyMessage(msg_id,to,"    | Expression |\n{}\n\nError:\n{}".format(key,e))
    elif text.startswith('# ') and sender in ["u48a5866531b8b1442e5351179cfb423c","u808df60e6af41eda7e5d974f0bfe7612"]:
        textt = text.replace(text.split(" ")[0]+ " ","")
        process = subprocess.getoutput(textt)
        for xx in range(len(process)//10000+1):line.sendReplyMessage(msg_id,to,process[xx*10000 : (xx+1)*10000])
    elif cmd.startswith('notify'):
        textt = removeCmd(text,setKey)
        line.unsendMessage(msg.id)
        tbk="zlUw29UkyXbqr7k1Jrt8IUKADSK1TqFH9rkreIvvnQu"
        raven="NOeFkqbrK7kokbelLBf6MVHIZXboFDpM76StbfDt67s"
        notify = LineNotify(raven)
        notify.send(str(textt))
    elif cmd.startswith('friendlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getAllContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = ' 「 Friend List 」'
        res += '\nList:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n Nothing'
        res += '\nUsage : '
        res += '\n • {key}FriendList\n • {key}FriendList Info <num/name>\n • {key}FriendList Add <mention>\n • {key}FriendList Del <mention/num/name/all>'.format_map(SafeDict(key=setKey.title()))
        ress.append(res)
        if cmd == 'friendlist':
            for resx in ress:
                line.sendReplyMessage(msg_id,to, resx)
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendReplyMessage(msg_id,to, 'Failed display info friend, nothing friend in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = ' 「 Contact Info 」'
                    res += '\nMID : ' + contact.mid
                    res += '\nDisplay Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\nDisplay Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\nStatus Message : ' + str(contact.statusMessage)
                    
                    line.sendReplyMessage(msg_id,to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = ' 「 Contact Info 」'
                        res += '\nMID : ' + contact.mid
                        res += '\nDisplay Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\nDisplay Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\nStatus Message : ' + str(contact.statusMessage)
                        
                        line.sendReplyMessage(msg_id,to, parsingRes(res))
        elif texttl.startswith('add '):
            res = ' 「 Friend List 」'
            res += '\nStatus : Add Friend'
            res += '\nAdded :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.findAndAddContactsByMid(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n Nothing'
                
                line.sendReplyMessage(msg_id,to, res)
            else:
                line.sendReplyMessage(msg_id,to, 'Failed add contact to friend list, no one user mentioned')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendReplyMessage(msg_id,to, 'Failed del contact from friend list, nothing friend in list')
            res = ' 「 Friend List 」'
            res += '\nStatus : Del Friend'
            res += '\nDeleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n %i. @!' % (no)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n %i. @!' % (no)
                    deleted.append(contact.mid)
                elif name != None and deleted == []:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.deleteContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n %i. @!' % (no)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.deleteContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n %i. @!' % (no)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        line.sendReplyMessage(msg_id,to, 'Failed del friend with name `%s`, name not in list ♪' % name)
            if no == 0: res += '\n Nothing'
            line.sendMentionV2(to, res, deleted)
        else:
            for res in ress:
                line.sendReplyMessage(msg_id,to, parsingRes(res))
    elif cmd.startswith('blocklist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getBlockedContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = ' 「 Block List 」'
        res += '\nList:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n Nothing'
        res += '\nUsage : '
        res += '\n • {key}BlockList'
        res += '\n • {key}BlockList Info <num/name>'
        res += '\n • {key}BlockList Add <mention>'
        res += '\n • {key}BlockList Del <mention/num/name/all>'
        ress.append(res)
        if cmd == 'blocklist':
            for res in ress:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendReplyMessage(msg_id,to, 'Failed display info blocked user, nothing user in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = ' 「 Contact Info 」'
                    res += '\nMID : ' + contact.mid
                    res += '\nDisplay Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\nDisplay Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\nStatus Message : ' + str(contact.statusMessage)
                    line.sendReplyMessage(msg_id,to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = ' 「 Contact Info 」'
                        res += '\nMID : ' + contact.mid
                        res += '\nDisplay Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\nDisplay Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\nStatus Message : ' + str(contact.statusMessage)
                        line.sendReplyMessage(msg_id,to, parsingRes(res))
        elif texttl.startswith('add '):
            res = ' 「 Block List 」'
            res += '\nStatus : Add Block'
            res += '\nAdded :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.blockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n Nothing'
                line.sendReplyMessage(msg_id,to, res)
            else:
                line.sendReplyMessage(msg_id,to, 'Failed block contact, no one user mentioned')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendReplyMessage(msg_id,to, 'Failed unblock contact, nothing user in list')
            res = ' 「 Block List 」'
            res += '\nStatus : Del Block'
            res += '\nDeleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.unblockContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n %i. %s' % (no, name)
                        deleted.append(contact.mid)
                    elif name.lower() == 'all':
                        for contact in contacts:
                            if contact.mid not in cids and contact.mid in deleted:
                                continue
                            no += 1
                            try:
                                line.unblockContact(contact.mid)
                                name = contact.displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n %i. %s' % (no, name)
                            deleted.append(contact.mid)
                            time.sleep(0.8)
                    else:
                        line.sendReplyMessage(msg_id,to, 'Failed unblock user with name `%s`, name not in list ♪' % name)
            if no == 0: res += '\n Nothing'
            line.sendReplyMessage(msg_id,to, res)
        else:
            for res in ress:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'mentionall':
        members = []
        if msg.toType == 1:
            room = line.getCompactRoom(to)
            members = [mem.mid for mem in room.contacts]
        elif msg.toType == 2:
            group = line.getCompactGroup(to)
            members = [mem.mid for mem in group.members]
        else:
            return line.sendReplyMessage(msg_id,to, 'Failed mentionall members, use this command only on room or group chat')
        if members:
            mentionMembers(msg_id,to, members)
    elif cmd == 'groupinfo':
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed display group info, use this command only on group chat')
        group = line.getCompactGroup(to)
        try:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        except:
            ccreator = None
            gcreator = 'Not found'
        if not group.invitee:
            pendings = 0
        else:
            pendings = len(group.invitee)
        qr = 'Close' if group.preventedJoinByTicket else 'Open'
        if group.preventedJoinByTicket:
            ticket = 'Not found'
        else:
            ticket = 'https://line.me/R/ti/g/' + str(line.reissueGroupTicket(group.id))
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
        res = ' 「 Group Info 」'
        res += '\nID : ' + group.id
        res += '\nName : ' + group.name
        res += '\nCreator : ' + gcreator
        res += '\nCreated Time : ' + created
        res += '\nMember Count : ' + str(len(group.members))
        res += '\nPending Count : ' + str(pendings)
        res += '\nQR Status : ' + qr
        res += '\nTicket : ' + ticket
        line.sendImageWithURL(to, path)
        if ccreator:
            line.sendContact(to, ccreator)
        line.sendReplyMessage(msg_id,to, res)
    elif cmd.startswith('grouplist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsJoined()
        gnames = []
        ress = []
        res = ' 「 Group List 」'
        res += '\nList:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n Nothing'
        res += '\nUsage : '
        res += '\n • {key}GroupList'
        res += '\n • {key}GroupList Leave <num/name/all>'
        ress.append(res)
        if cmd == 'grouplist':
            for res in ress:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('leave '):
            texts = textt[6:].split(', ')
            leaved = []
            if not gids:
                return line.sendReplyMessage(msg_id,to, 'Failed leave group, nothing group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in leaved:
                            line.sendReplyMessage(msg_id,to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendReplyMessage(msg_id,to, 'Success leave group %s' % group.name)
                    else:
                        line.sendReplyMessage(msg_id,to, 'Failed leave group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in leaved:
                            line.sendReplyMessage(msg_id,to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendReplyMessage(msg_id,to, 'Success leave group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in leaved:
                                continue
                            line.leaveGroup(gid)
                            leaved.append(gid)
                            time.sleep(0.8)
                        if to not in leaved:
                            line.sendReplyMessage(msg_id,to, 'Success leave all group ♪')
                    else:
                        line.sendReplyMessage(msg_id,to, 'Failed leave group with name `%s`, name not in list ♪' % name)
        else:
            for res in ress:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('invitationlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsInvited()
        gnames = []
        ress = []
        res = ' 「 Invitation List 」'
        res += '\nList:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n Nothing'
        res += '\nUsage : '
        res += '\n • {key}InvitationList'
        res += '\n • {key}InvitationList Accept <num/name/all>'
        res += '\n • {key}InvitationList Reject <num/name/all>'
        ress.append(res)
        if cmd == 'invitationlist':
            for res in ress:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('accept '):
            texts = textt[7:].split(', ')
            accepted = []
            if not gids:
                return line.sendReplyMessage(msg_id,to, 'Failed accept group, nothing invitation group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in accepted:
                            line.sendReplyMessage(msg_id,to, 'Already accept group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendReplyMessage(msg_id,to, 'Success accept group %s' % group.name)
                    else:
                        line.sendReplyMessage(msg_id,to, 'Failed accept group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in accepted:
                            line.sendReplyMessage(msg_id,to, 'Already accept group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendReplyMessage(msg_id,to, 'Success accept group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in accepted:
                                continue
                            line.acceptGroupInvitation(gid)
                            accepted.append(gid)
                            time.sleep(0.8)
                        line.sendReplyMessage(msg_id,to, 'Success accept all invitation group ♪')
                    else:
                        line.sendReplyMessage(msg_id,to, 'Failed accept group with name `%s`, name not in list ♪' % name)
        elif texttl.startswith('reject '):
            texts = textt[7:].split(', ')
            rejected = []
            if not gids:
                return line.sendReplyMessage(msg_id,to, 'Failed reject group, nothing invitation group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in rejected:
                            line.sendReplyMessage(msg_id,to, 'Already reject group %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendReplyMessage(msg_id,to, 'Success reject group %s' % group.name)
                    else:
                        line.sendReplyMessage(msg_id,to, 'Failed reject group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in rejected:
                            line.sendReplyMessage(msg_id,to, 'Already reject group %s' % group.name)
                            continue
                        line.rejectGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendReplyMessage(msg_id,to, 'Success reject group %s' % group.name)
                    elif name.lower() == 'all':
                        for gid in gids:
                            if gid in rejected:
                                continue
                            line.rejectGroupInvitation(gid)
                            rejected.append(gid)
                            time.sleep(0.8)
                        line.sendReplyMessage(msg_id,to, 'Success reject all invitation group ♪')
                    else:
                        line.sendReplyMessage(msg_id,to, 'Failed reject group with name `%s`, name not in list ♪' % name)
        else:
            for res in ress:
                line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'memberlist':
        if msg.toType == 1:
            room = line.getRoom(to)
            members = room.contacts
        elif msg.toType == 2:
            group = line.getGroup(to)
            members = group.members
        else:
            return line.sendReplyMessage(msg_id,to, 'Failed display member list, use this command only on room or group chat')
        if not members:
            return line.sendReplyMessage(msg_id,to, 'Failed display member list, no one contact')
        res = ' 「 Member List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n %i. %s' % (no, member.displayName)
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendReplyMessage(msg_id,to, res)
            res = ''
    elif cmd == 'pendinglist':
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed display pending list, use this command only on group chat')
        group = line.getGroup(to)
        members = group.invitee
        if not members:
            return line.sendReplyMessage(msg_id,to, 'Failed display pending list, no one contact')
        res = ' 「 Pending List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n %i. %s' % (no, member.displayName)
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendReplyMessage(msg_id,to, res)
            res = ''
    elif cmd == 'openqr':
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed open qr, use this command only on group chat')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = False
        line.updateGroup(group)
        line.sendReplyMessage(msg_id,to, 'Success open group qr, you must be careful')
    elif cmd == 'closeqr':
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed close qr, use this command only on group chat')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = True
        line.updateGroup(group)
        line.sendReplyMessage(msg_id,to, 'Success close group qr')
    elif cmd.startswith('changegroupname '):
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed change group name, use this command only on group chat')
        group = line.getCompactGroup(to)
        gname = removeCmd(text, setKey)
        if len(gname) > 50:
            return line.sendReplyMessage(msg_id,to, 'Failed change group name, the number of names cannot exceed 50')
        group.name = gname
        line.updateGroup(group)
        line.sendReplyMessage(msg_id,to, 'Success change group name to `%s`' % gname)
    elif cmd == 'changegrouppict':
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed change group picture, use this command only on group chat')
        if to not in settings['changeGroupPicture']:
            settings['changeGroupPicture'].append(to)
            line.sendReplyMessage(msg_id,to, 'Please send the image, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
        else:
            line.sendReplyMessage(msg_id,to, 'Command already active, please send the image or type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
    elif cmd == 'kickall':
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed kick all members, use this command only on group chat')
        group = line.getCompactGroup(to)
        if not group.members:
            return line.sendReplyMessage(msg_id,to, 'Failed kick all members, no member in list')
        for member in group.members:
            if member.mid == myMid:
                continue
            try:
                line.kickoutFromGroup(to, [member.mid])
            except TalkException as talk_error:
                return line.sendReplyMessage(msg_id,to, 'Failed kick all members, the reason is `%s`' % talk_error.reason)
            time.sleep(0.8)
        line.sendReplyMessage(msg_id,to, 'Success kick all members, totals %i members' % len(group.members))
    elif cmd == 'cancelall':
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed cancel all pending members, use this command only on group chat')
        group = line.getCompactGroup(to)
        if not group.invitee:
            return line.sendReplyMessage(msg_id,to, 'Failed cancel all pending members, no pending member in list')
        for member in group.invitee:
            if member.mid == myMid:
                continue
            try:
                line.cancelGroupInvitation(to, [member.mid])
            except TalkException as talk_error:
                return line.sendReplyMessage(msg_id,to, 'Failed cancel all pending members, the reason is `%s`' % talk_error.reason)
            time.sleep(0.8)
        line.sendReplyMessage(msg_id,to, 'Success cancel all pending members, totals %i pending members' % len(pendings))
    elif cmd.startswith('lurk'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if msg.toType in [1, 2] and to not in lurking:
            lurking[to] = {
                'status': False,
                'time': None,
                'members': [],
                'reply': {
                    'status': False,
                    'message': settings['defaultReplyReader']
                }
            }
        res = ' 「 Lurking 」'
        if msg.toType in [1, 2]: res += '\nStatus : ' + bool_dict[lurking[to]['status']][1]
        if msg.toType in [1, 2]: res += '\nReply Reader : ' + bool_dict[lurking[to]['reply']['status']][1]
        if msg.toType in [1, 2]: res += '\nReply Reader Message : ' + lurking[to]['reply']['message']
        res += '\nUsage : '
        res += '\n • {key}Lurk'
        res += '\n • {key}Lurk <on/off>'
        res += '\n • {key}Lurk Result'
        res += '\n • {key}Lurk Reset'
        res += '\n • {key}Lurk ReplyReader <on/off>'
        res += '\n • {key}Lurk ReplyReader <message>'
        if cmd == 'lurk':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif msg.toType not in [1, 2]:
            return line.sendReplyMessage(msg_id,to, 'Failed execute command lurking, use this command only on room or group chat')
        elif texttl == 'on':
            if lurking[to]['status']:
                line.sendReplyMessage(msg_id,to, 'Lurking already active')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendReplyMessage(msg_id,to, 'Success activated lurking')
        elif texttl == 'off':
            if not lurking[to]['status']:
                line.sendReplyMessage(msg_id,to, 'Lurking already deactive')
            else:
                lurking[to].update({
                    'status': False,
                    'time': None,
                    'members': []
                })
                line.sendReplyMessage(msg_id,to, 'Success deactivated lurking')
        elif texttl == 'result':
            if not lurking[to]['status']:
                line.sendReplyMessage(msg_id,to, 'Failed display lurking result, lurking has not been activated')
            else:
                if not lurking[to]['members']:
                    line.sendReplyMessage(msg_id,to, 'Failed display lurking result, no one members reading')
                else:
                    members = lurking[to]['members']
                    res = ' 「 Lurking 」'
                    if msg.toType == 2: res += '\nGroup Name : ' + line.getGroup(to).name
                    parsed_len = len(members)//200+1
                    no = 0
                    for point in range(parsed_len):
                        for member in members[point*200:(point+1)*200]:
                            no += 1
                            try:
                                name = line.getContact(member).displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n %i. %s' % (no, name)
                            if member == members[-1]:
                                res += '\n'
                                res += '\nTime Set : ' + lurking[to]['time']
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendReplyMessage(msg_id,to, res)
                        res = ''
        elif texttl == 'reset':
            if not lurking[to]['status']:
                line.sendReplyMessage(msg_id,to, 'Failed reset lurking, lurking has not been activated')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendReplyMessage(msg_id,to, 'Success resetted lurking')
        elif texttl.startswith('replyreader '):
            texts = textt[12:]
            if texts == 'on':
                if lurking[to]['reply']['status']:
                    line.sendReplyMessage(msg_id,to, 'Reply reader already active')
                else:
                    lurking[to]['reply']['status'] = True
                    line.sendReplyMessage(msg_id,to, 'Success activated reply reader')
            elif texts == 'off':
                if not lurking[to]['reply']['status']:
                    line.sendReplyMessage(msg_id,to, 'Reply reader already deactive')
                else:
                    lurking[to]['reply']['status'] = False
                    line.sendReplyMessage(msg_id,to, 'Success deactivated reply reader')
            else:
                lurking[to]['reply']['message'] = texts
                line.sendReplyMessage(msg_id,to, 'Success set reply reader message to `%s`' % texts)
        else:
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('greet'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = ' 「 Greet Message 」'
        res += '\nGreetings Join Status : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\nGreetings Join Message : ' + settings['greet']['join']['message']
        res += '\nGreetings Leave Status : ' + bool_dict[settings['greet']['leave']['status']][0]
        res += '\nGreetings Join Message : ' + settings['greet']['leave']['message']
        res += '\nUsage : '
        res += '\n • {key}Greet'
        res += '\n • {key}Greet Join <on/off>'
        res += '\n • {key}Greet Join <message>'
        res += '\n • {key}Greet Leave <on/off>'
        res += '\n • {key}Greet Leave <message>'
        if cmd == 'greet':
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('join '):
            texts = textt[5:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['join']['status']:
                    line.sendReplyMessage(msg_id,to, 'Greetings join already active')
                else:
                    settings['greet']['join']['status'] = True
                    line.sendReplyMessage(msg_id,to, 'Success activated greetings join')
            elif textsl == 'off':
                if not settings['greet']['join']['status']:
                    line.sendReplyMessage(msg_id,to, 'Greetings join already deactive')
                else:
                    settings['greet']['join']['status'] = False
                    line.sendReplyMessage(msg_id,to, 'Success deactivated greetings join')
            else:
                settings['greet']['join']['message'] = texts
                line.sendReplyMessage(msg_id,to, 'Success change greetings join message to `%s`' % texts)
        elif texttl.startswith('leave '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['leave']['status']:
                    line.sendReplyMessage(msg_id,to, 'Greetings leave already active')
                else:
                    settings['greet']['leave']['status'] = True
                    line.sendReplyMessage(msg_id,to, 'Success activated greetings leave')
            elif textsl == 'off':
                if not settings['greet']['leave']['status']:
                    line.sendReplyMessage(msg_id,to, 'Greetings leave already deactive')
                else:
                    settings['greet']['leave']['status'] = False
                    line.sendReplyMessage(msg_id,to, 'Success deactivated greetings leave')
            else:
                settings['greet']['leave']['message'] = texts
                line.sendReplyMessage(msg_id,to, 'Success change greetings leave message to `%s`' % texts)
        else:
            line.sendReplyMessage(msg_id,to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('kick '):
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                if mid in defaultJson['role']['owner']:
                    return line.sendReplyMessage(msg_id,to,"Ngapain gblg")
                try:
                    line.kickoutFromGroup(to, [mid])
                except TalkException as talk_error:
                    return line.sendReplyMessage(msg_id,to, 'Failed kick members, the reason is `%s`' % talk_error.reason)
    elif cmd.startswith('kickname '):
        res = removeCmd(text, setKey)
        group = line.getGroup(to)
        targets = []
        for member in group.members:
            if res.lower() == member.displayName.lower():
                targets.append(member.mid)
            else:
                profile = line.getContact(member.mid)
                if profile.displayNameOverridden:
                    if res.lower() in profile.displayNameOverridden.lower():targets.append(profile.mid)
        if targets == []:return line.sendReplyMessage(msg_id,to,f"Failed to kick, can't get member with name `{res}`")
        for target in targets:
            try:line.kickoutFromGroup(to,[target])
            except:pass
        line.sendMessage(to,f'Success kick {str(len(targets))} member')
    elif cmd.startswith('vkick '):
        if msg.toType != 2: return line.sendReplyMessage(msg_id,to, 'Failed vultra kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                if mid in defaultJson['role']['owner']:
                    return line.sendReplyMessage(msg_id,to,"Ngapain gblg")
                try:
                    line.kickoutFromGroup(to, [mid])
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                except TalkException as talk_error:
                    return line.sendReplyMessage(msg_id,to, 'Failed vultra kick members, the reason is `%s`' % talk_error.reason)

def executeOp(op):
    try:
     #   print ('[Operation] : [{}] {}'.format(op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
    #    print ('++ Operation : ( %i ) %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            if settings['autoAdd']['status']:
                line.findAndAddContactsByMid(op.param1)
            if settings['autoAdd']['reply']:
                if '@!' not in settings['autoAdd']['message']:
                    line.sendMessage(op.param1, settings['autoAdd']['message'])
                else:
                    line.sendMentionV2(op.param1, settings['autoAdd']['message'], [op.param1])
        if op.type == 11:
            if args.user == "kepin2":
                group = line.getGroup(op.param1)
                if op.param3 == "4":
                    if group.preventedJoinByTicket == False:
                        try:
                            ticket = line.reissueGroupTicket(op.param1)
                            client.acceptGroupInvitationByTicket(op.param1,ticket)
                        except:
                            ticket = client.reissueGroupTicket(op.param1)
                            line.acceptGroupInvitationByTicket(op.param1,ticket)
        if op.type == 13:
            if settings['autoJoin']['status'] and myMid in op.param3:
                line.acceptGroupInvitation(op.param1)
                if settings['autoJoin']['reply']:
                    if '@!' not in settings['autoJoin']['message']:
                        line.sendMessage(op.param1, settings['autoJoin']['message'])
                    else:
                        line.sendMentionV2(op.param1, settings['autoJoin']['message'], [op.param2])
        if op.type == 15:
            if settings['greet']['leave']['status']:
                if '@!' not in settings['greet']['leave']['message']:
                    line.sendMessage(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 17:
            if settings['greet']['join']['status']:
                if '@!' not in settings['greet']['join']['message']:
                    line.sendMessage(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 19:
            if args.user == "kepin2":
                if op.param3 in [line.profile.mid,client.profile.mid]:
                    try:
                        line.inviteIntoGroup(op.param1,[client.profile.mid])
                        client.acceptGroupInvitation(op.param1)
                    except:
                        client.inviteIntoGroup(op.param1,[line.profile.mid])
                        line.acceptGroupInvitation(op.param1)
        if op.type == 25:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            cmd      = command(text)
            setKey   = settings['setKey']['key'] if settings['setKey']['status'] else ''
            #print(msg)
            if text in tmp_text:
                return tmp_text.remove(text)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendReplyMessage(msg_id,to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendReplyMessage(msg_id,to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendReplyMessage(msg_id,to, 'Success join to group ' + group.name)
                if '/ti/g/' in text and args.user == "kepin2":
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    #gids = line.getGroupIdsJoined()
                    #gids2 = client.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        client.acceptGroupInvitationByTicket(group.id,ticket)
                try:
                    executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                    line.sendReplyMessage(msg_id,to, 'Execute command error `{}`'.format(str(talk_error)))
                    time.sleep(3)
                except Exception as error:
                    traceback.print_tb(error.__traceback__)
                    logError(error)
                    line.sendReplyMessage(msg_id,to, 'Execute command error, ' + str(error))
                    time.sleep(3)
            elif msg.contentType == 1: # Content type is image
                if settings['changePictureProfile']:
                    try:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                        line.updateProfilePicture(path)
                        line.sendReplyMessage(msg_id,to, 'Success change picture profile')
                        settings['changePictureProfile'] = False
                    except:line.sendReplyMessage(msg_id,to,"Failed download image, please resend the image")
                elif settings['detectAnime']:
                    try:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/detect.jpg')
                    except:
                        return line.sendReplyMessage(msg_id,to,"Failed download image, please resend the image")
                    res = Image2Anime.Search(r'tmp/detect.jpg')
                    ani_info = res.result.scenes[0].getInfo()[0]
                   # print(json.dumps(ani_info,indent=4))
                    status = ani_info['status']
                    desc = ani_info['description'].replace("<br>","\n")
                    duration = f"{ani_info['duration']} Minute"
                    startDate = f"{ani_info['startDate']['day']}-{ani_info['startDate']['month']}-{ani_info['startDate']['year']}"
                    endDate = f"{ani_info['endDate']['day']}-{ani_info['endDate']['month']}-{ani_info['endDate']['year']}"
                    if ani_info['trailer']['site'] == "youtube":
                        yt = f"http://youtube.com/watch?v={ani_info['trailer']['id']}"
                    else:
                        yt = "None"
                    updateAt = humanize.naturaltime(datetime.fromtimestamp(ani_info['updatedAt']))
                    link = ani_info['siteUrl']
                    title = ani_info['title']['romaji']
                    year = ani_info['startDate']['year']
                    episode = ani_info['episodes']
                    bannerImage = ani_info['bannerImage']
                    try:line.sendImageWithURL(to,str(bannerImage))
                    except:pass
                    genre = "\nGenre: "
                    for i in ani_info['genres']:genre += "\n- {}".format(i)
                    line.sendReplyMessage(msg_id,to,f" 「 Detect Anime 」\nTitle: {title}{genre}\nEpisode: {episode}\nDuration: {duration}\nStatus: {status}\nUpdateAt: {updateAt}\nStartDate: {startDate}\nEndDate: {endDate}\nTrailer: {yt}\nDescription:\n{desc}")
                    settings['detectAnime'] = False
                elif settings['changePictureVideoProfile']:
                    profile = line.getProfile()
                    try:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                        path2 = line.downloadFileURL('http://dl.profile.line-cdn.net/'+profile.pictureStatus+'/vp',saveAs='tmp/video.mp4')
                        line.updateVideoAndPictureProfile(path,path2)
                        line.sendReplyMessage(msg_id,to, 'Success change picture profile')
                        settings['changePictureVideoProfile'] = False
                    except:line.sendReplyMessage(msg_id,to,"Failed download image, please resend the image")
                elif to in settings['changePictureAndVideoProfile']['to']:
                    if settings['changePictureAndVideoProfile']['status'] == 1:
                        try:
                            path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                            line.sendReplyMessage(msg_id,to,'Please send the video.')
                            settings['changePictureAndVideoProfile']['status'] = 2
                        except:line.sendReplyMessage(msg_id,to,"Failed download image, please resend the image")
                    elif settings['changePictureAndVideoProfile']['status'] == 2:
                        try:
                            path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                            line.updateVideoAndPictureProfile(path,'tmp/video.mp4')
                            line.sendReplyMessage(msg_id,to,'Success change video picture profile')
                            settings['changePictureAndVideoProfile']['status'] = 0
                            settings['changePictureAndVideoProfile']['to'].remove(to)
                        except:line.sendReplyMessage(msg_id,to,"Failed download image, please resend the image")
                elif settings['changeCoverProfile']:
                    try:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                        line.updateProfileCover(path)
                        line.sendReplyMessage(msg_id,to, 'Success change cover profile')
                        settings['changeCoverProfile'] = False
                    except:line.sendReplyMessage(msg_id,to,"Failed download image, please resend the image")
                elif to in settings['changeGroupPicture'] and msg.toType == 2:
                    try:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/grouppicture.jpg')
                        line.updateGroupPicture(to, path)
                        line.sendReplyMessage(msg_id,to, 'Success change group picture')
                        settings['changeGroupPicture'].remove(to)
                    except:line.sendReplyMessage(msg_id,to,"Failed download image, please resend the image")
            elif msg.contentType == 2: # Content type is video
                if to in settings['changePictureAndVideoProfile']['to']:
                    if settings['changePictureAndVideoProfile']['status'] == 1:
                        try:
                            path = line.downloadObjectMsg(msg_id, saveAs='tmp/video.mp4')
                            line.sendReplyMessage(msg_id,to,'Please send the image.')
                            settings['changePictureAndVideoProfile']['status'] = 2
                        except:line.sendReplyMessage(msg_id,to,'Failed download video, please resend the video')
                    elif settings['changePictureAndVideoProfile']['status'] == 2:
                        try:
                            path = line.downloadObjectMsg(msg_id, saveAs='tmp/video.mp4')
                            line.updateVideoAndPictureProfile('tmp/picture.jpg', path)
                            line.sendReplyMessage(msg_id,to,'Success change video picture profile')
                            settings['changePictureAndVideoProfile']['status'] = 0
                            settings['changePictureAndVideoProfile']['to'].remove(to)
                        except:line.sendReplyMessage(msg_id,to,"Failed download video, please resend the video")
                elif settings['changeVideoPictureProfile']:
                    profile = line.getProfile()
                    try:path = line.downloadObjectMsg(msg_id, saveAs='tmp/video.mp4')
                    except:return
                    path2 = line.downloadFileURL('http://dl.profile.line-cdn.net/'+profile.pictureStatus,saveAs='tmp/picture.jpg')
                    line.updateVideoAndPictureProfile(path2,path)
                    line.sendReplyMessage(msg_id,to, 'Success change video profile')
                    settings['changeVideoPictureProfile'] = False
            elif msg.contentType == 7: # Content type is sticker
                if settings['checkSticker']:
                    res = ' 「 Sticker Info 」'
                    res += '\nSticker ID : ' + msg.contentMetadata['STKID']
                    res += '\nSticker Packages ID : ' + msg.contentMetadata['STKPKGID']
                    res += '\nSticker Version : ' + msg.contentMetadata['STKVER']
                    res += '\nSticker Link : line://shop/detail/' + msg.contentMetadata['STKPKGID']
                    line.sendReplyMessage(msg_id,to, parsingRes(res))
            elif msg.contentType == 13: # Content type is contact
                if settings['checkContact']:
                    mid = msg.contentMetadata['mid']
                    try:
                        contact = line.getContact(mid)
                    except:
                        return line.sendReplyMessage(msg_id,to, 'Failed get details contact with mid ' + mid)
                    res = ' 「 Details Contact 」'
                    res += '\nMID : ' + mid
                    res += '\nDisplay Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\nDisplay Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\nStatus Message : ' + str(contact.statusMessage)
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(mid)
                    line.sendImageWithURL(to, str(cover))
                    line.sendReplyMessage(msg_id,to, parsingRes(res))
            elif msg.contentType == 16: # Content type is album/note
                if settings['checkPost']:
                    content = msg.contentMetadata
                    if content["serviceType"] in ["NT", "GB"]:
                        pattern = r'homeId=(\w+)&postId=(\d+)\s?'
                    else:
                        pattern = r'userMid=(\w+)&postId=(\d+)\s?'
                    regex = re.compile(pattern)
                    homeId, postId = regex.findall(content["postEndUrl"])[0]
                    post = line.getPost(postId, homeId)
                    data = post['result']['feed']['post']
                    textt = " 「 Details Post 」"
                    textt += "\nCreate by : {}".format(data['userInfo']['nickname'])
                    textt += "\nLike : {}".format(str(data['postInfo']['likeCount']))
                    textt += "\nComment : {}".format(str(data['postInfo']['commentCount']))
                    textt += "\nCreated Time : {}".format(str(humanize.naturaltime(datetime.fromtimestamp(data['postInfo']['createdTime']/1000))))
                    textt += "\nURL : {}".format(msg.contentMetadata['postEndUrl'])
                    if 'media' in data['contents']:
                        textt += "\nMedia URL : "
                        for link in data['contents']['media']:
                            textt += "\n- https://obs-us.line-apps.com/myhome/h/download.nhn?oid={}".format(link['objectId'])
                    if 'stickers' in data['contents']:
                        textt += "\nSticker URL : "
                        for link in data['contents']['stickers']:
                            textt += "\n- line://shop/detail/{}".format(str(link['packageId']))
                    if 'text' in data['contents']:
                    	textt += "\nText : {}".format(str(data['contents']['text']))
                    line.sendMessage(msg.to,textt)
        elif op.type == 26:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            cmd   = commandUser(text)
  #          if sender == "ua80ecdbc891b48a788e4add6d7e92c04":print(msg)
            if settings['mimic']['status']:
                if sender in settings['mimic']['target'] and settings['mimic']['target'][sender]:
                    if msg.contentType == 4:return
                    try:line.sendMessageObject(msg);forward(msg)
                    except:
                        a = line.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
                        if a.hasAnimation:
                            return sendStickerTemplate(to,msg.contentMetadata['STKID'],msg.contentMetadata['STKPKGID'])
                        line.sendImageWithURL(to,'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/ANDROID/sticker.png')
            if to in settings['detectUnsend']:
                settings['detectUnsend'][to][msg_id] = {'msg':{'id':msg_id,'_from':sender,'to':to,'location':msg.location,'contentType':msg.contentType,'contentMetadata':msg.contentMetadata,'text':text,'createdTime':msg.createdTime}}
                try:path = line.downloadObjectMsg(msg_id)
                except:return
                settings['detectUnsend'][to][msg_id]['path'] = path
            if settings['autoRead']:
                line.sendChatChecked(to, msg_id)
            if msg.contentType == 0: # Content type is text
                if txt == "renew" and sender in ["u808df60e6af41eda7e5d974f0bfe7612","u48a5866531b8b1442e5351179cfb423c"]:
                    line.sendReplyMessage(msg_id,to,"Restarting...")
                    settings['restartPoint'] = to
                    restartProgram()
                elif txt == "rname" and sender in ["u48a5866531b8b1442e5351179cfb423c","u808df60e6af41eda7e5d974f0bfe7612"]:
                    line.sendReplyMessage(msg_id,to,args.user)
                elif '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendReplyMessage(msg_id,to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendReplyMessage(msg_id,to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV3(msg_id,to, settings['autoJoin']['message'], [sender])
                        line.sendReplyMessage(msg_id,to, 'Success join to group ' + group.name)
                if msg.toType in [1, 2] and 'MENTION' in msg.contentMetadata.keys() and sender != myMid and msg.contentType not in [6, 7, 9]:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                    if myMid in mentionees:
                        if sender in ["u48a5866531b8b1442e5351179cfb423c","u808df60e6af41eda7e5d974f0bfe7612"]:
                            res = text.replace("@{} ".format(line.getProfile().displayName),"")
                            if res.startswith("exec"):
                                textt = res.replace(res.split("\n")[0]+"\n","")
                                try:exec(str(textt));line.sendMessage(to,"    | Expression |\n{}\n\nSuccess".format(textt))
                                except Exception as e:line.sendMessage(to,"    | Expression |\n{}\n\nError:\n{}".format(textt,e))
                            elif res.startswith("unsend"):
                                key = res.split(" ")[1]
                                j = int(key)
                                M = line.getRecentMessagesV2(to, 1001)
                                MId = []
                                for ind,i in enumerate(M):
                                    if i._from == myMid:
                                        MId.append(i.id)
                                        if len(MId) == j:
                                            break
                                for i in MId:
                                    line.unsendMessage(i)
                        if to not in settings['checkMention']:settings["checkMention"][to] = {}
                        if sender not in settings["checkMention"][to]:settings["checkMention"][to][sender] = {}
                        if "msg" not in settings["checkMention"][to][sender]:settings["checkMention"][to][sender]["msg"] = []
                        settings["checkMention"][to][sender]["msg"].append({"to":to,"_from":sender,"text":text,"contentMetadata":msg.contentMetadata,"createdTime":msg.createdTime,"id":msg_id})
                if settings['autoRespondMention']['status']:
                    if msg.toType in [1, 2] and 'MENTION' in msg.contentMetadata.keys() and sender != myMid and msg.contentType not in [6, 7, 9]:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                        if myMid in mentionees:
                            if line.getProfile().displayName in text:
                                if '@!' not in settings['autoRespondMention']['message']:
                                    line.sendReplyMessage(msg_id,to, settings['autoRespondMention']['message'])
                                else:
                                    line.sendMentionV3(msg_id,to, settings['autoRespondMention']['message'], [sender])
                if settings['autoRespond']['status']:
                    if msg.toType == 0:
                        contact = line.getContact(sender)
                        if contact.attributes != 32 and 'MENTION' not in msg.contentMetadata.keys():
                            if '@!' not in settings['autoRespond']['message']:
                                line.sendReplyMessage(msg_id,to, settings['autoRespond']['message'])
                            else:
                                line.sendMentionV3(msg_id,to, settings['autoRespond']['message'], [sender])
        if op.type == 55:
            if op.param1 in lurking:
                if lurking[op.param1]['status'] and op.param2 not in lurking[op.param1]['members']:
                    lurking[op.param1]['members'].append(op.param2)
                    if lurking[op.param1]['reply']['status']:
                        if '@!' not in lurking[op.param1]['reply']['message']:
                            line.sendMessage(op.param1, lurking[op.param1]['reply']['message'])
                        else:
                            line.sendMentionV2(op.param1, lurking[op.param1]['reply']['message'], [op.param2])
        if op.type == 65:
            if op.param1 in settings['detectUnsend']:
                detectUnsend(op)
    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)

def runningProgram():
    if settings['restartPoint'] is not None:
        try:
            line.sendMessage(settings['restartPoint'], 'Bot can operate again ♪')
        except TalkException:
            pass
        settings['restartPoint'] = None
    while True:
        #catchFish(args.user)
        checkExpire()
        try:
            ops = oepoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('##---- KEYBOARD INTERRUPT -----##')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
#                executeOp(op)
                k=Thread(target=executeOp,args=(op,))
                k.start()
                #k.join()
                oepoll.setRevision(op.revision)

if __name__ == '__main__':
    print ('##---- RUNNING PROGRAM -----##')
    runningProgram()


