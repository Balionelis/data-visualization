import matplotlib.pyplot as plt
import numpy as np
import mpld3
import webbrowser

# Name of the .html file
filename = 'scatter_plot.html'

# Create some random data
x = np.random.rand(10)
y = np.random.rand(10)
indices = np.arange(10)  # Define an array of indices

# Create a scatter plot with different colors and sizes for each point
colors = np.random.rand(10)
sizes = 1000 * np.random.rand(10)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Add a colorbar to show the range of colors
colorbar = plt.colorbar()
colorbar.set_label('Color')

# Add titles and labels
plt.title("Random Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add a tooltip with the coordinates and indices of each point
tooltip_text = ["x: {:0.2f}, y: {:0.2f}, index: {}".format(x[i], y[i], indices[i]) for i in range(len(x))]
tooltip = mpld3.plugins.PointHTMLTooltip(plt.scatter(x, y, c=colors, s=sizes, alpha=0.5), tooltip_text)
mpld3.plugins.connect(plt.gcf(), tooltip)

# Save the plot as an HTML file
mpld3.save_html(plt.gcf(), "scatter_plot.html")

# Automatically opens the file
webbrowser.open_new_tab(filename)
