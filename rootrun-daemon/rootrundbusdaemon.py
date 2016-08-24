# -*- coding: utf-8 -*-
import dbus 
import dbus.service 
import dbus.mainloop.glib
import sys
import subprocess
from socket import *              # portable socket interface plus constants


class RootRunDbusService(dbus.service.Object): 

    def __init__ (self, bus, mainloop): 

        self.bus = bus 
        self.bus_name = dbus.service.BusName("zx.rootrun.rootrundaemon", bus=bus) 
        dbus.service.Object.__init__(self, self.bus_name, "/") 
        self.mainloop = mainloop 
         
		    
    @dbus.service.method("zx.rootrun.rootrundaemon.interface", in_signature='s', out_signature='as', sender_keyword='sender') 
    def rootRun(self, cmd, sender=None):
        mycmd = cmd
        out = ""
        error = ""
        exception = ""
        try:
        	p = subprocess.Popen(mycmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        	p.wait()
        	out = p.stdout.read().strip()
        	error = p.stderr.read().strip() 
        except Exception, e:
            exception = str(e)
        return [str(p.pid),out,error,exception]
        
    @dbus.service.method("zx.rootrun.rootrundaemon.interface", in_signature='', out_signature='', sender_keyword='sender')
    def exit(self,sender=None):
        self.mainloop.quit()

        
