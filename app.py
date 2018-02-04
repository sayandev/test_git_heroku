from flask import Flask, render_template
import requests   
import numpy as np
from bokeh.plotting import figure, output_notebook, show
from bokeh import embed
app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<h1>Bokeh plot embeded With Flask Webapp. Data fetched from QUANDL API; moving average convergence-divergence analysis is also shown in plot. </h1><a href=https://finance.yahoo.com/lookup?s=API>Go to plot page</a>'
	

if __name__ == '__main__':
  app.run(port=33507)