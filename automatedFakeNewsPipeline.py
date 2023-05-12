from evidenceCollector.evidenceCollectorModule import *
from preprocessingLayer.preprocessingLayerModule import *
from classificationLayer.classificationLayerModule import *
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSequenceClassification


def automatedFakeNewsPipeline(inputClaim):

  cosineSimilarityModel = SentenceTransformer("danjohnvelasco/filipino-sentence-roberta-v1")
  filteredUrlList, extractedArticlesList, topFiveEvidences = evidenceCollector(inputClaim, cosineSimilarityModel)

  preprocessingTokenizer = AutoTokenizer.from_pretrained("danjohnvelasco/filipino-sentence-roberta-v1")
  preprocessedEvidences = preprocessingLayer(topFiveEvidences, preprocessingTokenizer)

  transformerModel = 'jcblaise/electra-tagalog-small-uncased-discriminator-newsphnli'
  entailmentClassifierTokenizer = AutoTokenizer.from_pretrained(transformerModel)
  entailmentClassifierModel = AutoModelForSequenceClassification.from_pretrained(transformerModel)

  finalPrediction = classificationLayer(entailmentClassifierTokenizer, entailmentClassifierModel, inputClaim, preprocessedEvidences)

  return finalPrediction, topFiveEvidences
