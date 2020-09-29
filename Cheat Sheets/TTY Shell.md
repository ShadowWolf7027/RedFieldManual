# Spawn TTY Shell

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