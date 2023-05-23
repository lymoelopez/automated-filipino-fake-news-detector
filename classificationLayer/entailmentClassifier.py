import torch


def entailmentClassifier(entailmentClassifierTokenizer, entailmentClassifierModel, claim, evidence):

  tokens = entailmentClassifierTokenizer([(claim, evidence)], padding='max_length', truncation='longest_first', max_length=128, return_tensors='pt')
  
  with torch.no_grad():
    output = entailmentClassifierModel(**tokens)[0]
    entailmentClassification = output.argmax(1).item()
  
  # O means "Entailment" and 1 means "Contradiction"
  return entailmentClassification 


def findEntailmentClassificationOfEachEvidence(entailmentClassifierTokenizer, entailmentClassifierModel, inputClaim, preprocessedEvidences):
  entailmentClassificationOfEachEvidence = list(map(entailmentClassifier, [entailmentClassifierTokenizer]*len(preprocessedEvidences), [entailmentClassifierModel]*len(preprocessedEvidences), [inputClaim]*len(preprocessedEvidences), preprocessedEvidences))
  return entailmentClassificationOfEachEvidence
