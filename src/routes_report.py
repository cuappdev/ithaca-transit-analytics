import csv

from src.report import Report
import src.utils as utils

class RoutesReport(Report):

    def generate(self):
        # Write fields to routes_report.csv
        self.writer.writerow(['timestamp', 'origin', 'destination'])

        # Read routes.csv
        for index, row in enumerate(self.reader):
            if index == 0:
                continue
            msg_json = utils.parse_msg_json(row[1])
            origin, dest = self.get_origin_dest(msg_json)
            timestamp = row[0]
            self.writer.writerow([timestamp, origin, dest])

    def get_origin_dest(self, msg_json):
        origin = utils.parse_key(msg_json, 'originName')
        dest = utils.parse_key(msg_json, 'destinationName')
        if not origin or origin == 'Current Location':
            origin = utils.parse_key(msg_json, 'start')
        if not dest or dest == 'Current Location':
            dest = utils.parse_key(msg_json, 'end')
        return origin, dest
