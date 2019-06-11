def merge_ranges(meetings):
    """
        Add a feature to the company's calendar tool to see the times in a day when everyone is available.

        Meetings are stored as a tuple of integers representing the number of 30 minute blocks past 9AM.
        (2, 3) Meeting from 10:00 - 10:30 AM
        (6, 9) Meeting from 12:00 - 1:30 PM

        This function will take in a list of meeting time ranges and returns a list of condensed ranges.
    """

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the first earliest meeting
    merged_meetings = [sorted_meetings[0]]

    # starting loop with the second meeting
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        # initializing variables for last merged_meetings
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings
