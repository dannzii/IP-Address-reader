import smtplib
from PyEamilUserCred import userCred

class SmptMail:
	userCred = userCred
	mailServer = "smtp.gmail.com:587"
	msg = ""
	to = []

	def __init__(self, to, msg):
		self.to = to
		self.msg = msg

	def getMsg(self):
		return self.msg

	def getRecipients(self):
		return self.to

	def setMsg(self, msg):
		
		if isinstance(msg, str):
			self.msg = msg

	def setRecipients(self, recip):

		if isinstance(recip, list):
			self.to = recip

	def addRecipient(self, recip):
		
		if isinstance(recip, str):
			self.to.append(recip)

	def send(self):
		pass


