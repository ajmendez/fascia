''' A simple website handler 
2014 May : Mendez
'''
import sys
import time
try:
    import androidhelper as android
except:
    import android


def main():
    '''Loads the website view'''
    droid = android.Android()
    try:
        droid.webViewShow('http://hydrogen.bluenet.mooo.com:5555')
        while True:
            time.sleep(10)
            sys.stdout.write('.')
            sys.stdout.flush()
    except KeyboardInterrupt:
        print 'Bye!'
    except:
        raise
    finally:
        # well this is suppose to be here, but alas --- NOPE
        # droid.dismiss()
        pass



if __name__ == '__main__':
    main()