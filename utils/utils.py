import re

regexp = re.compile(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}')
emailexp = re.compile(r'[a-zA-Z]{1,}@[a-zA-Z]{1,}.com', flags=re.I)
phoneexp = re.compile(r'[0-9]{4,5}-[0-9]{4}')


def cpfValidation(value):
    if len(regexp.findall(value)) == 1:
        return True
    else:
        return False

def emailValidation(value):
    if len(emailexp.findall(value)) == 1:
        return True
    else:
        return False

def phoneValidation(value):
    if len(phoneexp.findall(value)) == 1:
        return True
    else:
        return False