from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer


def automatedFakeNewsConfig():

  urlBanList = ["facebook", "twitter", "youtube", "pdf", "blog", "tiktok", "instagram", "youtu.be", "mp4", "mp3", "audiobook", "podcast", "spotify", "slideshare", "github", "huggingface", "reddit", "bible", "dailymotion"]

  cosineSimilarityModel = SentenceTransformer("danjohnvelasco/filipino-sentence-roberta-v1")
  preprocessingTokenizer = AutoTokenizer.from_pretrained("danjohnvelasco/filipino-sentence-roberta-v1")
  transformerModel = 'jcblaise/electra-tagalog-small-uncased-discriminator-newsphnli'

  return  urlBanList, cosineSimilarityModel, preprocessingTokenizer, transformerModel
