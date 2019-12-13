import os
import json
import pandas as pd
import time
from pathlib import Path

__author__ = 'ichistov'

def time_string():
    """
    Return string with current time

    :return: String, formatted as 'Time: HH:MM:SS DD/MM/YYYY'
    """
    return 'Time: {time.tm_hour:02d}:{time.tm_min:02d}:{time.tm_sec:02d} {time.tm_mday:02d}/{time.tm_mon:02d}/{time.tm_year}'.format(
        time=time.localtime())

# Parsing JSON configuration file
config_file = r'config.json'
try:
    with open(config_file) as config:
        json_data = json.load(config)
except FileNotFoundError:
    print("JSON file wasn't found on specified location")
    exit(-1)

report_folder = json_data["reportPath"]
input_folder = json_data["inputFolder"]
output_folder = json_data["outputFolder"]
result_name = json_data["resultFileName"]

# Checking empty Input folder or not
if not len(os.listdir(input_folder)) > 0:
    print("Input file isn't found in Input Folder")
    exit(-1)

# Getting all files in folder as List
files_list = os.listdir(input_folder)

# Depending full path to input\output file
full_path = input_folder + '\\'
full_output_path = output_folder + '\\'

# Create new DataFrame
all_data = pd.DataFrame()

# Iteration for all files in input folder starting from 2nd file, saving header and dropping two firstly columns
for file in files_list:
    if files_list[0] not in str(file):
        all_data = all_data.append(pd.read_csv(full_path + file, header=None, encoding='latin1').iloc[3:, 2:])
    else:
        all_data = pd.read_csv(full_path + files_list[0], header=None, encoding='latin1').iloc[:, 2:]

# Output results
output_results = Path(full_output_path + result_name + '.csv')

# Save all dates in total output file
all_data.to_csv(output_results, encoding='latin1', index=False, header=False)

# count rows and columns in DataFrame
count_row = all_data.shape[0]
count_col = all_data.shape[1]

# Create report directory
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Open report file and save information
report_file = open(report_folder + '\\report_VT_split.txt', 'w')
report_file.write('Start script in {time}\n'.format(time=time_string()) + '\n')
report_file.write('Input Data: ' + str(files_list) + '\n')
report_file.write('Result file in: ' + str(output_results) + '\n')
report_file.write('Result file contains - ' + 'Row: ' + str(count_row) + ' Column: ' + str(count_col) + '\n''\n')
report_file.write('Script finished in {time}\n'.format(time=time_string()))
report_file.close()

print('Script finished in {time}\n'.format(time=time_string()))