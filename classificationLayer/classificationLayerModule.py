from entailmentClassifier  import entailmentClassifier 
from votingClassifier import votingClassifier


def classificationLayer(inputClaim, preprocessedEvidences, highestSimilarityScores, entailmentClassifier):

  numberOfEvidences = len(preprocessedEvidences)
  classificationOfEachEvidence = list(map(llmClassifier , [inputClaim]*numberOfEvidences, preprocessedEvidences, [entailmentClassifier]*numberOfEvidences))
  votingClassifierPrediction = votingClassifier(classificationOfEachEvidence)

  return votingClassifierPrediction
