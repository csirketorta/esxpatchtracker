import feedparser
import ssl
import smtplib
from pathlib import Path

# emailhez szukseges valtozok
sender_email = ""  # kuldo e-mail cime
sender_password = ""  # kuldo jelszava
receiver_email = ""  # Kinek menjen az e-mail?

esx70feed = feedparser.parse("https://esxi-patches.v-front.de/atom/ESXi-7.0.0.xml")
entry70 = esx70feed.entries[0]
esx67feed = feedparser.parse("https://esxi-patches.v-front.de/atom/ESXi-6.7.0.xml")
entry67 = esx67feed.entries[0]
esx65feed = feedparser.parse("https://esxi-patches.v-front.de/atom/ESXi-6.5.0.xml")
entry65 = esx65feed.entries[0]

try:
    f = open('esx70.txt')
    f.close()
except FileNotFoundError:
    fle = Path('esx70.txt')
    fle.touch(exist_ok=True)

try:
    f = open('esx67.txt')
    f.close()
except FileNotFoundError:
    fle = Path('esx67.txt')
    fle.touch(exist_ok=True)

try:
    f = open('esx65.txt')
    f.close()
except FileNotFoundError:
    fle = Path('esx65.txt')
    fle.touch(exist_ok=True)

f_orig70 = open("esx70.txt", "r")
old_log70 = (f_orig70.read())
f_orig70.close()

f_orig67 = open("esx67.txt", "r")
old_log67 = (f_orig67.read())
f_orig67.close()

f_orig65 = open("esx65.txt", "r")
old_log65 = (f_orig65.read())
f_orig65.close()

if entry70.title != old_log70:
    f_new = open("esx70.txt", "w")
    f_new.write(entry70.title)
    f_new.close()
    message = """Subject: """ + entry70.title + """\n""" + """{}""".format(entry70.summary_detail.value).replace(
        "<a href=\"", "").replace("\">link</a>.", "").replace("follow the", "please check this: ")

    with smtplib.SMTP_SSL("server", 465, ssl.create_default_context()) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

if entry67.title != old_log67:
    f_new = open("esx67.txt", "w")
    f_new.write(entry67.title)
    f_new.close()
    message = """Subject: """ + entry67.title + """\n""" + """{}""".format(entry67.summary_detail.value).replace(
        "<a href=\"", "").replace("\">link</a>.", "").replace("follow the", "please check this: ")

    with smtplib.SMTP_SSL("server", 465, ssl.create_default_context()) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

if entry65.title != old_log65:
    f_new = open("esx65.txt", "w")
    f_new.write(entry65.title)
    f_new.close()
    message = """Subject: """ + entry65.title + """\n""" + """{}""".format(entry65.summary_detail.value).replace(
        "<a href=\"", "").replace("\">link</a>.", "").replace("follow the", "please check this: ")

    with smtplib.SMTP_SSL("server", 465, ssl.create_default_context()) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

exit()
