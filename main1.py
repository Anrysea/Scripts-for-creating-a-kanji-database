import re
import openai
import csv
import os

history = []


openai.api_key = "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"

start_string = "Переведи с японского на русский, как для словаря, но не слишком объёмно -\n"
#start_responce = "Понял вас. Пришлите мне кандзи, и я предоставлю примеры в указанном вами формате, я обязательно буду следовать установленным правилам"

def get_part_after_dash(s):
    parts = s.split('-')
    return parts[-1].strip() if len(parts) > 1 else s
def get_words_after_dash(input_string):
    words = input_string.split('\n')
    words1 = [get_part_after_dash(s) for s in words]
    return '\ '.join(word.strip() for word in words1)

#history.append({"role": "assistant", "content": start_responce})

def generate_response(string):
        request_string = start_string + string.replace(",", "\n" )
        print(request_string)
        history.append({"role": "user", "content": request_string})
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=history
        )
        print(completion.choices[0].message.content.strip())
        return completion.choices[0].message.content.strip()





with open('translate1.txt', 'a', encoding='utf-8') as outfile:
    response = generate_response("門,専門,部門,名門,正門,校門,門出,入門する,破門する")
    print(response)
    outfile.write(str(response) + '\n')
    history = []
