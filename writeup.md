## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

Missing values may occur if the device connection was compromised either due to falling off or another cause. Ignoring these values essentially gets rid of a marker that shows an anomaly in the data, which would serve as a marker to explore the data surrounding it in case the data surrounding the missing/no signal values were affected as well. 

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

The standard deviations would represent fluctuations of the heart rate from the average heart at any given time since standard deviation represents how much a group differs from the mean of the group.

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

When x is at 2, 7, and 10, there are drastic drops in max heart rate. When x is around 13 and 20, there is a sharp increase at both times. When x is at 25, there is a sharp decrease from near the peak, and a sharp decrease when x is 30. When x is around 37, there is a sharp increase again, and then a decrease around x=40, and the last sharp increase at x = 43. 

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

Yes, there is a corresponding difference in the stdevs graph and are aligned with the times described above when there was a sharp increase or decrease in average heart rate. 
