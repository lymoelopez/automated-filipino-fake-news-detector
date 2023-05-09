import torch


def entailmentClassifier(entailmentClassifierTokenizer, entailmentClassifierModel, claim, evidence):

  tokens = entailmentClassifierTokenizer([(claim, evidence)], padding='max_length', truncation='longest_first', max_length=128, return_tensors='pt')
  
  with torch.no_grad():
    out = entailmentClassifierModel(**tokens)[0]
    entailmentClassification = out.argmax(1).item()
  
  # O means "Entailment" and 1 means "Contradiction"
  return entailmentClassification 


def findEntailmentClassificationOfEachEvidence(entailmentClassifierTokenizer, entailmentClassifierModel, claim, preprocessedEvidences):
  entailmentClassificationOfEachEvidenceList = list(map(entailmentClassifier, [entailmentClassifierTokenizer]*len(preprocessedEvidences), [entailmentClassifierModel]*len(preprocessedEvidences), [claim]*len(preprocessedEvidences), preprocessedEvidences))
  return entailmentClassificationOfEachEvidenceList 
