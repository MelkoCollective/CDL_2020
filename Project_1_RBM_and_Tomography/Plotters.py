import matplotlib.pyplot as plt
from IPython import display

class XYPlotter():
    def __init__(self, href=None, title="", x_label="", y_label=""):
        """
        params:
          - href - where to put a horizontal reference line
          - title - the plot title
          - x_label - label for x-axis
          - y_label - label for y-axis
        """ 
        self.x_series = []
        self.y_series = []
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.href = href

    def update(self, x, y, redraw_fig=True):
        """
        updates the state of the plotter object and redraws the plot by default
        set redraw_fig to False if you just want to update the series data
         without updating the plot
        """
        self._update_series_data(x, y)
        if redraw_fig:
            self._update_plot()

    def _update_series_data(self, x, y):
        self.x_series.append(x)
        self.y_series.append(y)

    def _update_plot(self):
        display.clear_output(wait=True)
        plt.plot(self.x_series, self.y_series)
        if self.href is not None:
            plt.plot(self.x_series, [self.href]*len(self.x_series), 'r--')
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()