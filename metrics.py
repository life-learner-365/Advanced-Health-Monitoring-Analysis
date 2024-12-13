def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """

    maximums = []
    for val in range(0, len(data), n):
        max_val = max(data[val: val+n])
        maximums.append(max_val)
    return maximums  

def window_average(data: list, n: int) -> list:
    """
    Calculate average value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of averages from each window (size should be len(data)//6)
    """


    averages = []
    for val in range(0, len(data), n):
        avg_val = sum(data[val: val+n])/len(data[val: val+n])
        averages.append(round(avg_val,2))
    return averages  


def window_stddev(data: list, n: int) -> list:
    """
    Calculate standard deviation of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of standard deviations from each window (size should be len(data)//6)
    """
    # Call functions for filtering list argument
    #filter_nondigits(data)
    #filter_outliers(data)

    std_devs = []
    for val in range(0, len(data), n):
        # Pass on windows that only have one value
        if len(data[val: val+n]) == 1:
            continue

        # Calculate stddev for each window
        avg = sum(data[val: val+n])/len(data[val: val+n])
        dev_squared_sum = 0
        for x in data[val: val+n]:
            dev_squared = (x - avg)**2
            dev_squared_sum = dev_squared_sum + dev_squared
        var = dev_squared_sum/(len(data[val: val+n])-1)
        sd = var ** .5
        std_devs.append(round(sd,2))
    return std_devs
