import csv
import sys

from src.routes_report import RoutesReport
from src.search_count_report import SearchCountReport

def generate_report(filename):
    # Make sure filename is a csv file
    extension_index = filename.rfind('.csv')
    if extension_index == -1:
        print(f'{filename} is not a csv file! Please try again.')
        return

    csv_file = open(filename)
    csv_reader = csv.reader(csv_file)

    # Setup writer
    basename = filename[:extension_index]
    report_name = f'./reports/{basename}_report.csv'
    report_file = open(report_name, mode='w')
    report_writer = csv.writer(report_file)

    report = None
    if filename == 'routes.csv':
        report = RoutesReport(csv_reader, report_writer)
    elif filename == 'search_count.csv':
        report = SearchCountReport(csv_reader, report_writer)

    if report:
        print(f'Generating report for {filename} in {report_name}.')
        report.generate()
    else:
        print('Unsupported csv file. Please try again.')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        generate_report(filename)
    else:
        print('Unsupported command. Please run `python generate_report.py [CSV_FILE_NAME]`')
