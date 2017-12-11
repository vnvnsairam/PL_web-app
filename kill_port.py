import os
import subprocess
import re

ports = ['80']


popen = subprocess.Popen(['netstat', '-lpn'],
                         shell=False,
                         stdout=subprocess.PIPE)
(data, err) = popen.communicate()

pattern = "^tcp.*((?:{0})).* (?P<pid>[0-9]*)/.*$"
pattern = pattern.format(')|(?:'.join(ports))
prog = re.compile(pattern)
for line in data.split('\n'):
    match = re.match(prog, line)
    if match:
        pid = match.group('pid')
        subprocess.Popen(['kill', '-9', pid])