# Install the dependencies
# pip install ipywidgets

import ipywidgets as widgets
from IPython.display import display

count = 0
label = widgets.Label(value="Count: 0")
button = widgets.Button(description="+ click")

def increase(b):
    global count
    count += 1
    label.value = f"Count: {count}"

button.on_click(increase)

display(button, label)