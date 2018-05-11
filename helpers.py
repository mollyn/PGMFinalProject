"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Helper functions for analysis
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


"""""""""""""""""""""""""""""""""""""""
Close all open matplotlib plots
"""""""""""""""""""""""""""""""""""""""
def ca():
    plt.close("all")
    

"""""""""""""""""""""""""""""""""""""""
Create pretty list of the columns of a
pandas dataframe
"""""""""""""""""""""""""""""""""""""""
def cols(df):
    return df.columns.tolist()
    
    
"""""""""""""""""""""""""""""""""""""""
Easily reassign values in the dataframe,
to make it easier to work with
"""""""""""""""""""""""""""""""""""""""
def reassignVals(df,col,oldVal,newVal):
    indices = df[df[col]==oldVal].index
    df.set_value(indices,col,newVal)
    # no return necessary, modifies in place
    
    
"""""""""""""""""""""""""""""""""""""""
Special version of reassignVals, since
dataframes and nan's are stupid and 
don't like to get along
oldVal=nan is assumed for this fcn
"""""""""""""""""""""""""""""""""""""""
def reassignNans(df,col,newVal):
    indices = df[df[col].isnull()].index
    df.set_value(indices,col,newVal)
    # no return necessary, modifies in place
 
"""""""""""""""""""""""""""""""""""""""
Take in bokeh plot and apply formatting
I want to be standard across all of
my plots
"""""""""""""""""""""""""""""""""""""""   
def standardize(p):
    p.xaxis.axis_label_text_font_size = "14pt"
    p.yaxis.axis_label_text_font_size = "14pt"
    p.y_range.start = 0
    p.title.text_font_size = "16pt"
    p.title.align = "center"    
    p.xaxis.major_label_text_font_size = "9pt"
    p.yaxis.major_label_text_font_size = "9pt"
    
"""""""""""""""""""""""""""""""""""""""
Take in bokeh plot and apply formatting
I want to be standard across all vbar 
plots
"""""""""""""""""""""""""""""""""""""""    
def standardizevbar(p):
    p.xaxis.minor_tick_line_color = None
    p.xgrid.grid_line_color = None
    p.xaxis.major_label_orientation = -0.75
    

"""""""""""""""""""""""""""""""""""""""
Take in bokeh plot and info to put
percentages on top of the bars
"""""""""""""""""""""""""""""""""""""""   
def addPctsToBars(p, x, top, totalSize):
    pcts = top / totalSize * 100
    pcts = np.round(pcts,2)
    pctsStrings = []
    for i in range(pcts.size):
        pctsStrings.append(str(pcts[i]) + "%")
    
    source = ColumnDataSource(data=dict(x=x,
                                        top=top,
                                        pcts = pctsStrings))
    labels = LabelSet(x='x',y='top',text='pcts',
                      level='glyph',x_offset=0,y_offset=0,
                      source=source,render_mode='canvas',
                      text_align='center',text_font_size="10pt")
    p.add_layout(labels)
    print(sum(pcts))

