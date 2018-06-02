import smtplib
import datetime

class SmtpMailClass:
	userCred = None
	mailServer = None
	msg = ""
	to = []
	subject = ""

	def __init__(self, userCred,location, port):
		self.userCred = userCred
		self.mailServer = smtplib.SMTP(location, port)

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

	def setSubject(self, sub):
		if isinstance(sub,str):
			self.subject = sub

	def send(self):
		user = self.userCred

		try:
			newMsg = "\r\n".join([
					  "From: "+user.email,
					  "To: "+ ", ".join(self.to),
					  "Subject: "+self.subject,
					  "",
					  self.msg])

			self.mailServer.ehlo()
			self.mailServer.starttls()
			self.mailServer.login(user.email, user.password)
			self.mailServer.sendmail(user.email, self.to, newMsg)
			self.mailServer.close()
		except Exception as e:
			
			with open("emailerrorlog.log", "a") as stream:
				stream.write(str(datetime.datetime.now())+"\n")
				print e
				stream.write(str(e))
				stream.write("\n\n")


