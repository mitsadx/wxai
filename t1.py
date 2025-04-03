from wxauto import WeChat
import time
from openai import OpenAI

client = OpenAI(api_key="<your api key>", base_url="https://api.deepseek.com")
wx = WeChat()
listen_list = ['','']
sender_list = ['','','','']

for i in listen_list:
    wx.AddListenChat(who=i, savepic=True)
flag = False
wait = 1
while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who              # 获取聊天窗口名（人或群名）
        one_msgs = msgs.get(chat)   # 获取消息内容
        for msg in one_msgs:
            msgtype = msg.type       # 获取消息类型
            content = msg.content  
            sender = msg.sender                    
            print(f'【{who}】：{content}')
            if content == 'on':
                flag = True
                chat.SendMsg('ciallo~')
                continue
            if content == 'off':
                flag = False
                chat.SendMsg('Bye~')
                continue
            if msgtype == 'friend' and flag:
                if sender == sender_list[1]:
                    messages4=[{"role": "system", "content": "你的名字是tincl，尽力帮助"}]
                    messages4.append({"role": "user", "content": content})
                    response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages4,
                    temperature = 1.3,
                    stream=False
                    )
                    messages1.append(response.choices[0].message)
                    chat.SendMsg(response.choices[0].message.content)
                if sender == sender_list[2]:
                    messages1=[{"role": "system", "content": "你尽力帮助"}]
                    messages1.append({"role": "user", "content": content})
                    response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages1,
                    temperature = 1.3,
                    stream=False
                    )
                    messages1.append(response.choices[0].message)
                    chat.SendMsg(response.choices[0].message.content)
                if sender == sender_list[3]:
                    messages2=[{"role": "system", "content": "尽力帮助"}]
                    messages2.append({"role": "user", "content": content})
                    response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages2,
                    temperature = 1.3,
                    stream=False
                    )
                    messages2.append(response.choices[0].message)
                    chat.SendMsg(response.choices[0].message.content)
                if sender == sender_list[4]:
                    messages3=[{"role": "system", "content": "尽力帮助"}]
                    messages3.append({"role": "user", "content": content})
                    response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages3,
                    temperature = 1.3,
                    stream=False
                    )
                    messages3.append(response.choices[0].message)
                    chat.SendMsg(response.choices[0].message.content)
    time.sleep(wait)