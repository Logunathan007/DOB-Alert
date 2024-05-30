import requests
from math import *
import smtplib
from email.message import EmailMessage
import datetime as dt

def msg_format(ls):
    empty_str = ""
    print(ls);
    for i in ls:
        name = "Name: "+i[0]+"\n";
        dob = "DOB: "+i[1]+"\n";
        info = ""
        for j in i[2].split("_"):
            info+= (j+"\n")
        print("info is ",info)

        if(i[3] == 0):
            soon = "Today is her Birth Day.\n\n"
        else:
            soon = str(i[3])+" days to go.\n\n"
        empty_str += (name+dob+info+soon);
    return empty_str

def sender(msg):
    TOKEN = "6584489985:AAHtVcDn9e6HSb4b6ZPON4xhCrEcmGWmRNo"
    chat_id = "-1001919957179"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    d = dict(requests.get(url).json())
    print(d)
    if(d['ok']):
        return "Message successfully send"
    else:
        return "Message not send"

def runer(datas):
    em_list=[]
    todays = dt.datetime.now()
    for i in datas:
        v = i[1]
        vv = v.split('/')
        if len(vv) == 1:
            vv = v.split('.')
        if len(vv) == 1:
            vv = v.split('-')
        if len(vv) == 1:
            vv = v.split('\\')
        if len(vv) == 1:
            vv = v.split(' ')
        #print (vv)
        #print(i[2])
        try:
            date = dt.date(day=int(vv[0]),month=int(vv[1]),year=todays.year) - dt.date(todays.year,todays.month,todays.day)
        except ValueError:
            date = dt.date(day=int(vv[1]),month=int(vv[0]),year=todays.year) - dt.date(todays.year,todays.month,todays.day)
        #print(i[0] ,'+' ,date.days)
        if (date.days == 30) or (date.days <= 7 and  date.days >= 0):
            i.append(date.days)
            em_list.append(i)
            #sender(k,v,date.days)
    return em_list





