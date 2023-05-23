import statistics as stat


def votingClassifier(entailmentClassificationOfEachEvidence):
  votingClassifierPrediction = stat.mode(entailmentClassificationOfEachEvidence)
  return votingClassifierPrediction
