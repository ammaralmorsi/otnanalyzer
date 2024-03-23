import pickle
from Parser_APIs import Parser_API

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

x = Parser_API(loaded_data)

print(x.opu_frame_parser)
print(x.odu_frame_parser)
print(x.otu_frame_parser)
