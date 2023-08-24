import asyncio
import aiohttp
import random

async def send_requests(url, port, time, num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = []
        counter = 0
        for _ in range(num_requests):
            headers = {'User-Agent': generate_user_agent()}
            tasks.append(session.get(f"{url}:{port}", headers=headers, timeout=time))
            counter += 1
        await asyncio.gather(*tasks)
        print(f"Отправлено {counter} запросов")

def generate_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
    ]
    return random.choice(user_agents)

choice = input("Выберите метод отправки запросов (1 - по ссылке, 2 - по IP-адресу): ")
if choice == "1":
    url = input("Введите URL вашего сайта: ")
elif choice == "2":
    ip = input("Введите IP-адрес вашего сервера: ")
else:
    print("Неправильный выбор метода отправки запросов")

port = input("Введите порт: ")
time = int(input("Введите время ожидания в секундах: "))
num_requests = int(input("Введите количество запросов: "))

loop = asyncio.get_event_loop()
if choice == "1":
    loop.run_until_complete(send_requests(url, port, time, num_requests))
elif choice == "2":
    loop.run_until_complete(send_requests(ip, port, time, num_requests))
else:
    print("Неправильный выбор метода отправки запросов")