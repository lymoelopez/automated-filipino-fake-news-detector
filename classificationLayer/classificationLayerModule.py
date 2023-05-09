from entailmentClassifier import *
from votingClassifier import *


def classificationLayer(entailmentClassifierTokenizer, entailmentClassifierModel, claim, preprocessedEvidences):
  entailmentClassificationOfEachEvidence = findEntailmentClassificationOfEachEvidence(entailmentClassifierTokenizer, entailmentClassifierModel, claim, preprocessedEvidences)
  votingClassifierPrediction = votingClassifier(entailmentClassificationOfEachEvidence)

  return votingClassifierPrediction
  
