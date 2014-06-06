import sys
import calendar
from datetime import datetime

# from kivy.config import Config
# Config.set('graphics', 'width', '600')
# Config.set('graphics', 'height', '1024')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout



Builder.load_string('''
#:kivy 1.6
[SideBar@BoxLayout]:
    content: content
    orientation: 'vertical'
    size_hint: ctx.size_hint if hasattr(ctx, 'size_hint') else (1, 1)
    Image:
        source: ctx.image
        size_hint: (1, None)
        height: root.width
    GridLayout:
        cols: 2
        # just add a id that can be accessed later on
        id: content

<Root>:
    Button:
        center_x: root.center_x
        text: 'press to add_widgets'
        size_hint: .2, .2
        on_press:
            root.load_content(sb.content)
            #
            # what comes after `:` is basically normal python code
            #sb.content.clear_widgets()
            # however using a callback that you can control in python
            # gives you more control
            #root.load_content(sb.content)
    SideBar:
        id: sb
        size_hint: .2, 1
        image: 'data/images/image-loading.gif'
''')



class Root(FloatLayout):
  shown = False
  def load_content(self, content):
    if self.shown:
      self.shown = False
      content.clear_widgets()
    else:
      self.shown = True
      for but in range(20):
        content.add_widget(Button(text=str(but)))

class MyApp(App):
  def build(self):
    return Root()




class MainScreen(GridLayout):
  # def __init__(self, **kwargs):
  #   Logger.info('xxx: %s'%kwargs)
  #   kwargs.setdefault('cols', 1)
  #   kwargs.setdefault('rows', 5)
  #   # kwargs.setdefault('size_hint',(1,1))
  #   super(GridLayout, self).__init__(**kwargs)
  # 
  # def load_content(self, content):
  #   content.add_widget(Button(text='test'))
  #   content.add_widget(Button(text='test2'))
  pass

class FasciaApp(App):
  title = 'Fascia'
  
  def build(self):
    return MainScreen()



class CalendarApp(App):
  def build(self):
    today = datetime.now()
    cal = calendar.Calendar(calendar.SUNDAY)
    layout = GridLayout(cols=7)
    
    for iweek,week in enumerate(cal.monthdays2calendar(today.year, today.month)):
      if iweek == 0: # label each col by the day
        for _,wkday in week:
          label = Label(text='[b]%s[/b]'%calendar.day_abbr[wkday], markup=True)
          layout.add_widget(label)
      
      for day, wkday in week: # add each day
        if day != 0:
          button = Button(text='%d'%day)
        else:
          button = Label(text = '')
        layout.add_widget(button)
    return layout

if __name__ == '__main__':
    MyApp().run()
    # FasciaApp().run()
    # CalendarApp().run()