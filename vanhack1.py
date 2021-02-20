# Timesheet Sum
# You've been keeping time sheets to record your in/out times for the past year. Up until now, you've relied on hand totals to report the number of hours worked in a billing period. Instead of risking inaccuracy and wasted time, in this challenge, concoct a function to sum the sheet automatically.
#
# Here are the formatting constraints you've adopted:
#
# In/out times for each day are on their own line.
# There may be multiple comma- and space-separated ranges in a single line; for example: 10-1, 2:30-8, ordered chronologically and non-overlapping.
# A time range is delimited by spaces and a dash (-).
# Each time is in either H or H:MM format.
# It's assumed that in any interval of work, the end time is the first occurrence of its hour after the start, possibly on the next day. In other words, 10-1 could either mean 10 PM to 1 AM or 10 AM to 1 PM and will always be 3 hours, never 10 AM to 1 AM (15 hours).
# Minutes, if present, will always be in quarters of hours: 00, 15, 30, 45.
# Times are a mix of 24-hour format (military time) and 12-hour format (but consistent within each range).
# AM/PM or any other text is not present in any timesheet.
# Here's the function definition:
#
# timesheetSum(path)
# Parameters
# path: String - path to the timesheet text file to read
#
# Return Value
# Float - the sum of all start/end intervals in the timesheet
#
# Example
# Let's take a look at timesheets/04_april.txt:
#
# 10-11, 11:30-4, 5-6
# 7:45-8:30, 10-2
# 8-11:30
# 6-9
# 10:30-12, 1:30-2
# 11-1:30, 5-8, 9-10
# 10-14, 17:30-21:30
# Note that the last line is in military time! Here's each interval in the file with elapsed time:
#
# start | end   | elapsed
# ------+-------+--------
# 10    | 11    | 1.0
# 11:30 | 4     | 4.5
# 5     | 6     | 1.0
# 7:45  | 8:30  | 0.75
# 10    | 2     | 4.0
# 8     | 11:30 | 3.5
# 6     | 9     | 3.0
# 10:30 | 12    | 1.5
# 1:30  | 2     | 0.5
# 11    | 1:30  | 2.5
# 5     | 8     | 3.0
# 9     | 10    | 1.0
# 10    | 14    | 4.0
# 17:30 | 21:30 | 4.0
# ------+-------+--------
# total           34.25
# Therefore, a call to sum_timesheet("timesheets/04_april.txt") should return 34.25.

def sum_timesheet(path):
    time_sum = 0
    file = open(path, "r")
    read_file = file.readlines()
    content = [x.replace(":", ".") for x in read_file]
    bottle = [x.strip().split(",") for x in content]
    for bot in bottle:
        for each_time in bot:
            split_time = each_time.split("-")
            start_time = split_time[0].strip()
            end_time = split_time[1].strip()
            start_hour = int(float(start_time.strip()))
            end_hour = int(float(end_time.strip()))

            if len(start_time) > 2:
                start_minute = int(start_time.strip().split(".")[1]) / 60
                start_hour += start_minute

            if len(end_time) > 2:
                end_minute = int(end_time.strip().split(".")[1]) / 60
                end_hour += end_minute

            if start_hour > end_hour:
                end_hour = end_hour + 12
            time_difference = end_hour - start_hour
            time_sum += time_difference
    return time_sum



