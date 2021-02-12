import os 
import hazm 

normalizer = hazm.Normalizer()

base_dir = "dataset"
base_dir_listing = os.listdir(base_dir) 

files_contents = []

for directory in base_dir_listing:
    if directory != ".DS_Store":
        files = os.listdir(base_dir + "/" + directory)
        for text_file in files:
            if text_file != ".DS_Store":
                f = open(base_dir + "/" + directory + "/" + text_file)
                files_contents.append(f.readlines())

print(len(files_contents))