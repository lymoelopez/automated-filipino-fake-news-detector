from entailmentClassifier import *
from votingClassifier import *


def classificationLayer(entailmentClassifierTokenizer, entailmentClassifierModel, claim, preprocessedEvidences):
  evidencesEntailmentClassification = findEntailmentClassificationOfEachEvidence(entailmentClassifierTokenizer, entailmentClassifierModel, claim, preprocessedEvidences)
  votingClassifierPrediction = votingClassifier(evidencesEntailmentClassification)

  return votingClassifierPrediction
  
