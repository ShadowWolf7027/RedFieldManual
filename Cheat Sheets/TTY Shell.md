# Spawn TTY Shell

Create fully interactive shell from nc
```bash
nc -lnvp 4444

python -c 'import pty;pty.spawn("bash")' # or whatever you use below to spawn a bash shell

^Z # Ctrl-Z

stty raw -echo

fg
```

```python
python -c 'import pty; pty.spawn("/bin/bash")'
```
```bash
echo os.system('/bin/bash')
```
```
/bin/sh -i
```
```perl
perl —e 'exec "/bin/sh";'

or

perl: exec "/bin/sh";
```
```ruby
ruby: exec "/bin/sh"
```
```lua
lua: os.execute('/bin/sh')
```

Within vi
```
:!bash

or

:set shell=/bin/bash:shell
```