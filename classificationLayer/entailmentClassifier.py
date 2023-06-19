import torch


def entailmentClassifier(inputClaim, evidence, entailmentClassifier):

  entailmentClassifierTokenizer, entailmentClassifierModel = entailmentClassifier
  
  tokens = entailmentClassifierTokenizer([(inputClaim, evidence)], padding='max_length', truncation='longest_first', max_length=128, return_tensors='pt')
  
  with torch.no_grad():
    output = entailmentClassifierModel(**tokens)[0]
    entailmentClassification = output.argmax(1).item()
  
  # O means "Entailment" and 1 means "Contradiction"
  return entailmentClassification
