import pickle
from Parser_APIs import Parser_API

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

x = Parser_API(loaded_data)

print(x.get_opu_overhead())
print(x.get_odu_overhead())
print(x.get_otu_overhead())
