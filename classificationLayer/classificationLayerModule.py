from llmClassifier  import llmClassifier 
from votingClassifier import votingClassifier


def classificationLayer(inputClaim, preprocessedEvidences, highestSimilarityScores, llmWithPromptTemplate):

  numberOfEvidences = len(preprocessedEvidences)
  classificationOfEachEvidence = list(map(llmClassifier , [inputClaim]*numberOfEvidences, preprocessedEvidences, [llmWithPromptTemplate]*numberOfEvidences))
  votingClassifierPrediction = votingClassifier(classificationOfEachEvidence)

  return votingClassifierPrediction
