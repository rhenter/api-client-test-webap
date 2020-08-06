import codecs
import os
import re

from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)


def get_version():
    current_version = ''
    changes = os.path.join(BASE_DIR, "CHANGES.rst")
    pattern = r'^(?P<version>[0-9]+.[0-9]+(.[0-9]+)?)'
    with codecs.open(changes, encoding='utf-8') as changes:
        for line in changes:
            match = re.match(pattern, line)
            if match:
                current_version = match.group("version")
                break
    return current_version or '0.1.0'
