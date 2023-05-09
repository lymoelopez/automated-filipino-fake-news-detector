from transformers import AutoTokenizer

def findBPE (text, tokenizer):
  tokenIDs = tokenizer.encode(text)
  BPE = tokenizer.convert_ids_to_tokens(tokenIDs)
  text = " ".join(BPE)
  return text