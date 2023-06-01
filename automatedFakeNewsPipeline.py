from evidenceCollector.evidenceCollectorModule import evidenceCollector
from preprocessingLayer.preprocessingLayerModule import preprocessingLayer
from classificationLayer.classificationLayerModule import classificationLayer
from automatedFakeNewsConfig import automatedFakeNewsConfig
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def automatedFakeNewsPipeline(inputClaim, config=automatedFakeNewsConfig()):

  inputClaim = inputClaim.lower()
  urlBanList, cosineSimilarityModel, llm, llmWithPromptTemplate = config
  topEvidences, topEvidencesUrl = evidenceCollector(inputClaim, urlBanList, cosineSimilarityModel)
  
  if len(topEvidencesUrl) == 0:
    finalPrediction = 1
  else:
    preprocessedEvidences = preprocessingLayer(topEvidences)
    finalPrediction = classificationLayer(inputClaim, preprocessedEvidences, llmWithPromptTemplate)

  return finalPrediction, topEvidencesUrl
