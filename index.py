import matplotlib.pyplot as plt
from math import log, factorial as fct

class Bigo():
    def __init__(self):
        #Create a figure and axes.
        self.fig, self.axes = plt.subplots(figsize = (10, 10))
        #Create a range for x values to process.
        self.x = range(1, 102, 10)
        # All needed data for graphs. Just to keep code cleaner
        self.graph_data = [{"y" : [i / i for i in self.x], "color" : "#3868A2", "label" : "O(1)"},
                           {"y" : [log(i) for i in self.x], "color" : "#9F2F2C", "label" : "O(logn)"},
                           {"y" : self.x, "color" : "#769831", "label" : "O(n)"},
                           {"y" : [i*log(i) for i in self.x], "color" : "#583A7C", "label" : "O(nlogn)"},
                           {"y" : [i**2 for i in self.x], "color" : "#2388A3", "label" : "O(n^2)"},
                           {"y" : [2**i for i in self.x], "color" : "#D67423", "label" : "O(2^n)"},
                           {"y" : [fct(i) for i in self.x], "color" : "#89A1C9", "label" : "O(n!)"}]
        #Set limits, Y for keep figure similar to the model.
    def set_limits(self):
        self.axes.set_xlim(0, 100)
        self.axes.set_ylim(0, 1000)
        #Set labels of X and Y axes and Graph.
    def set_labels(self):
        self.axes.set_title("Big-O Complexity")
        self.axes.set_xlabel("Elements")
        self.axes.set_ylabel("Operations")
        #Draw graphs using data we declared inside our constructor.
    def draw_graphs(self):
        #Loop all over the data and place datas into where they belong.
        for data in self.graph_data:
            self.axes.plot(self.x, data["y"], color = data["color"], label = data["label"])
        #Indicating graphs with names-to-colors
    def show_tbl(self):
        self.axes.legend()
        #Draw plot
    def draw_plot(self):
        plt.show()        

#Initialize our class
bigo = Bigo()
#Set limits for axes
bigo.set_limits()
#Set labels for axes
bigo.set_labels()
#Draw graphs and show tables
bigo.draw_graphs()
bigo.show_tbl()
#Draw plot
bigo.draw_plot()
