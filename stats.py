
def make_word_frequency_dict(func):    
    def sort_on(items): #getting "num" values in dictionary for sorting
        return items["num"]
    
    temp_list = []
    new_list = []
    new_dict = {}
    for keys, values in func.items():
        new_dict = {"char": keys, "num": values}
        temp_list.append(new_dict)
    
    temp_list.sort(reverse = True, key = sort_on)
    
    for i in range(len(temp_list)):
        new_list.append(f"{temp_list[i]["char"]}: {temp_list[i]["num"]}")
    
    return new_list

def get_num_characters(path):
    with open(path) as f:
        filecontents = f.read().lower()
        chara_list = [char for word in filecontents.split() for char in word]
        chara_dict = {}
        for character in chara_list:
            if character in chara_dict:
                chara_dict[character] += 1
            else:
                chara_dict[character] = 1
        return chara_dict
        
def get_num_words(path):
  with open(path) as f:
    filecontents = f.read()
    words = filecontents.split()
    num_words = len(words)
    return f"Found {num_words} total words"


"""  
def get_book_text(path):
 with open(path) as f:
  filecontents = f.read()
  print(filecontents) 
"""
