import requests
from vkbottle.user import User, Message
from threading import Thread
import time
import json

class Timer:
    def __init__(self):
        self.timer = [False, 0]
        Thread(target=self.run).start()
        
    def is_timing(self):
        return not self.timer[0]

    def add_timer(self, time):
        self.timer[0] = True
        self.timer[1] = time
        
    def run(self):
        while True:
            if self.timer == [True, 0]:
                self.timer = [False, 0]
            elif self.timer[0]:
                self.timer[1] -= 1
                time.sleep(1)
            else:
                time.sleep(5)

def get_cmds():
    with open('commands.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def add_cmd(key, value):
    cmds = get_cmds()
    cmds['commands'][key] = value
    return save(cmds)

def delete_cmd(key):
    cmds = get_cmds()
    del cmds['commands'][key]
    return save(cmds)

def save(dict_):
    with open('commands.json', 'w', encoding='utf-8') as f:
        json.dump(dict_, f, indent=4)
    return True


s = requests.Session()
s.proxies = {
    'http': 'zippo656476_gmail_co:c591284f2d@212.162.132.50:30001',
    'https': 'zippo656476_gmail_co:c591284f2d@212.162.132.50:30001'
}

s.headers.update({
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'locale=ru; LLXR=1605458623; LLXUR=e91f7024e6aa; _ym_d=1605458622; _ym_uid=1605458622684117545; s1=jCRt3rNjqagAs33KiLjSuaHS09Rl6DfzPfuH4Oe6kH6M45OFdAJvehzpslMVQms51EkEVR9k6tomGk1xUfc9HOIf6Kke8P5qZTvMn8g7RTG%2BcYoBF3NA%2F5QwUjuxrfSr2rGdqzLUHwO3DgbGIuS4ld7ZSUC3csRNO0JGlROcb7S1b5DmWROEgd2wT75GPGlCczNAXcncYVL8n8m6o%2BRvdTHDZ4O6es2SiOsTEi%2FH9l0y%2FPqkCvm4eku2xKRkn7%2Fh2xh6tYXE06cs2FHZREdSp1j5Sqn4Mum%2BGJsClSeJq88hAtmT%2ByN6HBi%2FiivJ27tJpqtgq5fQug0u0rCmj7WcliXgEaQnPJdAkVkLNcJsQVw7E81NP4sS4gzEuWYXKwFVrpsYx0L9LoS0CLCItfL5daMvjRK4BqmDsQaQ2lcIUcYb1S%2FaOuUNYYiFkUqxd9ucCl7%2FhWNyf6ZCWZPKReJPbPu4fs%2BHxd%2BxRjkaNVCPs1HWa1o9ATLFhUiUyWYFWEFnVFklkbWk%2BFHVfIb3uBBBCaCp8c1WLmDTIUCG%2F1RzLdUPTCvhFl8Wdh7LkBOfsw5eva6Ct%2FR%2FOvT4glgJncIFyfdRH1z%2BvV2feUpvb6kpgUPWkbLrAbPBB5XrxP97tBetsZF2WIyXmwLgKTyezkZ1Sv%2FJRM%2FzEFOON%2FhSUhO9Ak0%3D; s2=jsKtcQYiEVLvFmOdv%2FJ2hPlCfheaIWaZq8b8n0n2voU0zGdMWP9FfK%2F%2FWhqdemWyXk47PhKxLhqD0WnYB5MrX0MMdTK%2FraRto%2BGv3I5s0FJxGihJvr075Ne3Qbo2QeAXAOkXqLacbaHBZZm9WGGeqMm0vuF9pb9i85bVY8dxypSM1%2BXkOesNvoKjHNXVXjBkzD8r7CxqA3s1CNwZzBigZh4bDSgIThAyx9JIcQWL3HmOO3TpJJZEPLVqEGKOiW3U%2BOE1zQsuW%2FHRoIqV8cuSn3ydB6oS9zu5dnA2I1j7h9qPSAC9xo%2FQn0LFQ93kY58JnmEiZnNQzAg1oIksYALVmqMliTY4NEyTRgOFQEh%2F85MqcO6egP9%2FzxqRp8F9KuPAqd57pxYkCHiIUxOKEHDhccSomR8Fwq94iw3MccumVWfhNcro9%2FnqCoZDIM2sDOdDDSe5PuGriNLE%2ByqO%2FDPSBlN8tjr1btgcm9mAVkLe4E8G5MJXgd6yBlQ35pK%2BvLxHpEg0iYKZ61kOkcT8WuJoLLbTMKOZSMfQJxcaoJwecC4CsQ0yFDv9qBjWSbCHH5%2Fl6hMHVInLuYI%2BjwUCPbr6NVkC%2BOKMGjXA9So2nt74F1Wzmw4x0rNSKGoHNMp7WrttcYbB84b4jtw55eK02sv09QJHQD2uPzNdlfrJm2DjEZg%3D; wallet_check_hide_zero=1; cf_clearance=1cfdf5745f8dbe327a36759056ad15a037a3edde-1609077207-0-250; Rfr=https%3A%2F%2Fyobit.net%2Fru%2Fhistory%2Fwithdrawals%2FRUR; __cfduid=db8e768fe64bac3bb3fd99fbab5e665151610739532; marketbase=rur; PHPSESSID=7f0s2ts2f5ft21ol32vm78re3h; locale_chat=en; 0051fa699827131ac08c1c74ab46953f=1',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
})

user = User("e6aac850546c977a725fff0ee6b5ad38287bf3288e552d0d9be6bda24c2b55f72cbdc66cf7404e7108c12")
timer = Timer()

coms = [
    'кнопка работает?',
    'чек кнопку', 
    'чек кнопка', 
    'чек пул', 
    'пул пополнили?', 
    'чек бтк', 
    'бтк?', 
    'мать бигпата шлюха',
    'ктт скам',
    '!пул',
    'пул',
    'пипи пупу чек',
    'чек',
    'иди нахуй'
]

@user.on.message_handler(text="<item>")
async def wrapper(ans: Message, item: str):
    if timer.is_timing():
        if item.lower() in coms:
            timer.add_timer(15)
            csrf = '3fb6fd3efed395b0ddf7c586e51eadc78bda86e1ba29db4ce8dded9378308a37c3b3454a04bd67767454d2e202750d48a21b6222ed67642d13991a4db8ed7664'
            data = {
                'action': 'send_earned_to_balance',
                'csrf_token': csrf
            }
            req = s.post('https://yobit.net/ajax/system_affiliate_signature4.php', data).text[:-1]
            return f"Ответ сервера: {req}"
        
        elif 'add cmd' in item.lower():
            timer.add_timer(6)
            try:
                key = item.split(':')[1].strip().lower()
                value = item.split(':')[2].strip()
                if "!" in value:
                    return "! - Запрещенный символ"
                if len(value) > 250:
                    return "сообщение содержит больше 250 слов, такое нам не нада"
                return str(add_cmd(key, value))
            except Exception as e:
                return e
            
        elif 'del cmd' in item.lower():
            timer.add_timer(6)
            try:
                key = item.split(':')[1].strip()
                return str(delete_cmd(key))
            except Exception as e:
                return e
        
        elif item.lower() in get_cmds()['commands'].keys():
            timer.add_timer(6)
            cm = get_cmds()['commands'][item.lower()]
            return cm
            

user.run_polling()