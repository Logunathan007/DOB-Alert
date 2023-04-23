
from math import *
import smtplib
from email.message import EmailMessage
import datetime as dt

def declist(dec):
    key = list(map(int,input("Enter the Key: ").strip().split()))
    ans = []
    a = 0;
    bas = 0;
    sub2 = []
    for i in dec:
        sub = list();
        for j in i:
            sub.append(chr(j//key[a]))
            a+=1;
            if(a >= len(key)):
                a=0;
        if(bas == 4):
            ans.append(sub2);
            sub2 = list();
            bas = 0
        sub2.append(''.join(sub));
        bas+=1;
    return ans;

def msg_format(ls):
    empty_str = ''
    if ls == []:
        val = """
                <p style="font-weight: bold;" "font-size: 40px;">
                    <h1>No Alert for Today</h1>
                </p><br><hr>
        """
        empty_str += val
    else:
        for i in ls:
            if (i[4] == 30) or (i[4] <= 7 and i[4] >= 1):
                val = """
                <p style="font-weight: bold;" "font-size: 40px;">
                    <h1>{name}</h1> <h2>({branch} {depa})</h2> Has born in {dob} & his birthday is soon in {days} days.
                </p><br><hr>
                """.format(name=i[0],branch=i[1],depa=i[2],dob=i[3], days=i[4])
                empty_str += val
            if i[4] == 0:
                val = """
                <p style="font-weight: bold;" "font-size: 40px;">
                    <h1>{name}</h1> <h2>({branch} {depa})</h2> Has born in {dob} & Today is her Birthday.
                </p><br><hr>
                """.format(name = i[0],branch=i[1],depa=i[2],dob=i[3])
                empty_str += val
    html_val = """
    <html>
    <body>
    {}
    </body>
    </html>
    """.format(empty_str)
    return empty_str

def sender(html_val):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_id = "botbot20032003@gmail.com"
    receiver_id = "jlogu2003@gmail.com"
    password = "lhso drne dmoq qevr"
    msg = EmailMessage()
    msg['Subject'] = 'DOB-Alert'
    msg['From'] = sender_id
    msg['To'] = receiver_id
    msg.set_content(html_val,subtype='html')
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_id, password)
        server.sendmail(sender_id, receiver_id, msg.as_string())
        server.quit()
    return "Message successfully send"

def runer(datas):
    em_list=[]
    todays = dt.datetime.now()
    for i in datas:
        v = i[3]
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
