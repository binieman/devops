"""
This is a test file.The original idea is on automateControl.py

"""

from os import system
import libtmux
from subprocess import PIPE, run,Popen

def output(command):
    result = Popen(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    output = ''
    while True:
        inchar = result.stdout.read(1)
        output+=inchar
        if inchar: #neither empty string nor None
            print(str(inchar), end='') #or end=None to flush immediately
        else:
            print('') #flush for implicit line-buffering
            break
    return output


def tmux(command):
    return output('tmux %s' % command)


def tmux_shell(command):
    tmux('send-keys "%s" "C-m"' % command)




server = libtmux.Server()
session = server.find_where({"session_name": "vagrant_test"})

session = server.new_session(session_name="vagrant_test", kill_session=True, attach=False)
window = session.new_window(attach=True, window_name="vagrant_test")
tmux('select-window -t 0')
print(tmux_shell('vagrant up'))
pane1 = window.attached_pane
pane2 = window.split_window(vertical=True)
pane3 = window.split_window(vertical=True)
window.select_layout('even-horizontal')
pane1.send_keys('vagrant ssh VM1')
pane2.send_keys('vagrant ssh VM2')
pane3.send_keys('vagrant ssh VM3')
server.attach_session(target_session="vagrant_test")
