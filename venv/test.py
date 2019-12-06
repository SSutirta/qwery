import fasttext
model = fasttext.load_model('cbowModel.bin')
print(model.words) # list of words in dictionary
