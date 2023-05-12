from  preprocessingLayerModule import *


def findPreprocessedEvidences(topFiveEvidences, preprocessingTokenizer):
  preprocessedEvidences = list(map(preprocessingLayer, topFiveEvidences, [preprocessingTokenizer]*len(topFiveEvidences)))

  return preprocessedEvidences
