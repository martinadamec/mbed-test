#!/usr/bin/env python

import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

class SendEmail:

	subject = None
	text = None
	send_from = "noreply@kuleuven.be"

	def __init__(self, subject = None, text = None):
		self.subject = subject
		self.text = text

	def setSubject(self, subject):
		self.subject = subject

	def setText(self, text):
		self.text = text

	def addXlsxFile(self, msg, filename, path):
		part = MIMEBase('application', "octet-stream")
		part.set_payload(open(path, "rb").read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="' + filename + '"')
		msg.attach(part)

	def send(self, send_to):
		msg = MIMEMultipart()
		msg['From'] = self.send_from
		msg['To'] = send_to
		msg['Date'] = formatdate(localtime = True)
		msg['Subject'] = self.subject
		msg.attach(MIMEText(self.text))

		# Add attachemnts
		self.addFiles(msg)

		# establish SMTP
		smtp = self.establishSMTP()
		smtp.sendmail(self.send_from, send_to, msg.as_string())
		smtp.quit()

	def establishSMTP(self):
		return smtplib.SMTP("localhost")
