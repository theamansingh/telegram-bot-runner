from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    reply = None
    if msg is not None:
        try:
            if int(msg):
                import requests
                api_key = 'UAs8NFbd45nvhzTdkHBBCdUKAKRHbF58eSUHfUEI'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json', 'Api-Key': api_key}
                response = requests.post('http://be.redash.box8.co.in/api/queries/'+str(
                    msg)+'/refresh?api_key=UAs8NFbd45nvhzTdkHBBCdUKAKRHbF58eSUHfUEI', headers=headers)
                reply = response.text
        except:
            reply = 'Please enter query number'

    return reply


update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
