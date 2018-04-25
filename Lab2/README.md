# Data

We experimented with 2 different methods for displaying the data: a histogram and a kernel density model. Both of these graphs were coded in Python with MatPlotLib. The pros and cons of each method are explained below:

## Histogram
<table>
    <tr><td><img alt="open opps 1" src="https://raw.githubusercontent.com/phi-line/Physics-Code/master/Lab2/images/histogram.png"></td></tr>
    <tr><td>A histogram is very good at displaying the probability of each dataset. However, due to the variance of each dataset in terms of error, the histograms have more data that fills each bin. The data for 40 swings converges more tightly around the value 1.58 showing a higher density in that area. Realizing this, we chose to explore models like a Kernel Density Estimation.</td></tr>
</table>

## KDE
<table>
    <tr><td><img alt="open opps 1" src="https://raw.githubusercontent.com/phi-line/Physics-Code/master/Lab2/images/kde.png"></td></tr>
    <tr><td>A  Kernel Density Estimation attempts to smooth out the data in a dataset and provide a nice way look at the accumulation of results in a particular area of the set. We used a Gaussian smoothing method to give a clear representation of the density patches in the datasets.</td></tr>
</table>
