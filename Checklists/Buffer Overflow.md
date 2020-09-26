# Buffer Overflow

1. Identify vulnerable portion of program
2. Fuzz the application figure out when it will crash
3. Find the offset
```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l NUMBER
```
```
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l NUMBER -q ADDRESS
```
4. Overwrite EIP
5. Find Bad Characters
6. Find JMP ESP
7. Generate shellcode
