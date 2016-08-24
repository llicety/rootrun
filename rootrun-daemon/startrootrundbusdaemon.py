#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import signal
import dbus
import dbus.mainloop.glib
from gi.repository import GObject
from rootrundbusdaemon import RootRunDbusService

if __name__ == '__main__':
    os.environ["TERM"] = "xterm"
    os.environ["PATH"] = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/X11R6/bin"

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    GObject.threads_init()
    mainloop = GObject.MainLoop()
    signal.signal(signal.SIGINT, lambda : mainloop.quit())
    RootRunDbusService(dbus.SystemBus(), mainloop)
    mainloop.run()
