import requests
import settings

def get_bot_updates(limit, offset):
	par = {'limit' : limit, 'offset' : offset}
	url = 'https://api.telegram.org/'+settings.BOT_API+'/getUpdates'
	result = requests.get(url, params = par)
	decoded = result.json()
	return  decoded['result']

result = get_bot_updates(5,0)
first_update = result[0]
text_inc = result[0]['message']['text']
update_id = result[0]['update_id']
chat_id = result[0]['message']['chat']['id']
for item in result:
	text_inc = item ['message']['text']
	update_id = item['update_id']
	print(update_id, text_inc)

new_offset = update_id+1

def sendmsg (chat_id, text_out):
	par = {'chat_id' : chat_id, 'text' : text_out}
	url = 'https://api.telegram.org/'+settings.BOT_API+'/sendMessage'
	result = requests.get(url, params = par)
	decoded = result.json()
	return decoded

def get_rate(currency):
	rate_url = 'https://api.cryptonator.com/api/ticker'+currency+'-rur'
	result = requests.get(rate_url)
	decoded = result.json()
	rate = float(decoded['ticker']['price'])
	return rate

while True:
	get_bot_updates(5, new_offset)
	if text_inc == '/start':
		sendmsg(chat_id,
					'Привет! Выбери команду для получения текущей котировки:\n /btc — Выводит актуальный курс биткоина \n /eth — Выводит актуальный курс эфириума ')
	elif text_inc == '/eth':
		sendmsg(chat_id, get_rate('/eth'))
	elif text_inc == '/btc':
		sendmsg(chat_id, get_rate('/btc'))
	else:
		sendmsg(chat_id, 'Не понял, набери команду еще раз')






