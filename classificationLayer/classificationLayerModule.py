from entailmentClassifier import *
from votingClassifier import *


def classificationLayer(entailmentClassifierTokenizer, entailmentClassifierModel, claim, preprocessedEvidences):
  evidencesEntailmentClassification = findEvidencesEntailmentClassification(entailmentClassifierTokenizer, entailmentClassifierModel, claim, preprocessedEvidences)
  votingClassifierPrediction = votingClassifier(evidencesEntailmentClassification)

  return votingClassifierPrediction
  
