from flask import Flask, render_template
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
#from bokeh.io import curdoc

import json
import os
import datetime


app = Flask(__name__, template_folder=".")

@app.route("/")
def home():
    content = json.load(open("data.json"))
    plot = figure(title="Line graph", x_axis_label="Time",x_axis_type='datetime', y_axis_label="Value", plot_width=800, plot_height=250,sizing_mode='stretch_width')
    #curdoc().theme = 'dark_minimal'
    #curdoc().add_root(plot)
    plot.toolbar.logo = None
    #plot.toolbar_location = None
    plot.line(
        [datetime.datetime.fromtimestamp(int(dt)//1000) for dt in content["nav"]["datetime"]],
        [float(x) for x in content["nav"]["values"]],
        line_width=2)
    scripts, div = components(plot)
    content["script"] = scripts
    content["div"] = div

    entries = []
    for filename in os.listdir("blog_entries/"):
        with open("blog_entries/" + filename, "r") as f:
            date = datetime.datetime.strptime(filename.replace(".txt", ""), "%Y-%m-%d").date()
            entries.append((date, f.read()))
    entries.sort()
    entries = entries[::-1]

    content["blogs"] = []
    for entry in entries:
        blog = {"date":entry[0]}
        text = entry[1]
        blog["title"] = text.split("\n")[0]
        blog["body"] = "\n".join(text.split("\n")[2:])
        content["blogs"].append(blog)

    return render_template("base.html", **content)

if __name__ == "__main__":
    app.run(debug=True)