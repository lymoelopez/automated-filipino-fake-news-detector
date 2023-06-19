from entailmentClassifierModule import entailmentClassifierModule
from votingClassifier import votingClassifier


def classificationLayer(inputClaim, preprocessedEvidences, highestSimilarityScores, entailmentClassifier):

  numberOfEvidences = len(preprocessedEvidences)
  classificationOfEachEvidence = list(map(entailmentClassifierModule, [inputClaim]*numberOfEvidences, preprocessedEvidences, [entailmentClassifier]*numberOfEvidences))
  votingClassifierPrediction = votingClassifier(classificationOfEachEvidence)

  return votingClassifierPrediction
