import statistics as stat


def votingClassifier(evidencesEntailmentPrediction):
  votingClassifierPrediction = stat.mode(evidencesEntailmentPrediction)
  return votingClassifierPrediction
  