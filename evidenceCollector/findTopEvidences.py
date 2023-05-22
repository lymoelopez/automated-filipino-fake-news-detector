from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def findSimilarityScores(inputClaim, urlBodyList, cosineSimilarityModel):

  # append claim in front of url body/content list
  sentences = list(urlBodyList)
  sentences.insert(0, inputClaim)
  sentenceEmbeddings = cosineSimilarityModel.encode(sentences)

  similarityScores = cosine_similarity(
      [sentenceEmbeddings[0]],
      sentenceEmbeddings[1:]
  )

  return similarityScores[0]

def findNumberOfEvidences(urlBodyList):

  numberOfArticles = len(urlBodyList)

  if numberOfArticles > 5:
    numberOfEvidences = 5
  else:
    numberOfEvidences = numberOfArticles

  return numberOfEvidences

def findHighestSimilarityScores(inputClaim, urlBodyList, cosineSimilarityModel):

  numberOfEvidences = findNumberOfEvidences(urlBodyList)

  similarityScores = findSimilarityScores(inputClaim, urlBodyList, cosineSimilarityModel)
  highestSimilarityScoresIndex = np.argpartition(similarityScores,-numberOfEvidences)[-numberOfEvidences:]
  highestSimilarityScores = similarityScores[highestSimilarityScoresIndex]
  
  return  highestSimilarityScores, highestSimilarityScoresIndex

def sortIndexBasedOnOriginalList(originalList, indexList):
  sortedIndexList = indexList[np.argsort(originalList)[::-1]]
  return sortedIndexList

def findTopList(givenList, topIndex):
  numpyList = np.array(givenList)
  topList = numpyList[topIndex]
  return topList

def findTopEvidences(inputClaim, urlBodyList, urlList, cosineSimilarityModel):

  highestSimilarityScores, highestSimilarityScoresIndex = findHighestSimilarityScores(inputClaim, urlBodyList, cosineSimilarityModel)
  sortedHighestSimilarityScoresIndex  = sortIndexBasedOnOriginalList(highestSimilarityScores, highestSimilarityScoresIndex)

  topEvidences = findTopList(urlBodyList, sortedHighestSimilarityScoresIndex)
  topEvidencesUrl = findTopList(urlList, sortedHighestSimilarityScoresIndex)

  return topEvidences, topEvidencesUrl
