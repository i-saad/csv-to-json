#!/usr/bin/python3

import os
import csv
import json

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
# traverse every r directory, and list directories as m and files as csvs
  for r,m,csvs in os.walk(root):
    #print(csvs)
    # loop on every file in folders
    for f in csvs:
      if f.endswith(".csv"):
        jsn = os.path.splitext(f)[0]+'.json'

        with open(f'{r}/{f}', 'r') as input_file:
          reader = csv.DictReader(input_file)

          jsonoutput = f'{r}/{jsn}'
          print('Creating file:', jsonoutput)
          with open(jsonoutput, 'w+') as output_file:
            for row in reader:
              json.dump(row, output_file)
              output_file.write(',\n')
