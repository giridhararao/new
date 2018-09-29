import smtplib
import email.utils
from celery import Celery
from celery.schedules import crontab
app = Celery()
def send_mail(subject, msg):
    try:
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('www.giridhararao@gmail.com','Nanileela')
        message='Subject:{}\n\n{}',format(subject, msg)
        mail.sendmail('www.giridhararao@gmail.com', 'www.giridhararao@gmail.com', message)
        mail.quit()
        print("email send sucess")
    except:
        print("email failed to send")
subject="hai "
msg=" message send through python "
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        send_mail(subject, msg),
        )
