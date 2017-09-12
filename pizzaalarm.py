Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
from urllib2 import urlopen
from time import sleep
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
# Phone Numbers go into this dictionary
phoneNumberList = {"Tomi Getselev": 01638850610, "Jakob Hollweck": 015229603683}
 
while True:
    for key, value in phoneNumberList.iteritems():
        pNumber = str(value)
        pNumberName = str(key)
        url = "https://order.dominos.com/orderstorage/GetTrackerData?Phone=" + pNumber
        thepage = urllib.urlopen(url)
        soup = BeautifulSoup(thepage, "xml")
        print "Checking " + pNumberName + "..."
        
        # Gatekeeper XML tag stored in a variable
        orderStatuses = str(soup.find('OrderStatuses').text)
        
        # Gatekeeper
        if orderStatuses != "":
            
            # Pertinent XML tags stored in variables
            startTime = str(soup.find('StartTime').text)
            orderDescription = str(soup.find('OrderDescription').text)
            print orderDescription
            # vvv Put additional XML tags code in between these comments vvv
 
 
            # ^^^ Put additional XML tags code in between these comments ^^^
          
            # Email code
            sender = 'pythonpizzaalerts@gmail.com'
            # Put your email address in between the '' for receiver
            receiver = 'jakob.hollweck@gmail.com'
 
            # Structuring the email
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = "Your friend ordered pizza!"
 
            # The email message
            body = str(pNumberName) + " ordered " + orderDescription + " at " + startTime
            msg.attach(MIMEText(body, 'plain'))
 
            # Access sender email and send email
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('pythonpizzaalerts@gmail.com','pizzatothepy')
            message = msg.as_string()
            mail.sendmail(sender, receiver, message)
            mail.close()
 
        else:
            pass
            print "No order for " + pNumberName
 
        # Be cautious if you edit this sleep statement. 
        # Do not reduce the wait time too much. 
        # We don't want to accidentally DDoS Dominos :)
        sleep(60)
