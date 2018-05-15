"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
IMPORTS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from __future__ import division
import os
import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, DataRange1d, LabelSet
from bokeh.io import output_notebook
from bokeh.models.ranges import FactorRange, Range1d
from bokeh.models.glyphs import *
from bokeh.colors import *
from bkcharts import HeatMap

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
NECESSARY FILE PATHS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
usbDriveLetter = "D:\\"
projectFolder = "PGM_Spr2018\\Project_python"
baseFolder = os.path.join(usbDriveLetter,projectFolder)

os.chdir(baseFolder);
allContents = os.listdir(".")
sys.path.append(allContents)

dataFolder = os.path.join(baseFolder,'data')

exec(open("helpers.py"))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
KEY TO SOME OF THE DATA FIELDS - FROM CITI BIKE
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Source: https://www.citibikenyc.com/system-data
    User Type: "Customer"=24 hr pass or 3 day pass
               "Subscriber"=annual member
    Gender: 0=unknown
        1=male
        2=female
"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
KEY TO SOME OF THE DATA FIELDS - MY OWN ASSIGNMENTS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    User Type
        0 = unknown (not reported in the data)
        1 = subscriber (annual pass)
        2 = temporary (24 hour or 3 day pass)
"""