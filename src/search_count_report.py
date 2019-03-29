import csv
from datetime import datetime

from src.report import Report
import src.utils as utils

class SearchCountReport(Report):

    def generate(self):
        # Write fields to search_count.csv
        self.writer.writerow(['day', 'hour', 'count'])

        time_to_count_dict = {}

        # Read routes.csv
        for index, row in enumerate(self.reader):
            if index == 0:
                continue
            timestamp = row[0]
            datetime = self.parse_date(timestamp)
            hour = datetime.hour
            day = timestamp.split(',')[0]

            if day not in time_to_count_dict:
                time_to_count_dict[day] = {}

            if hour in time_to_count_dict[day]:
                time_to_count_dict[day][hour] += 1
            else:
                time_to_count_dict[day][hour] = 1

        for day in time_to_count_dict:
            for hour in time_to_count_dict[day]:
                self.writer.writerow([day, hour, time_to_count_dict[day][hour]])

    def parse_date(self, timestamp):
        # Ordinal suffixes are the suffixes at the end of days like 1st, 2nd, or 3rd.
        ordinal_suffixes = ['st', 'th', 'rd']
        time_str = timestamp
        # Remove ordinal suffixes so we can easily convert to datetime object
        for s in ordinal_suffixes:
            time_str = time_str.replace(s, '')
        # Remove the milliseconds from time
        time_str = time_str.split('.')[0]

        # Sample date format is March 29 2019, 01:00:00
        return datetime.strptime(time_str, "%B %d %Y, %H:%M:%S")
