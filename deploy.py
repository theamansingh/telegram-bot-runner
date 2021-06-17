from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    reply = None
    if msg is not None:
        try:
            if int(msg):
                import requests
                api_key = os.environ['api_key']
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json', 'Api-Key': api_key}
                response = requests.post('http://be.redash.box8.co.in/api/queries/'+str(
                    msg)+'/refresh?api_key='+str(api_key), headers=headers)
                reply = str(msg)+' triggered successfully.'
        except:
            reply = 'Please enter a valid query number!'

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
                from_ = item["message"]["from"]["id"]
                reply = make_reply(message)
                bot.send_message(reply, from_)
            except:
                message = None
