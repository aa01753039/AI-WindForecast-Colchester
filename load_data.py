"""
Script for combining CSV files with the same prefix into a single CSV file.
"""
import os
import csv

def join_csv_files(folder_path):
    # Function to check if the row should be skipped
    def should_skip_row(file_name, first_row, is_first_file):
        # Do not skip any rows for the first specified files
        if file_name in ["brighton_0001.csv", "colchester_0001.csv"]:
            return False
        # For other files, skip the first row if it's not the first file processed
        return is_first_file and first_row[0].isdigit()

    # Function to process and combine files for a given prefix
    def process_files(files, output_file_name):
        combined_data = []
        for i, filename in enumerate(files):
            with open(os.path.join(folder_path, filename), mode='r') as file:
                reader = csv.reader(file)
                first_row = next(reader, None)
                if first_row is None:
                    continue  # Skip empty files
                
                # Determine if the current row should be skipped
                if i > 0 and should_skip_row(filename, first_row, i == 0):
                    # Skip the next row if the first is numeric and not the first file
                    next(reader, None)
                else:
                    # Include the first row for the first file
                    combined_data.append(first_row)
                
                # Append the rest of the rows
                combined_data.extend(list(reader))
        
        # Write combined data to new CSV
        with open(os.path.join(folder_path, output_file_name), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(combined_data)
    
    # Collect files for each prefix
    brighton_files = [file for file in os.listdir(folder_path) if file.startswith("brighton")]
    colchester_files = [file for file in os.listdir(folder_path) if file.startswith("colchester")]

    # Process and combine files for each prefix
    process_files(brighton_files, "brighton.csv")
    process_files(colchester_files, "colchester.csv")

# Assuming the folder 'data' is in the current working directory
join_csv_files('data')
