"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt

# import os module for finding absolute path
import os

def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    """  

    # get absolute path of file
    path = os.path.abspath(filename)

    # open file and read into the `data` list
    file = open(path)
    heart_rates = file.read().split("\n")
    hr = filter_nondigits(heart_rates)
    hr = filter_outliers(hr)
    file.close()

    # plot each list
    maximums = window_max(hr, 6)
    averages = window_average(hr, 6)
    stdevs = window_stddev(hr, 6)

    # for loop to plot all lists
    plots = {"maximums": maximums, "averages": averages, "stdevs": stdevs}
    for key,value in plots.items():
        plt.plot(range(0,len(value)), value)
        
        # Find the digit in filename to name each file and plot
        data_num = 0
        for char in filename:
            if char.isdigit():
                data_num = char

        plt.title(key.capitalize() + " " + data_num)
        plt.savefig(os.path.abspath("images") + "/" + key + data_num + ".png")
        plt.show()

    # return all 3 lists
    return(window_max(hr, 6), window_average(hr, 6), window_stddev(hr, 6) )


if __name__ == "__main__":
    run("data/data6.txt")
