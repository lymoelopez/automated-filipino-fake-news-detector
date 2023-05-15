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

def findHighestSimilarityScores(inputClaim, extractedArticlesList, model):

  numberOfEvidences = findNumberOfEvidences(extractedArticlesList)

  similarityScores = findSimilarityScores(inputClaim, extractedArticlesList, model)
  highestSimilarityScoresIndex = np.argpartition(similarityScores,-numberOfEvidences)[-numberOfEvidences:]
  highestSimilarityScores = similarityScores[highestSimilarityScoresIndex]
  
  return  highestSimilarityScores, highestSimilarityScoresIndex

def sortIndexBasedOnOriginalList(indexList, originalList):
  sortedIndexList = indexList[np.argsort(originalList)[::-1]]
  return sortedIndexList

def findTopList(givenList, topIndex):
  numpyList = np.array(givenList)
  topList = numpyList[topIndex]
  return topList

def findTopEvidences(inputClaim, extractedArticlesList, filteredUrlList, model):

  highestSimilarityScores, highestSimilarityScoresIndex = findHighestSimilarityScores(inputClaim, extractedArticlesList, model)
  sortedHighestSimilarityScoresIndex  = sortIndexBasedOnOriginalList(highestSimilarityScoresIndex, highestSimilarityScores)

  topEvidences = findTopList(extractedArticlesList, sortedHighestSimilarityScoresIndex)
  topEvidencesUrl = findTopList(filteredUrlList, sortedHighestSimilarityScoresIndex)

  return topEvidences, topEvidencesUrl
