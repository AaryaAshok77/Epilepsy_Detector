from glob import glob

# Specify the directory containing the files
directory = '/Users/aaryaashokk/Documents/Coding/Projects/DataSets/'

# Use glob to find all files ending with .edf and not .edf.seizure
edf_files = glob(directory + '*.edf')
edf_files = [file for file in edf_files if not file.endswith('.seizure.edf')]

print(edf_files)