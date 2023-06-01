from llmClassifier  import llmClassifier 
from votingClassifier import votingClassifier


def classificationLayer(inputClaim, preprocessedEvidences, llmWithPromptTemplate):

  classificationOfEachEvidence = list(map(llmClassifier , [inputClaim]*len(preprocessedEvidences), preprocessedEvidences, [llmWithPromptTemplate]*len(preprocessedEvidences)))
  votingClassifierPrediction = votingClassifier(classificationOfEachEvidence)

  return votingClassifierPrediction
