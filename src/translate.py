import json
import subprocess
from typing import Optional


def en2ru(word) -> Optional[str]:
    cmd = ('sdcv', '-u', 'LingvoUniversal (En-Ru)', '-j', '-e', word, '--utf8-output')
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if not stderr:
        data = stdout.decode('utf-8')
        translation = json.loads(data)
        if translation:
            definition = translation[0]['definition']
            return definition
