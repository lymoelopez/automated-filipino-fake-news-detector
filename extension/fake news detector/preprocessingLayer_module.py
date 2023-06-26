from preprocessingLayer_textCleaning import findCleanedText


def preprocessingLayer(inputClaim, topEvidences):
  preprocessedClaim = findCleanedText(inputClaim)
  preprocessedEvidences = list(map(findCleanedText, topEvidences))
  return preprocessedClaim, preprocessedEvidences
