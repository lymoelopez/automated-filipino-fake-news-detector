from evidenceCollector.evidenceSelector import evidenceSelector
from preprocessingLayer.preprocessingLayerModule import preprocessingLayer
from classificationLayer.classificationLayerModule import classificationLayer
from automatedFakeNewsConfig import automatedFakeNewsConfig
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from progressBar import progressBar, testingProgress
import numpy as np
import ast


def findTopList(givenList, topIndex):
  numpyList = np.array(givenList)
  topList = numpyList[topIndex].tolist()
  return topList

def findIndexOfTopEvidences(urlList, topEvidencesUrl):

  indexOfTopEvidences = []

  for item in topEvidencesUrl:
    if item in urlList:
      indexOfItem = urlList.index(item)
      indexOfTopEvidences.append(indexOfItem)

  return indexOfTopEvidences


predictionProgressBar = testingProgress()

def automatedFakeNewsTestingPipeline2(inputClaim, filteredSearchResults, topEvidencesUrlInString, config=automatedFakeNewsConfig(currentDate="June 09 2023")):

  predictionProgressBar.showProgress()
  
  if len(filteredSearchResults[0]) == 0:
    finalPrediction = 1
    topEvidencesUrl = []
    predictionPercentage = 100 
    classificationOfEachEvidence = [] 
    highestSimilarityScores = []
  else:
    inputClaim = inputClaim.lower()
    urlBanList, cosineSimilarityModel, llm, llmWithPromptTemplate = config

    urlList, urlTitleList, urlBodyList = filteredSearchResults

    
    try:
      topEvidencesUrl = ast.literal_eval(topEvidencesUrlInString)
    except:
      topEvidencesUrlInString = "['" + topEvidencesUrlInString + "']"
      topEvidencesUrl = ast.literal_eval(topEvidencesUrlInString)
      

    indexOfTopEvidences = findIndexOfTopEvidences(urlList, topEvidencesUrl)
      

    
    topEvidencesTitle = findTopList(urlTitleList, indexOfTopEvidences)
    topEvidencesBody = findTopList(urlBodyList, indexOfTopEvidences)    
    topSearchResults =  [topEvidencesUrl, topEvidencesTitle, topEvidencesBody]
    
    topEvidences, highestSimilarityScores = evidenceSelector(inputClaim, topSearchResults, cosineSimilarityModel)
    topEvidencesContent = topEvidences[0]
    # topEvidencesUrl = topEvidences[1]

    preprocessedClaim, preprocessedEvidences = preprocessingLayer(inputClaim, topEvidencesContent)
    predictionDetails  = classificationLayer(preprocessedClaim, preprocessedEvidences, highestSimilarityScores, llmWithPromptTemplate)
    
    finalPrediction = predictionDetails[0]
    predictionPercentage = predictionDetails[1]
    classificationOfEachEvidence = predictionDetails[2]
  
  return finalPrediction, predictionPercentage, classificationOfEachEvidence, highestSimilarityScores