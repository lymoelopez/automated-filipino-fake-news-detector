from transformers import AutoTokenizer


def findBPE (text, preprocessingTokenizer):

  BPEtokenIDs =  preprocessingTokenizer.encode(text)
  BPEtokens =  preprocessingTokenizer.convert_ids_to_tokens(BPEtokenIDs)
  tokenizedText = " ".join(BPEtokens)

  return tokenizedText
