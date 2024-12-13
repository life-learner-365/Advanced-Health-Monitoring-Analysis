def filter_nondigits(data: list) -> list:
    """
    Name: 
        filter_nondigits
    Description: 
        The function filter_nondigits returns a list of integers with all non-digit strings removed
    Syntax: 
        filter_nondigits(data)
    Parameters: 
        data (List): The list of strings representing heart rate samples with possible invalid or missing data. 
    Returns: 
        list[int]: list of integers, with all non-digit strings removed
    """
    cleaned_list = []

    # strip values in text list and append integers only
    for val in data:
        val = val.strip()
        try:
            if isinstance(int(val), int):
                    val = int(val)
                    cleaned_list.append(val)
        except:
            pass
    return cleaned_list


def filter_outliers(data: list) -> list:
    """
    Name: 
        filter_outliers
    Description: 
        This function will take in a list of integers and filter out all heart rate samples 
        that are less than 30 and greater than 250.
    Syntax: 
        filter_outliers(data)
    Parameters: 
        data (List): The list of integers representing heart rate samples.
    Returns: 
        list[int]: list of integers, with values less than 30 and greater than 250 removed.
    """

    filtered_list = []
    for val in data:
         if val > 30 and val < 250:
              filtered_list.append(val)
    return filtered_list

