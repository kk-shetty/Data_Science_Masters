# Import necessary modules
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
from bokeh.models.widgets import Slider
from bokeh.io import output_notebook, push_notebook, show

# Output to the notebook
output_notebook()

# Create a data source
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 5, 8, 2, 7], 'size': [10, 15, 20, 25, 30]}
source = ColumnDataSource(data=data)

# Create the plot
plot = figure(width=400, height=400)
plot.circle('x', 'y', size='size', source=source, color='blue', alpha=0.6)

# Create the slider
slider = Slider(start=5, end=50, value=10, step=5, title="Marker Size")

# Create the update function
def update_plot(attrname, old, new):
    # Get the new size value from the slider
    new_size = slider.value
    
    # Update the data source with the new size values
    new_data = dict(data)
    new_data['size'] = [new_size * i for i in data['size']]
    source.data = new_data

# Attach the update function to the slider's 'on_change' event
slider.on_change('value', update_plot)

# Arrange the layout
layout = column(plot, slider)

# Add the layout to the current document
curdoc().add_root(layout)
