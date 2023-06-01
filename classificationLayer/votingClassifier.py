import statistics as stat


def votingClassifier(classificationOfEachEvidence):
  votingClassifierPrediction = stat.mode(classificationOfEachEvidence)
  return votingClassifierPrediction
