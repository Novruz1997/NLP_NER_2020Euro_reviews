# -*- coding: utf-8 -*-
"""Named_Entity_Recognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nekDYf3Z7QKeBALHOKRve971CN7gMP0A
"""

import spacy
import random
import json
import pathlib
root = pathlib.Path().cwd()
new_file = root.joinpath('train_data', 'train_data.json')

with open(new_file) as f:
  data = json.load(f)

nlp = spacy.blank('en')
ner = nlp.create_pipe('ner')
nlp.add_pipe(ner)

# print(nlp.pipe_names)

for label in data['classes']:
  nlp.entity.add_label(label)

optimizer = nlp.begin_training()

li = []
for text, annotations in data['annotations']:
  li.append((text, annotations))


# Start the training
nlp.begin_training()

# Loop for 10 iterations
for itn in range(10):
    # Shuffle the training data
    random.shuffle(li)
    losses = {}
   
    # Batch the examples and iterate over them
    for batch in spacy.util.minibatch(li, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]
        
        # Update the model
        nlp.update(texts, annotations, losses=losses)
        print(losses)

TEST_DATA = ['Turkey has very young and talanted squad for this tournament',
             'Hakan Calhanoglu will be top scorer for Turkey',
             'the best players of France are Mbappe and Kante',
             'Cristiano will score 10 goals in this tournament', 
             'I am defending last World Cup champions, France',
             'Belgium is serious favorite of crown',
             'Memphis Depay was more valuable for Holland than abybody else',
             'Lewandowski will score more goals and assists for Poland than EURO 2016',
             'Harry Kane is my favorite player for golden boot',
             ]

# Process each text in TEST_DATA
for doc in nlp.pipe(TEST_DATA):
    # Print the document text and entitites
    print(doc.text)
    print(doc.ents,'\n\n')

