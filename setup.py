import os
if os.name == 'nt':
    os.system('pip install pystyle')
    os.system('pip install colorama')
    os.system('pip install math')
else:
    os.system('pip3 install pyintaller')
    os.system('pip3 install colorama')
    os.system('pip3 install math')