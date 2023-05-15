from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

def automatedFakeNewsConfig():
  numberOfSearchResults = 20
  cosineSimilarityModel = SentenceTransformer("danjohnvelasco/filipino-sentence-roberta-v1")
  preprocessingTokenizer = AutoTokenizer.from_pretrained("danjohnvelasco/filipino-sentence-roberta-v1")
  transformerModel = 'jcblaise/electra-tagalog-small-uncased-discriminator-newsphnli'

  return numberOfSearchResults, cosineSimilarityModel, preprocessingTokenizer, transformerModel
