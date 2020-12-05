#IP & URL Logger by Goxome
# Subscribe Our YouTube Channel & All

#modules required
import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

#COLORS USED
red = '\033[31m'        # Red Light
yellow = '\033[93m'        # Yellow Light
lgreen = '\033[92m'        # Green Light
clear = '\033[0m'         # Clear Color
bold = '\033[01m'        # Bold Color
cyan = '\033[96m'        # Cyan Color Light
Black = '\033[0;30m'       # Black Light
Green ="\033[0;32m"        # Green Dark
Blue ="\033[0;34m"         # Blue Light
BBlue ="\033[1;34m"        # Blue Dark
Purple ="\033[0;35m"       # Purple Light
White ="\[\033[0;37m\]"        # White

#TITLE
print (White+bold+" \n\n  <---(( << 𝔾𝕠𝕩𝕠𝕞𝕖 𝕆𝕗𝕗𝕚𝕔𝕚𝕒𝕝 - 𝕀ℙ 𝕃𝕠𝕘𝕘𝕖𝕣 >> ))--> \n"+clear)
print (lgreen+"            𝓕𝓸𝓵𝓵𝓸𝔀 𝓾𝓼 𝓸𝓷 𝓪𝓵𝓵 𝓼𝓸𝓬𝓲𝓪𝓵 𝓶𝓮𝓭𝓲𝓪   \n"+clear)

#SHORT INFO
print(BBlue+"\n\n ᴡʜᴀᴛ ɪꜱ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ ᴀɴᴅ ᴜʀʟ?")
print(red+"      <--------------->")
print(Blue+"\n ᴀɴ ɪɴᴛᴇʀɴᴇᴛ ᴘʀᴏᴛᴏᴄᴏʟ ᴀᴅᴅʀᴇꜱꜱ ɪꜱ ᴀ ɴᴜᴍᴇʀɪᴄᴀʟ ʟᴀʙᴇʟ ᴀꜱꜱɪɢɴᴇᴅ ᴛᴏ ᴇᴀᴄʜ ᴅᴇᴠɪᴄᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴀ ᴄᴏᴍᴘᴜᴛᴇʀ ɴᴇᴛᴡᴏʀᴋ ᴛʜᴀᴛ ᴜꜱᴇꜱ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴘʀᴏᴛᴏᴄᴏʟ ꜰᴏʀ ᴄᴏᴍᴍᴜɴɪᴄᴀᴛɪᴏɴ. A Uniform Resource Locator, colloquially termed a web address, is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it.  \n \n ")
print(Purple+"• ɪᴘ ᴀᴅᴅʀᴇꜱꜱ ᴏʀ ᴜʀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴꜱ ɢᴇɴᴇʀᴀᴛᴇᴅ! \n")

#API & TARGET URL
ip = args.target

# URL TARGET
# api = "http://ipinfo.io/json/" #IP-INFO
api = "http://ip-api.com/json/" #IP-API

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[ꜱᴛᴀᴛᴜꜱ]:", data['status'])
        print(red+"<--------------->"+red)
        print (b, "[ᴠɪᴄᴛɪᴍ]:", data['query'])
        print(red+"<--------------->"+red)
        print (a, "[ɪꜱᴘ]:", data['isp'])
        print(red+"<--------------->"+red)
        print (b, "[ᴏʀɢᴀɴɪꜱᴀᴛɪᴏɴ]:", data['org'])
        print(red+"<--------------->"+red)
        print (a, "[ᴄɪᴛʏ]:", data['city'])
        print(red+"<--------------->"+red)
        print (b, "[ʀᴇɢɪᴏɴ]:", data['regionName'])
        print(red+"<--------------->"+red)
        print (a, "[ʟᴏɴɢɪᴛᴜᴅᴇ]:", data['lon'])
        print(red+"<--------------->"+red)
        print (b, "[ʟᴀᴛɪᴛᴜᴅᴇ]:", data['lat'])
        print(red+"<--------------->"+red)
        print (a, "[ᴛɪᴍᴇ ᴢᴏɴᴇ]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (b, "[ᴢɪᴘ ᴄᴏᴅᴇ]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('𝙴𝚡𝚎𝚌𝚞𝚝𝚒𝚘𝚗 𝚃𝚎𝚛𝚖𝚒𝚗𝚊𝚝𝚒𝚗𝚐! [𝚃𝚑𝚊𝚗𝚔𝚜 𝚏𝚘𝚛 𝚄𝚜𝚒𝚗𝚐!],'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+bold+"[~]"+"ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɪɴᴛᴇʀɴᴇᴛ ᴅᴀᴛᴀ ɪꜱ ᴛᴜʀɴᴇᴅ ᴏɴ ᴀɴᴅ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ᴅᴀᴛᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ!"+clear)
sys.exit(1)