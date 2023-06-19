from evidenceCollector.evidenceCollectorModule import evidenceCollector
from preprocessingLayer.preprocessingLayerModule import preprocessingLayer
from classificationLayer.classificationLayerModule import classificationLayer
from automatedFakeNewsConfig import automatedFakeNewsConfig
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def automatedFakeNewsPipeline(inputClaim, config=automatedFakeNewsConfig()):

  inputClaim = inputClaim.lower()
  urlBanList, cosineSimilarityModel, entailmentClassifier = config
  topEvidences, highestSimilarityScores = evidenceCollector(inputClaim, urlBanList, cosineSimilarityModel)
  topEvidencesContent = topEvidences[0]
  topEvidencesDetails = topEvidences[1:]

  if len(topEvidencesContent) == 0:
    finalPrediction = 1
  else:
    preprocessedClaim, preprocessedEvidences = preprocessingLayer(inputClaim, topEvidencesContent)
    finalPrediction = classificationLayer(preprocessedClaim, preprocessedEvidences, highestSimilarityScores, entailmentClassifier)

  return finalPrediction, topEvidencesDetails 
