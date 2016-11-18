#!/usr/bin/python

import wx
import random

APP_SIZE_X = 215
APP_SIZE_Y = 120

class MyButtons(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(APP_SIZE_X, APP_SIZE_Y))

        wx.Button(self, 1, 'Open Cover', (15, 25))
        wx.Button(self, 2, 'Close Cover', (15, 50))
        wx.Button(self, 3, 'Exit', (115, 35))

        self.Bind(wx.EVT_BUTTON, self.OnOpen, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=2)
        self.Bind(wx.EVT_BUTTON, self.OnExit, id=3)

        self.Centre()
        self.ShowModal()
        self.Destroy()

    def OnOpen(self, event):
        def OnRun(self,event):
         path = "open.py"
         subprocess.Popen(path)

    def OnClose(self, event):
        def OnRun(self,event):
         path = "close.py"
         subprocess.Popen(path)

    def OnExit(self, event):
        self.Close(True)

app = wx.App(0)
MyButtons(None, -1, 'Dust Cover v0.1')
app.MainLoop()
