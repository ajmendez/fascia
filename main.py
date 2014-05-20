import calendar
from datetime import datetime

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput


# class MainScreen(FloatLayout):
#   def calendar(self):
#     for 

class FasciaApp(App):
  
  def build(self):
    today = datetime.now()
    cal = calendar.Calendar(calendar.SUNDAY)
    layout = GridLayout(cols=7)
    
    for iweek,week in enumerate(cal.monthdays2calendar(today.year, today.month)):
      # label each col by the day
      if iweek == 0:
        for _,wkday in week:
          label = Label(text='[b]%s[/b]'%calendar.day_abbr[wkday])
          layout.add_widget(label)
      
      # add each day
      for day, wkday in week:
        if day != 0:
          button = Button(text='%d'%day)
        else:
          button = Button(text = '')
        
        layout.add_widget(button)
      
      # add as a popup
      
      self.popup = Popup(title='%d: %s'%(today.year,
                                         calendar.month_abbr[today.month]),
                         content = layout,
                         size_hint = (None,None), 
                         size = (400,500)
                         )
>       # self.popup.open()
    # return MainScreen()

if __name__ == '__main__':
    FasciaApp().run()