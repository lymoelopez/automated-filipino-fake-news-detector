from textCleaning import findCleanedText


def preprocessingLayer(topEvidences):
  preprocessedEvidences = list(map(findCleanedText, topEvidences))
  return preprocessedEvidences
