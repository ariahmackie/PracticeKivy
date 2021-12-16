from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


# create a dropdown with button
dropdown = DropDown()
for index in range(10):
    # specify height manually when you add a widget
    # you disable the size_hint_y so that dropdown can
    # extend as far as it needs .

    btn = Button(text = 'Value %d' % index, size_hint_y=None, height = 44)
    # for each button attach a callback that will call the select() method
    # on the dropdown. We'll pass the text of the button as the data of the
    # selection.

    btn.bind(on_release=lambda bt: dropdown.select(btn.text))

    #Then add the button inside the dropdown
    dropdown.add_widget(btn)

    #create a big main button
    mainbutton = Button(text='Hello', size_hint=(None, None))

    #show the dropdown menu when the main button is released
    # note: all the bind() calls pass the instance of the caller (here, the
    # mainbutton instanc) as the first argument of the callback (here,
    # dropdown.open.).
    mainbutton.bind(on_release=dropdown.open)

    # listen for the selection in the dropdown list and
    # assign the data to the button text.

    dropdown.bind(on_select = lambda instance : xsetattr(mainbutton, 'text',))
    xrunTouchApp(mainbutton)
