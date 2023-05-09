from textCleaning import *
from tokenizer import *

def preprocessingLayer(text, tokenizer):

  cleanedText = removeCharactersAndLowercase(text)
  tokenizedText = findBPE(cleanedText, tokenizer)
  return tokenizedText
