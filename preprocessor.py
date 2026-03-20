
import re
import pandas as pd
def preprocess(data):
    # Normalize hidden unicode spaces from WhatsApp exports.
    data = data.replace('\u202f', ' ').replace('\u200e', '').replace('\ufeff', '')

    # Supports formats like: 17/02/24, 1:42 am - Name: Message
    pattern = r'^\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s?[apAP][mM])?\s-\s'
    messages = re.split(pattern, data, flags=re.MULTILINE)[1:]
    dates = re.findall(pattern, data, flags=re.MULTILINE)

    cleaned_dates = [re.sub(r'\s-\s$', '', date).strip() for date in dates]

    
    df=pd.DataFrame({'user_message':messages,'message_date':cleaned_dates})
    df['message_date']=pd.to_datetime(df['message_date'],dayfirst=True,errors='coerce')
    df=df.dropna(subset=['message_date'])
    df.rename(columns={'message_date':'date'},inplace=True)#inplace=true ni likhogi toh change ni krega
    users=[]
    messages=[]
    for message in df['user_message']:
        entry=re.split(r'([\w\W]+?):\s',message)
        if entry[1:]:#user name
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user']=users
    df['message']=messages
    df.drop(columns=['user_message'],inplace=True)
    df['year']=df['date'].dt.year
    df['month']=df['date'].dt.month_name()
    df['day']=df['date'].dt.day
    df['hour']=df['date'].dt.hour
    df['min']=df['date'].dt.minute
    df['month_num']=df['date'].dt.month
    df['only_date']=df['date'].dt.date
    df['day_name']=df['date'].dt.day_name()

    period=[]
    for hour in df['hour']:
        if hour==23:
            period.append(str(hour)+"-"+str("00"))
        elif hour==0:
            period.append(str("00")+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    df['period']=period
    return df