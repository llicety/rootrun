#!/usr/bin/python
# coding=utf-8

import sys
import dbus

def rootRun(cmd):
    try:
        bus = dbus.SystemBus()
    except:
        print "could not initiate system dbus"
        return False

    try:   
        obj = bus.get_object("zx.rootrun.rootrundaemon","/")
        iface = dbus.Interface(obj, "zx.rootrun.rootrundaemon.interface")

        res = iface.rootRun(cmd)
        print "pid:",res[0]
        if res[1] != "":
            print "----------------stdout---------------------"
            for strs in res[1].split("\n"):
                print strs
        if res[2] != "":
            print ""
            print "----------------stderr---------------------"
            for strs in res[2].split("\n"):
                print str(strs)
        if res[3] != "":
            print ""
            print "----------------exception---------------------"       
            for strs in res[3].split("\n"):
                print str(strs)                    
        
    except dbus.DBusException, e:
        print "dbus.DBusException error",e

    
if __name__ == "__main__":
    cmd = sys.argv[1:]
    cmd = " ".join(cmd)
    print "执行命令:",cmd 

    rootRun(cmd)

