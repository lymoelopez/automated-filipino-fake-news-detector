from  preprocessingLayerModule import preprocessingLayer


def findPreprocessedEvidences(topEvidences, preprocessingTokenizer):
  preprocessedEvidences = list(map(preprocessingLayer, topEvidences, [preprocessingTokenizer]*len(topEvidences)))
  return preprocessedEvidences
