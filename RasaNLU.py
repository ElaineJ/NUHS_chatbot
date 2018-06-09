# -*- coding: utf-8 -*-
"""
Created on Thu May 24 23:42:36 2018

@author: User
"""

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

#training_data = load_data('demo-rasa1.json')
#trainer = Trainer(config.load("sample_configs/config_spacy.yml"))
#trainer.train(training_data)
#model_directory = trainer.persist('./projects/default/')
#model_directory2=Metadata.load('./projects/default/model_20180525-011843/')

interpreter = Interpreter.load('./projects/default/model_20180529-135039/')
#Dictionary=interpreter.parse("my child is not passing motion")
#print(Dictionary)
#print(Dictionary['entities'][0]['entity'])
