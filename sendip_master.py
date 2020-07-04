# This program waits until the network is up, get's the IP address of the Raspberry PI and
# emails it to you. This is written in Python 3.


# Required Python 3 modules
import smtplib
import subprocess
import urllib.request
import time

# Configuration parameters. Since we put the password for the email account in
# the program is why we use a throw away gmail account.
# Configure the following 3 lines as needed for your istallation.
gmail_user = "YOUR_GMAIL_USERNAME@gmail.com"
gmail_password = "YOUR_GMAIL_PASSWORD"
to = ['YOUR_EMAIL@nku.edu','EMAIL2@SOMEWHERE.NET']

# This makes sure the network is up by trying to access google.com via http. If it fails
# it waits 30 seconds and trys again. This is an infinite loop. It will never exit if the network
# doesn't come up.

while True:
	try:
		urllib.request.urlopen("http://www.google.com").close()
	except urllib.request.URLError:
		print("Network not up yet")
		time.sleep(30)
	else:
		print("Network connected")
		break

# Get the IP address, hostname and create the email message parameters.
subject = 'My Raspberry PI IP Address'
sent_from = gmail_user
ip = subprocess.getoutput('hostname -I')
hostname = subprocess.getoutput('hostname')
print(ip)
tostr = ", ".join(to)
body = "The IP address of the Raspberry PI is: " + ip + " its hostname is " + hostname

# Create the email message.
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, tostr, subject, body)

# Try and send it. It will print out an error message if it can't be sent. This is
# most likely a firewall issue.

try:
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.ehlo()
	server.login(gmail_user, gmail_password)
	server.sendmail(sent_from, to, email_text)
	server.close()
	print("Email sent!")
except:
	print("Something went wrong")

