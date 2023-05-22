from evidenceCollector.evidenceCollectorModule import evidenceCollector
from preprocessingLayer.findPreprocessedEvidences import findPreprocessedEvidences
from classificationLayer.classificationLayerModule import classificationLayer
from automatedFakeNewsConfig import automatedFakeNewsConfig
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def automatedFakeNewsPipeline(inputClaim):

  urlBanList, cosineSimilarityModel, preprocessingTokenizer, transformerModel = automatedFakeNewsConfig()
  entailmentClassifierTokenizer = AutoTokenizer.from_pretrained(transformerModel)
  entailmentClassifierModel = AutoModelForSequenceClassification.from_pretrained(transformerModel)

  topEvidences, topEvidencesUrl = evidenceCollector(inputClaim, urlBanList, cosineSimilarityModel)
  
  if len(topEvidencesUrl) == 0:
    finalPrediction = 1
  else:
    preprocessedEvidences = findPreprocessedEvidences(topEvidences, preprocessingTokenizer)
    finalPrediction = classificationLayer(entailmentClassifierTokenizer, entailmentClassifierModel, inputClaim, preprocessedEvidences)

  return finalPrediction, topEvidencesUrl
