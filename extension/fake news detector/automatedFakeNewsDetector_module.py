from evidenceCollector_module import evidenceCollector
from preprocessingLayer_module import preprocessingLayer
from classificationLayer_module import classificationLayer
from automatedFakeNewsDetector_config import automatedFakeNewsConfig
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def automatedFakeNewsPipeline(inputClaim, config=automatedFakeNewsConfig()):

  inputClaim = inputClaim.lower()
  urlBanList, cosineSimilarityModel, llm, llmWithPromptTemplate = config
  topEvidences, highestSimilarityScores = evidenceCollector(inputClaim, urlBanList, cosineSimilarityModel)
  
  topEvidencesContent = topEvidences[0]
  topEvidencesDetails = topEvidences[1:]
  numberOfEvidences = len(topEvidencesContent)
  topEvidencesDetails.append(numberOfEvidences)
  
  if numberOfEvidences == 0:
    predictionDetails = [1, 100]
  else:
    preprocessedClaim, preprocessedEvidences = preprocessingLayer(inputClaim, topEvidencesContent)
    predictionDetails = classificationLayer(preprocessedClaim, preprocessedEvidences, highestSimilarityScores, llmWithPromptTemplate)

  return predictionDetails, topEvidencesDetails 
