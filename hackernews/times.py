import read

from dateutil.parser import parse


def _return_hour(timestamp):
    """ Grab the hour of a time object
    """

    return parse(timestamp).hour


def hour_frequency(series):
    """ Return a series with its hour 
        based on a time object
    """
    
    hours = series.apply(_return_hour)
    
    return hours.value_counts()