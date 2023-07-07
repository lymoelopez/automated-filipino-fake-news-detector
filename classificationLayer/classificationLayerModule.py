from llmClassifier  import llmClassifier 
from votingClassifier import votingClassifier
import collections


def findPredictionPercentage(numberOfEvidences, classificationOfEachEvidence, votingClassifierPrediction):
  frequencyOfClassification = collections.Counter(classificationOfEachEvidence)
  predictionPercentage = (frequencyOfClassification[votingClassifierPrediction] / numberOfEvidences) * 100
  return predictionPercentage

def classificationLayer(inputClaim, preprocessedEvidences, highestSimilarityScores, llmWithPromptTemplate):

  numberOfEvidences = len(preprocessedEvidences)
  classificationOfEachEvidence = list(map(llmClassifier , [inputClaim]*numberOfEvidences, preprocessedEvidences, [llmWithPromptTemplate]*numberOfEvidences))
  votingClassifierPrediction = votingClassifier(classificationOfEachEvidence)

  predictionPercentage = findPredictionPercentage(numberOfEvidences, classificationOfEachEvidence, votingClassifierPrediction)
  predictionDetails = [votingClassifierPrediction, predictionPercentage, classificationOfEachEvidence]
  
  return predictionDetails
