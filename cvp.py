from linepy import *
from akad.ttypes import ChatRoomAnnouncementContents, OpType, MediaType, ContentType, ApplicationType, TalkException, ErrorCode, Message
from threading import Thread
import time, traceback, sys, os, pafy, livejson

watashi = "u5691625e5d4355b730fc3f8f9ebf9874"
token = ""
client = LINE(appType="IOSIPAD")
myMid = client.profile.mid
programStart = time.time()
oepoll = OEPoll(client)
lurking = {}
tmp_text = []
settings = livejson.File("setting.json", True, True, 4)


def logError(error, write=True):
    traceback.print_tb(error.__traceback__)
    print ('++ Error : {error}'.format(error=error))

def reply(msg,text):
    return client.sendReplyMessage(msg.id,msg.to,text)

def restartProgram():
    print ('##----- PROGRAM RESTARTED -----##')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def ProfileChangeDual(msg,link):
    client.sendReplyMessage(msg.id,msg.to," 「 Profile 」\nType: Change Profile Video Picture\nStatus: Downloading....♪")
    try:
        url = link.replace('youtu.be/','youtube.com/watch?v=')
        req = pafy.new(url).streams[-1]
        path = client.downloadFileURL(req.url,saveAs='tmp/video.mp4')
        path2 = client.downloadFileURL('http://dl.profile.line-cdn.net/'+client.profile.pictureStatus,saveAs='tmp/pict.jpg')
        client.updateVideoAndPictureProfile(path2, path)
        reply(msg, " 「 Profile 」\nType: Change Profile Video Picture\nStatus: Profile Video Picture Hasbeen change♪")
    except Exception as e:
        print(traceback.print_exc())
        reply(msg,f" 「 Profile 」\nType: Change Profile Video Picture\nStatus: Error !\nReason: {e}")

def downloadVideoYT(link,saveAs):
    video = pafy.new(link)
    req = video.streams[-1]
    path = client.downloadFileURL(req.url,saveAs=saveAs)
    return saveAs

def executeCmd(msg, text, txt, msg_id, receiver, sender, to):
    #print(to)
    if txt == ".hi":
    	reply(msg,"Hi too !")
    elif txt == ".restart":
        reply(msg,"restart will begin")
        restartProgram()
    elif txt == ".speed":
        start = time.time()
        reply(msg,"Testing ...")
        elapse = time.time() - start
        reply(msg,f"Speed is {elapse} seconds")
    elif txt.startswith(".send"):
        res = text.split(" ")
        if res[1].lower() == "image":
            client.sendImageWithURL(to,res[2])
        if res[1].lower() == "video":
            client.sendVideoWithURL(to,res[2])
    elif txt.startswith(".changedual"):
        if len(text.split(" ")) == 1:
            if txt == ".changedual":
                settings['changePP'] = True
                reply(msg,"Send Image/Video to set up in profile")
        else:
            res = text.split(" ")[1]
            if res.lower() == "pict":
                if msg.relatedMessageId != None:
                    reply(msg,"Downloading ....")
                    try:path = client.downloadObjectMsg(msg.relatedMessageId,saveAs='tmp/pict.jpg')
                    except:return reply(msg,"Failed download !")
                    path2 = client.downloadFileURL('http://dl.profile.line-cdn.net/'+client.profile.pictureStatus+"/vp",saveAs='tmp/video.mp4')
                    client.updateVideoAndPictureProfile(path,path2)
                    reply(msg,"Success change profile picture video !")
                else:
                    settings['changedualPP'] = True
                    reply(msg,"Send image to set up in profile")
            elif res.lower() == "video":
                if msg.relatedMessageId != None:
                    reply(msg,"Downloading ....")
                    try:path = client.downloadObjectMsg(msg.relatedMessageId,saveAs='tmp/video.mp4')
                    except:return reply(msg,"Failed download !")
                    path2 = client.downloadFileURL('http://dl.profile.line-cdn.net/'+client.profile.pictureStatus,saveAs='tmp/picture.jpg')
                    client.updateVideoAndPictureProfile(path2,path)
                    reply(msg,"Success change profile video picture!")
                else:
                    settings['changedualVP'] = True
                    reply(msg,"Send video to set up in profile")
            elif "youtube.com" in res.lower() or "youtu.be" in res.lower():
                if 'youtu.be' in txt:
                    link = res.replace("youtu.be/","youtube.com/watch?v=")
                else:
                    link = res
                ProfileChangeDual(msg,link)
            
    elif txt == ".changepict":
        if msg.relatedMessageId != None:
            reply(msg,"Downloading ....")
            try:path = client.downloadObjectMsg(msg.relatedMessageId,saveAs='tmp/pict.jpg')
            except:return reply(msg,"Failed download !")
            client.updateProfilePicture(path)
            reply(msg,"Success change profile picture !")
        else:
            settings['changeDP'] = True
            reply(msg,"Send image to set up in profile")
    elif txt == ".changecover":
        if msg.relatedMessageId != None:
            reply(msg,"Downloading ....")
            try:path = client.downloadObjectMsg(msg.relatedMessageId,saveAs='tmp/cover.jpg')
            except:return reply(msg,"Failed download !")
            client.updateProfileCover(path)
            reply(msg,"Success change cover picture !")
        else:
            settings['changeCV'] = True
            reply(msg,"Send image to set up in cover")
    elif 'youtube.com' in txt or 'youtu.be' in txt:
        if 'youtu.be' in txt:
            link = text.replace("youtu.be/","youtube.com/watch?v=")
        else:
            link = text
        if settings['changePP'] == True and settings['status'] == 2:
            reply(msg,"Wait i will download it ....")
            path = downloadVideoYT(link,"tmp/video.mp4")
            reply(msg,"Success download, wait to upload to profile")
            client.updateVideoAndPictureProfile("tmp/pict.jpg",path)
            reply(msg,"Success change profile video !")
            settings['changePP'] = False
            settings['status'] = 0


def executeOp(op):
    try:
        #print ('++ Operation : ( %i ) %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            client.findAndAddContactsByMid(op.param1)
            client.sendMentionV2(op.param1,"Thanks for add me as your friend @!", [op.param1])
        if op.type == 25:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            if msg.contentType == 0: #CONTENT TYPE IS TEXT
                try:
                    executeCmd(msg, text, txt, msg_id, receiver, sender, to)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                        reply(msg,'Execute command error `{}`'.format(str(talk_error)))
                        time.sleep(3)
                except Exception as error:
                    traceback.print_tb(error.__traceback__)
                    logError(error)
                    reply(msg,'Execute command error, ' + str(error))
                    time.sleep(3)
            if msg.contentType == 1 and sender == myMid:
                if settings['changedualPP']:
                    reply(msg,"Downloading ....")
                    try:path=client.downloadObjectMsg(msg_id,saveAs='tmp/pict.jpg')
                    except:return reply(msg,"Failed to download the image !, please resend the image")
                    path2 = client.downloadFileURL('http://dl.profile.line-cdn.net/'+client.profile.pictureStatus+"/vp",saveAs='tmp/video.mp4')
                    settings['changedualPP'] = False
                    client.updateVideoAndPictureProfile(path,path2)
                    reply(msg,"Success change profile picture video")
                if settings['changeDP']:
                    reply(msg,"Downloading ....")
                    try:path=client.downloadObjectMsg(msg_id,saveAs='tmp/pict.jpg')
                    except:return reply(msg,"Failed to download the image !, please resend the image")
                    settings['changeDP'] = False
                    client.updateProfilePicture(path)
                    reply(msg,"Success update profile picture")
                if settings['changeCV']:
                    reply(msg,"Downloading ....")
                    try:path=client.downloadObjectMsg(msg_id,saveAs='tmp/cover.jpg')
                    except:return reply(msg,"Failed to download the image !, please resend the image")
                    settings['changeCV'] = False
                    client.updateProfileCover(path)
                    reply(msg,"Success update cover picture")
                if settings['changePP']:
                    if settings['status'] == 0:
                        reply(msg,"Downloading ....")
                        try:path=client.downloadObjectMsg(msg_id,saveAs='tmp/pict.jpg')
                        except Exception as e:print(e);return reply(msg,"Failed to download image !, please resend the image")
                        settings['status'] = 2
                        reply(msg,"Success download the image !, Send a video or link youtube to set up in profile")
                    elif settings['status'] == 1:
                        reply(msg,"Downloading ....")
                        try:path=client.downloadObjectMsg(msg_id,saveAs='tmp/pict.jpg')
                        except Exception as e:print(e);return reply(msg,"Failed to download image !, please resend the image")
                        settings['status'] = 0
                        settings['changePP'] = False
                        client.updateVideoAndPictureProfile(path,"tmp/video.mp4")
                        reply(msg,"Success change profile video !")
            elif msg.contentType == 2 and sender == myMid:
                if settings['changedualVP']:
                    reply(msg,"Downloading ....")
                    try:path=client.downloadObjectMsg(msg_id,saveAs='tmp/video.mp4')
                    except:return reply(msg,"Failed to download the video !, please resend the video")
                    path2 = client.downloadFileURL('http://dl.profile.line-cdn.net/'+client.profile.pictureStatus,saveAs='tmp/pict.jpg')
                    settings['changedualVP'] = False
                    client.updateVideoAndPictureProfile(path2,path)
                    reply(msg,"Success change profile video picture")
                if settings['changePP']:
                    if settings['status'] == 0:
                        reply(msg,"Downloading ....")
                        try:path=client.downloadObjectMsg(msg_id,saveAs='tmp/video.mp4')
                        except Exception as e:print(e);return reply(msg,"Failed to download video !, please resend the video")
                        settings['status'] = 1
                        reply(msg,"Success download the video !, Send a image to set up in profile")
                    elif settings['status'] == 2:
                        reply(msg,"Downloading ....")
                        try:path=client.downloadObjectMsg(msg_id,saveAs='tmp/video.mp4')
                        except Exception as e:print(e);return reply(msg,"Failed to download video !, please resend the video")
                        settings['status'] = 0
                        settings['changePP'] = False
                        client.updateVideoAndPictureProfile("tmp/pict.jpg",path)
                        reply(msg,"Success change profile video !")
    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)

def runningProgram():
    while True:
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
                executeOp(op)
          #      k=Thread(target=executeOp,args=(op,))
            #    k.start()
                #k.join()
                oepoll.setRevision(op.revision)

if __name__ == '__main__':
    print ('##---- RUNNING PROGRAM -----##')
    runningProgram()
