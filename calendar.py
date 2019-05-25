def merge_ranges(times_list):
    """
        Add a feature to the company's calendar tool to see the times in a day when everyone is available.

        Meetings are stored as a tuple of integers representing the number of 30 minute blocks past 9AM.
        (2, 3) Meeting from 10:00 - 10:30 AM
        (6, 9) Meeting from 12:00 - 1:30 PM

        This function will take in a list of meeting time ranges and returns a list of condensed ranges.
    """
