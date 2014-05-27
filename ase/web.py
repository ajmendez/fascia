import android
from fullscreenwrapper2 import _internal_exit_signal


def basic():
    droid = android.Android()
    droid.webViewShow('http://google.com')
    # droid.fullDismiss()

def force():
    droid = android.Android()
    droid.webViewShow('file:///sdcard/Pictures/JwvgFcx.gif')
    while True:
        event = droid.eventWait().result
    
        if event['name'] == 'kill':
            sys.exit()
        elif event['name'] == 'line':
            line_handler(event['data'])


if __name__ == '__main__':
    basic()
    # force()
    
