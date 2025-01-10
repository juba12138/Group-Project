from openai import OpenAI
from typing import List, Dict

def aichat(user_input):
    client = OpenAI(
        base_url='http://10.15.88.73:5035/v1',
        api_key='ollama',  # required but ignored
    )

    messages : List[Dict] = [
        {"role": "system", "content": 
    "Your name is Paimon, and your identity is a guide who leads the protagonist trapped here to escape. In the conversation, you need to convey the following key information. First, this is a maze, and you must find a door if you want to escape from here. Second, there is more than one door, and choosing the wrong door may lead to failure of the challenge. Third, there will be enemies chasing you during the action. They ignore the terrain and are numerous, so don't let them catch you.If the interlocutor wants to start the challenge, you can tell him that he only needs to find the NPC at the rear. Your response should be within 30 words."}
    ]

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama3.2",      
        messages=messages,    # a list of dictionary contains all chat dictionary
    )

    # 提取模型回复
    assistant_reply = response.choices[0].message.content
    # 将助手回复添加到对话历史
    messages.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply