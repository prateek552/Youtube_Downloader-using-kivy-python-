# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:04:51 2018

@author: Heller
"""
import kivy
kivy.require('1.0.10')
import pafy
from kivy.lang import Builder
from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.image import AsyncImage,Image
Config.window_icon = "download.png"
global url
class Download(Widget):
    textin=ObjectProperty()
    global url
    global s
    url= StringProperty("")
    pass 

    def downbut(self):
        global url
        global s
        url =self.textin.text 
        self.box = PageLayout()
        video=pafy.new(url)
        self.box.add_widget(Label(text='Swipe Left To See The Description')) 
        self.box.add_widget(Image(source='a.png'))
        self.box.add_widget(Button(text='Title              '+str(video.title)+'\nRating           '+str(video.rating)+'\nViews           '+str(video.viewcount)+'\nAuthor          '+str(video.author)+'\nLength          '+str(video.length)+' seconds\nCategory       '+str(video.category),background_color=(1.0, 1.0, 0.0, 1))) 
        self.box.add_widget(Button(text='Yes:-This is my video',background_color=(0.81, 0.27, 0.33, 1),on_press= lambda *args: self.popup.dismiss()))
        self.box.add_widget(Button(text='No:-This is not my video',background_color=(1.0, 0.0, 0.0, 1.0),on_press=lambda *args:App.get_running_app().stop()))
        self.popup = Popup(title='Discription of the video', content=self.box,
              auto_dismiss=False)
        self.popup.open()
        

class Desc(Widget):
    global url
    a=10
    def description(self):
        print (str(url))
        lambda *args:self.add_widget(Label(text="kkk"))
    def __init__(self, **kwargs):
        super(Desc, self).__init__(**kwargs)
        pass

    def downvid(self):
        video=pafy.new(url)
        best=video.getbestvideo()
        best.download("C:/")
        popup2=Popup(title='Notification',content=Label(text='Download Complete'),size=(400,400),auto_dismiss=True)
        popup2.open()
        
    def downaud(self):
        video=pafy.new(url)
        print (video)
        best=video.getbestaudio()
        best.download("C:/")
        popup2=Popup(title='Notification',content=Label(text='Download Complete'),size=(400,400),auto_dismiss=True)
        popup2.open()
    
    
class MainScreen(Screen):
    pass
class Second(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass
presentation=Builder.load_file("TestApp.kv")
class TestApp(App):
    def build(self):
        return presentation


if __name__ == '__main__':
    TestApp().run()