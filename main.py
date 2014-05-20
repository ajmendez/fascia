import calendar
from datetime import datetime

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput


class MainScreen(GridLayout):
  def __init__(self, **kwargs):
    self
  # def calendar(self):
  #   for 

class FasciaApp(App):
  
  def build(self):
    today = datetime.now()
    cal = calendar.Calendar(calendar.SUNDAY)
    layout = GridLayout(cols=7, size_hint=(0.5,0.5))
    
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
    
    self.layout = layout
    self.title = '%d: %s'%(today.year, calendar.month_abbr[today.month])
    
    self.popup = Popup(title='%d: %s'%(today.year,
                                       calendar.month_abbr[today.month]),
                       content = layout,
                       size_hint = (0.535,0.535),
                       # size_hint = (None,None),
                       # size = (400,500)
                       # size = layout.size,
                       )
    self.popup.open()
    return layout

if __name__ == '__main__':
    FasciaApp().run()