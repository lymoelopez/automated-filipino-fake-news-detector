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

def findNumberOfEvidences(extractedArticlesList):

  numberOfArticles = len(extractedArticlesList)

  if numberOfArticles > 5:
    numberOfEvidences = 5
  else:
    numberOfEvidences = numberOfArticles

  return numberOfEvidences

def findHighestSimilarityScoresIndex(inputClaim, extractedArticlesList, model):

  numberOfEvidences = findNumberOfEvidences(extractedArticlesList)

  similarityScores = findSimilarityScores(inputClaim, extractedArticlesList, model)
  highestSimilarityScoresIndex = np.argpartition(similarityScores,-numberOfEvidences)[-numberOfEvidences:]

  return  highestSimilarityScoresIndex

def findTopList(givenList, topIndex):

  numpyList = np.array(givenList)
  topList = numpyList[topIndex]

  return topList

def findTopEvidences(inputClaim, extractedArticlesList, filteredUrlList, model):

  highestSimilarityScoresIndex = findHighestSimilarityScoresIndex(inputClaim, extractedArticlesList, model)

  topEvidences = findTopList(extractedArticlesList, highestSimilarityScoresIndex)
  topEvidencesUrl = findTopList(filteredUrlList, highestSimilarityScoresIndex)

  return topEvidences, topEvidencesUrl
