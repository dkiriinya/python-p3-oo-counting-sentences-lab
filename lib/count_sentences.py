#!/usr/bin/env python3

class MyString:
  def __init__(self,value='') :
    self.value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self,value):
    if isinstance(value,str):
      self._value = value
    else:
      print("The value must be a string.")
      
  def is_sentence(self):
    return self._value[-1] == '.'
  
  def is_question(self):
   return self._value[-1] == '?'
  
  def is_exclamation(self):
    return self._value[-1] == '!'
  
  def count_sentences(self):
    split_options = ['.', '?', '!']
    for option in split_options:
      self._value = self._value.replace(option, '$')
    sentences = self._value.split('$')
    sentences = list(filter(None, sentences))
    return len(sentences)
  

    

    
