from bokeh.plotting import figure, show, output_file
import pandas

df=pandas.DataFrame(columns=["X", "Y"])
df["X"]=[0,1,2,3,4,5,6]
df["Y"]=[0,1,4,9,16,25,36]

p= figure(plot_width=500, plot_height=500, title="Squared Numbers", background_fill_color="grey", background_fill_alpha=0.1)

p.circle(df["X"], df["Y"], size=[i*2 for i in [1,4,8,12,16,20,24]], color="red", alpha=0.5)
output_file("scatter_charts.html")
show(p)

