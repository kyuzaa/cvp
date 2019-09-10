# -*- coding: utf-8 -*-

from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol
from akad import AuthService, TalkService
from akad.ttypes import LoginRequest

import json, requests, time

class LineConfig(object):
	LINE_HOST_DOMAIN 			= 'https://gd2.line.naver.jp'
	LINE_LOGIN_QUERY_PATH 		= '/api/v4p/rs'
	LINE_AUTH_QUERY_PATH 		= '/api/v4/TalkService.do'
	LINE_API_QUERY_PATH_FIR 	= '/S4'
	LINE_CERTIFICATE_PATH 		= '/Q'

	APP_VERSION = {
		'DESKTOPWIN': '5.9.0',
		'DESKTOPMAC': '5.9.0',
		'IOSIPAD': '8.14.2',
		'CHROMEOS': '2.1.5',
		'WIN10': '5.5.5',
		'DEFAULT': '8.11.0'
	}

	APP_TYPE    = 'IOSIPAD'
	APP_VER     = APP_VERSION[APP_TYPE] if APP_TYPE in APP_VERSION else APP_VERSION['DEFAULT']
	CARRIER     = '51089, 1-0'
	SYSTEM_NAME = 'Kyuza SB'
	SYSTEM_VER  = '5.0.1'
	IP_ADDR     = '8.8.8.8'

	def __init__(self, appName=None):
		if appName:
			self.APP_TYPE = appName
			self.APP_VER = self.APP_VERSION[self.APP_TYPE] if self.APP_TYPE in self.APP_VERSION else self.APP_VERSION['DEFAULT']
		self.APP_NAME = '{}\t{}\t{}\t{}'.format(self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
		self.USER_AGENT = 'Line/%s' % self.APP_VER
		
class LineAuth(object):
	authToken 	= ""
	
	def __init__(self, appName=None, systemName=None):
		self.config = LineConfig()
		self.session = requests.session()
		if appName is None:
			appName = self.config.APP_NAME
		if systemName is None:
			systemName = self.config.SYSTEM_NAME
		self.appName = LineConfig(appName).APP_NAME
		self.systemName = systemName
		self.userAgent = self.config.USER_AGENT
		self.headers = {
			'User-Agent': self.userAgent,
			'X-Line-Application': self.appName,
			'x-lal': 'ja-US_US',
		}

	def createTransport(self, path=None, update_headers=None, service=None):
		self.headers['x-lpqs'] = path
		if(update_headers is not None):
			self.headers.update(update_headers)
		transport 	= THttpClient.THttpClient(self.config.LINE_HOST_DOMAIN + path)
		transport.setCustomHeaders(self.headers)
		protocol 	= TCompactProtocol.TCompactProtocol(transport)
		client 		= service(protocol)
		return client

	def getJson(self, url, headers=None):
		if headers is None:
			return json.loads(self.session.get(url).text)
		else:
			return json.loads(self.session.get(url, headers=headers).text)

	def generateQrCode(self):
		client = self.createTransport(self.config.LINE_AUTH_QUERY_PATH, None, TalkService.Client)
		qrCode = client.getAuthQrcode(keepLoggedIn=1, systemName=self.systemName)
		result = 'line://au/q/{}'.format(qrCode.verifier)
		self.headers['X-Line-Access'] = qrCode.verifier
		return result

	def generateAuthToken(self):
		self.headers['x-lpqs'] = self.config.LINE_AUTH_QUERY_PATH
		getAccessKey = self.getJson(self.config.LINE_HOST_DOMAIN + self.config.LINE_CERTIFICATE_PATH, self.headers)
		client = self.createTransport(self.config.LINE_LOGIN_QUERY_PATH, None, AuthService.Client)
		req = LoginRequest()
		req.type = 1
		req.verifier = self.headers['X-Line-Access']
		req.e2eeVersion = 1
		res = client.loginZ(req)
		client = self.createTransport(self.config.LINE_API_QUERY_PATH_FIR, {'X-Line-Access':res.authToken}, TalkService.Client)
		self.authToken = res.authToken
		result = str(self.authToken)
		return result
