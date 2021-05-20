import os
import sys
import ssl


# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# context.load_cert_chain('C:\Apache24\conf\microbakd.pem', 'C:\Apache24\conf\microbakd.pem')

# activate virtualenv
PROJECT = "dash-flask"

# i'm using py -m venv venv
# @see: https://modwsgi.readthedocs.io/en/develop/user-guides/virtual-environments.html
# @see: https://stackoverflow.com/questions/25020451/no-activate-this-py-file-in-venv-pyvenv



activate_this = os.path.join('C:\\Users\\madisa\\projects', PROJECT, 'venv\\Scripts\\activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

BASE_DIR = os.path.join(os.path.dirname(__file__))
BASE_ROOT_DIR = BASE_DIR[:-9]
print(BASE_ROOT_DIR)
print(BASE_DIR)
if BASE_DIR not in sys.path:

    sys.path.append(BASE_DIR)
    sys.path.append(BASE_ROOT_DIR)

from flask_app.app import app

application = app
