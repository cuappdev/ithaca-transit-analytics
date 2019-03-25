import csv
import sys

def parse_message(msg):
  start_idx = msg.find('{')
  if start_idx == -1:
    return ''
  return msg[start_idx:]

def parse_key(msg, key):
  key_idx = msg.find(key)
  if key_idx == -1:
    return ''
  key_start_idx = key_idx + len(key) + 3
  key_end_idx = msg.find("'", key_start_idx)
  return msg[key_start_idx: key_end_idx]

def get_origin_dest(msg):
  origin = parse_key(msg, 'originName')
  dest = parse_key(msg, 'destinationName')
  if origin == 'Current Location' or origin == '':
    origin = parse_key(msg, 'start')
  if dest == '':
    dest = parse_key(msg, 'end')
  return origin, dest

def gen_routes_report(filename):
  # Setup writing to routes_report.csv
  report_file = open('routes_report.csv', mode='w')
  report_writer = csv.writer(report_file, delimiter=',')
  report_writer.writerow(['timestamp', 'start', 'end'])

  # Read filename as csv
  csv_file = open(filename)
  csv_reader = csv.reader(csv_file, delimiter=',')
  for index, row in enumerate(csv_reader):
    if index == 0:
      continue
    timestamp = row[0]
    msg = parse_message(row[1])
    origin, dest = get_origin_dest(msg)
    report_writer.writerow([timestamp, origin, dest])


if __name__ == '__main__':
  if len(sys.argv) == 2:
    filename = sys.argv[1]
    if filename == 'routes.csv':
      gen_routes_report(filename)
