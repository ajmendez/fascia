fascia
======

A dashboard system.



* Start the ssh server on the device.  This should be automatic with sshdroid.  Sometimes this dies, but it is generally running

* Start the scripting service to access over IP:PORT=5500 :

  * am start -a com.googlecode.android_scripting.action.LAUNCH_SERVER -n com.googlecode.android_scripting/.activity.ScriptingLayerServiceLauncher --ez com.googlecode.android_scripting.extra.USE_PUBLIC_IP true --ei com.googlecode.android_scripting.extra.USE_SERVICE_PORT 5500

* now setup the environmental variables:

  * # . setup.sh

* can run different programs now. e.g., 

  * python demo2.py
