import matplotlib.pyplot as plt
import numpy as np

# Create some random data
x = np.random.rand(50)
y = np.random.rand(50)

# Create a scatter plot with different colors and sizes for each point
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Add a colorbar to show the range of colors
colorbar = plt.colorbar()
colorbar.set_label('Color')

# Add titles and labels
plt.title("Random Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add a tooltip with the coordinates of each point
tooltip = mpld3.plugins.PointLabelTooltip(plt.scatter(x, y))
mpld3.plugins.connect(plt.gcf(), tooltip)

# Save the plot as an HTML file
mpld3.save_html(plt.gcf(), "scatter_plot.html")

