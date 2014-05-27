'''
@copyright: Hariharan Srinath, 2012
@license: This work is licensed under a Creative Commons Attribution 3.0 Unported License. http://creativecommons.org/licenses/by/3.0/
'''

xmldata = """<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:background="#66000000"
    android:paddingLeft="16dp"
    android:paddingRight="16dp" >
    <TextView
        android:id="@+id/name"
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="Demo"
        android:textSize="32dp"
        android:gravity="center"
        />
    <TextView
        android:id="@+id/time"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_below="@id/name"
        android:layout_alignParentLeft="true"
        android:layout_toLeftOf="@+id/weather" 
        android:text="Time"
        />
    <WebView
            android:id="@+id/web" 
            android:layout_width="400dp"
            android:layout_height="400dp"
            />
</RelativeLayout>"""


other = '''


    <TextView
        android:id="@+id/weather"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_below="@id/name"
        android:layout_toRightOf="@+id/time" 
        android:text="Weather"
        />
    <TextView
        android:id="@+id/network"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_below="@id/name"
        android:layout_toRightOf="@+id/weather" 
        android:layout_alignParentRight="true"
        android:text="Network"
        />
    <TextView
            android:layout_width="fill_parent"
            android:layout_height="0px"
            android:textSize="16dp"
            android:text="FullScreenWrapper2 Demo"
            android:textColor="#ffffffff"
            android:layout_weight="20"
            android:gravity="center"/>
    <TextView
            android:layout_width="fill_parent"
            android:layout_height="0px"
            android:background="#ff000000"
            android:id="@+id/txt_colorbox" 
            android:layout_weight="60"
            android:gravity="center"/>
    <LinearLayout
        android:layout_width="fill_parent"
        android:layout_height="0px"
        android:orientation="horizontal"
        android:layout_weight="20">
        <Button
            android:layout_width="fill_parent"
            android:layout_height="fill_parent"
            android:background="#ff66a3d2"
            android:text = "Random Color"
            android:layout_weight="1"
            android:id="@+id/but_change" 
            android:textSize="14dp"
            android:gravity="center"/>
        <Button
            android:layout_width="fill_parent"
            android:layout_height="fill_parent"
            android:background="#ff25567b"
            android:layout_weight="1"
            android:text = "Exit"
            android:textSize="14dp"
            android:id="@+id/but_exit" 
            android:gravity="center"/>
    </LinearLayout>



'''

import android, random
from fullscreenwrapper2 import *

class DemoLayout(Layout):
    def __init__(self, droid):
        self.droid = droid
        super(DemoLayout,self).__init__(xmldata,"FullScreenWrapper Demo")
        
    def on_show(self):
        self.add_event(key_EventHandler(handler_function=self.close_app))
        # add image 
        
        # Works
        # self.droid.fullSetProperty("image","src",
        #                            "@android:drawable/star_big_off")
        # fails 
        # self.droid.fullSetProperty("image","src",
        #                            "http://i.imgur.com/JwvgFcx.gif") 

        #
        # self.droid.fullSetProperty("web","src",
        #                            "file:///sdcard/Pictures/JwvgFcx.gif") 
        
        
        
        # self.views.but_change.add_event(click_EventHandler(self.views.but_change, self.change_color))
        # self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.close_app))
        
    def on_close(self):
        pass
    
    def close_app(self,view,event):
        FullScreenWrapper2App.exit_FullScreenWrapper2App()

    def change_color(self,view, event):
        colorvalue = "#ff"+self.get_rand_hex_byte()+self.get_rand_hex_byte()+self.get_rand_hex_byte()
        # self.views.txt_colorbox.background=colorvalue
    
    def get_rand_hex_byte(self):
        j = random.randint(0,255)
        hexrep = hex(j)[2:]
        if(len(hexrep)==1):
            hexrep = '0'+hexrep   
        return hexrep 

if __name__ == '__main__':
    droid = android.Android()
    random.seed()
    try:
    # if True:
        FullScreenWrapper2App.initialize(droid)
        FullScreenWrapper2App.show_layout(DemoLayout(droid))
        FullScreenWrapper2App.eventloop()
    except KeyboardInterrupt:
        print 'Done'
    except:
        raise
    finally:
        FullScreenWrapper2App.exit_FullScreenWrapper2App()