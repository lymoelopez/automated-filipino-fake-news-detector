from evidenceCollector.evidenceSelector import evidenceSelector
from preprocessingLayer.preprocessingLayerModule import preprocessingLayer
from classificationLayer.classificationLayerModule import classificationLayer
from automatedFakeNewsConfig import automatedFakeNewsConfig
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from progressBar import progressBar, testingProgress


predictionProgressBar = testingProgress()

def automatedFakeNewsTestingPipeline(inputClaim, filteredSearchResults, config=automatedFakeNewsConfig()):

  predictionProgressBar.showProgress()
  
  if len(filteredSearchResults[0]) == 0:
    finalPrediction = 1
    topEvidencesUrl = []
    
  else:
    inputClaim = inputClaim.lower()
    urlBanList, cosineSimilarityModel, entailmentClassifier = config

    topEvidences, highestSimilarityScores = evidenceSelector(inputClaim, filteredSearchResults, cosineSimilarityModel)
    topEvidencesContent = topEvidences[0]
    topEvidencesUrl = topEvidences[1]

    preprocessedClaim, preprocessedEvidences = preprocessingLayer(inputClaim, topEvidencesContent)
    finalPrediction = classificationLayer(preprocessedClaim, preprocessedEvidences, highestSimilarityScores, entailmentClassifier)

  return finalPrediction, topEvidencesUrl
