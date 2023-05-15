from evidenceCollector.evidenceCollectorModule import *
from preprocessingLayer.findPreprocessedEvidences import *
from classificationLayer.classificationLayerModule import *
from automatedFakeNewsConfig import * 
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def automatedFakeNewsPipeline(inputClaim):

  numberOfSearchResults, cosineSimilarityModel, preprocessingTokenizer, transformerModel = automatedFakeNewsConfig()
  entailmentClassifierTokenizer = AutoTokenizer.from_pretrained(transformerModel)
  entailmentClassifierModel = AutoModelForSequenceClassification.from_pretrained(transformerModel)

  topEvidences, topEvidencesUrl = evidenceCollector(inputClaim, cosineSimilarityModel, numberOfSearchResults)
  preprocessedEvidences = findPreprocessedEvidences(topEvidences, preprocessingTokenizer)
  finalPrediction = classificationLayer(entailmentClassifierTokenizer, entailmentClassifierModel, inputClaim, preprocessedEvidences)

  return finalPrediction, topEvidencesUrl
