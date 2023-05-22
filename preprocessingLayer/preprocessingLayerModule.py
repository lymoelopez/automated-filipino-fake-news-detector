from textCleaning import findCleanedText
from tokenizer import findBPE


def preprocessingLayer(text, preprocessingTokenizer):
  
  cleanedText = findCleanedText(text)
  tokenizedText = findBPE(cleanedText, preprocessingTokenizer)
  preprocessedText = tokenizedText

  return preprocessedText
