import os 
import json 
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

normalized_texts = []

for content in files_contents:
    normalized_text = normalizer.normalize(content[0])
    normalized_texts.append(normalized_text)

tokenized_lists = []

for text in normalized_texts:
    tokenized_list = hazm.word_tokenize(text)
    tokenized_lists.append(tokenized_list)

final_list = []

for tokenized_list in tokenized_lists:
    final_list += tokenized_list

words_frequency = []
freq_dic = {}

for word in final_list:
    print(f"Working on {word}")
    freq_dic[word] = final_list.count(word) 

json_file = json.dumps(freq_dic) 
with open("words.json", "w") as out_file:
    out_file.write(json)
