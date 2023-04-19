import os
import csv

# Set the path to the folder containing the WAV files
folder_path = "/Users/fuchunhsieh/Desktop/HomeWork/CSC-481/Audio Project/Original Sound Spectrograms"

# Create a list to store the file information
file_info = []

# Loop through all the files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a WAV file
    if file_name.endswith(".png"):
        # Get the full file path
        label = file_name[:4]
        # Append the file information to the list
        file_info.append((file_name, label))

# Write the file information to a CSV file
with open("file_info.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["File Name", "label"])
    writer.writerows(file_info)
