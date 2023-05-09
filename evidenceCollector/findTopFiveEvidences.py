from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def findSimilarityScores(inputClaim, extractedArticlesList, model):

  # append claim in front of extracted articles list
  sentences = list(extractedArticlesList)
  sentences.insert(0, inputClaim)
  sentenceEmbeddings = model.encode(sentences)

  similarityScores = cosine_similarity(
      [sentenceEmbeddings[0]],
      sentenceEmbeddings[1:]
  )

  return similarityScores[0]

def findTopFiveEvidences(inputClaim, extractedArticlesList, model):

  similarityScores = findSimilarityScores(inputClaim, extractedArticlesList, model)
  topFiveSimilarityScoresIndex = np.argpartition(similarityScores,-5)[-5:]

  numpyExtractedArticlesList = np.array(extractedArticlesList)
  topFiveEvidences = numpyExtractedArticlesList[topFiveSimilarityScoresIndex]

  return topFiveEvidences
     
