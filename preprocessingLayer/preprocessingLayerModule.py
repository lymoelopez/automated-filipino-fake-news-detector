from textCleaning import *
from tokenization import *

def preprocessingLayer(text, tokenizer):

  cleanedText = removeCharactersAndLowercase(text)
  tokenizedText = findBPE(cleanedText, tokenizer)
  return tokenizedText
