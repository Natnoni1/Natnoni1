login = input('Введите логин: ')
if login == '0':
    print('Логин правильный. Спасибо за покупку программы!')
else:
    print('Пароль не верный')
print('███╗░░██╗░█████╗░████████╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗')
print('████╗░██║██╔══██╗╚══██╔══╝██║░░██║██╔══██╗██╔══██╗██║░██╔╝')
print('██╔██╗██║███████║░░░██║░░░███████║███████║██║░░╚═╝█████═╝░')
print('██║╚████║██╔══██║░░░██║░░░██╔══██║██╔══██║██║░░██╗██╔═██╗░')
print('██║░╚███║██║░░██║░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗')
print('╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝')
print('Version: 0.1')
print('1. Пробив по номеру (скоро)  |   2. Пробив по IP')
print('3. Пробив по номеру машины |  4. Пробив по ФИО(скоро)')
print('6. Получить базы данных')
print('5. Помощь')
select = input('Выберите пункт: ')

if select == '2':
    getIP = input("[+] Введите IP ")
    url = "https://ipinfo.io/" + getIP + "/json"
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        print("\nIp не найдено!\n")
    infoList = json.load(getInfo)
    def whoisIPinfo(ip):
        try:
            myComand = "whois " + getIP
            whoisInfo = os.popen(myComand).read()
            return whoisInfo
        except:
            return "\n [!] -- Error -- [!] \n"
    print("IP: ", infoList["ip"])
    print("Город: ", infoList["city"])
    print("Регион: ", infoList["region"])
    print("Страна: ", infoList["country"])
    print("Провайдер: ", infoList["hostname"])
    time.sleep(1)
    print('')
if select == '3':
    print('Для пробива перейдите в бота:')
    print('https://t.me/BotAvinfo_bot')
if select == '5':
    print('Вы в меню помощи:')
    print('Привет. Это бесплатная версия программы для доксинга от тгк @natnoni')
    print('Все предельно просто! Выбераешь номер ультитлы и программа выдаст тебе инфу. Пользуйтесь ')
if select == '6':
    print('Для установки баз данных перейдите по ссылке:')
    print('https://drive.google.com/drive/folders/1YZYHUV3f8sgW6PQOqjCWmNWvKIxC5u0D?usp=sharing')
