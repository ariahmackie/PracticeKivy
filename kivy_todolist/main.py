# need for MainApp
from kivymd.app import MDApp

# you need these imports for a dialog box
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.picker import MDDatePicker
from datetime import datetime


#imports for listing tasks after you create them
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox


# Code for Dialog Box
class DialogContent(MDBoxLayout):
    '''Opens a dialog box that gets the task from the user '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # set the date_text label to today's date when user first opens dialog box
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

    def show_date_picker(self):
        '''opens the date picker '''
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        '''reformats data '''
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)


# classes list item with checkbox
class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Custom List Item '''

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk

    def mark(self, check, the_list_item):
        '''mark the task as complete or incomplete'''
        if check.active == True:
            # add strikethrough to the text if the checkbox is active
            the_list_item.text = '[s]'+ the_list_item.text+ '[/s]'
        else:
            # remove strikethrough
            pass

    def delete_item(self, the_list_item):
        '''Delete the task '''
        self.parent.remove_widget(the_list_item)

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom Left Container '''



class MainApp(MDApp):
    task_list_dialog = None
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"

    #add for making task dialog boxes
    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
            title = "Create Task",
            type='custom',
            content_cls=DialogContent()
            )
        self.task_list_dialog.open()

    def add_task(self, task, task_date):
        '''Add task to the list of tasks '''
        print(task.text, task_date)
        self.roots.ids['container'].add_widget(ListItemWithCheckbox(text='[b]'+task.text+'[/b]', secondary_text=task_date))
        task.text = ''

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    def add_task(self, task, task_date):
        '''add task to list of tasks'''
        print(task.text, task_date)
        task.text = ''


if __name__ == '__main__':
    app = MainApp()
    app.run()
