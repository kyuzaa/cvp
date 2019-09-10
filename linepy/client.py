# -*- coding: utf-8 -*-
from akad.ttypes import Message
from .auth import Auth
from .models import Models
from .talk import Talk
from .call import Call
from .timeline import Timeline
from .server import Server
from .shop import Shop

class LINE(Auth, Models, Talk, Call, Timeline, Shop):

    def __init__(self, idOrAuthToken=None, passwd=None, appType=None):
        self.certificate = None
        self.systemName = None
        self.appType = appType
        self.appName = None
        self.showQr = None
        self.channelId = None
        self.keepLoggedIn = True
        self.customThrift = True
        Auth.__init__(self)
        if not (idOrAuthToken or idOrAuthToken and passwd):
            self.loginWithQrCode()
        if idOrAuthToken and passwd:
            self.loginWithCredential(idOrAuthToken, passwd)
        elif idOrAuthToken and not passwd:
            self.loginWithAuthToken(idOrAuthToken)
        self.__initAll()

    def __initAll(self):

        self.profile    = self.talk.getProfile()
        self.userTicket = self.generateUserTicket()
        self.groups     = self.talk.getGroupIdsJoined()

        Models.__init__(self)
        Talk.__init__(self)
        Call.__init__(self)
        Timeline.__init__(self)
        Shop.__init__(self)
