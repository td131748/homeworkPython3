import os
import csv

# 1. Please download CSV files containing the stock history of some companies
# Save files giving them different names to a local folder on your drive
# 2. Write a program that searches for CSV files with stock rates in a given folder

file_name = 'Apple.csv'

def search_csv(file_name, folder_path = 'File'):
    file_path = os.path.join(folder_path, file_name)
    return os.path.exists(file_path)

# 3. Calculates the percentage change between Close and Open price and
# adds these values as another column to this CSV file.
# You can replace the old file or create a new one.
# Change = (Close-Open)/Open
# 4. The output files can be stored in another folder

file_path = os.path.join('File', file_name)
new_file_path = os.path.join('New_File', 'Modified.csv')
new_column_name = 'Percentage change'

with open(file_path, 'r') as read, open(new_file_path, 'w', newline='') as write:
    reader = csv.reader(read)
    writer = csv.writer(write)

    header = next(reader)
    header.append(new_column_name)
    writer.writerow(header)

    for row in reader:
        new_column_value = (float(row[1]) - float(row[4])) / float(row[1])
        row.append(round(new_column_value * 100, 2))
        writer.writerow(row)

