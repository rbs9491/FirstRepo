import pickle

def word_count(text, out_path):
    
    word_list = text.lower().split()
            
    count_dict = {}
    for w in word_list:
        if count_dict.get(w):
            count_dict[w] += 1
        else:
            count_dict[w] = 1
    
    parse_dict = sorted(count_dict.items())
    parse_dict = sorted(parse_dict, key = lambda x: x[1], reverse=True )
    parse_dict = [ f"{k},{v}\n" for k, v in parse_dict]
    write = "".join(parse_dict)
    
    with open(out_path, "w") as f:
        f.write(write)
        
        
def my_pickler(input_file, output_file):
    with open(input_file) as f:
        text = f.read()
    
    key_value_pair = text.split("\n")
    result = {}
    for i in key_value_pair[:-1]:
        key, value = i.split(",")
        result[key] = int(value)
            
    with open(output_file, "wb") as f2:
        pickle.dump(result, f2) 