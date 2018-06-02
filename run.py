import urllib2
from Smtp.UserCred import *
from Smtp.SmtpMail import *

# Gets ip address
ip = urllib2.urlopen('http://ip.42.pl/raw').read()


#reads user Credencials
userDetails = ["", ""]

#creating mail user
user = UserCredClass(userDetails[0], userDetails[1])

# Creating smtp mail class and setup
mail = SmtpMailClass(user, "smtp.gmail.com", 587)
mail.addRecipient("")
mail.setSubject("IP Address")
mail.setMsg("IP: "+ip)
mail.send()
