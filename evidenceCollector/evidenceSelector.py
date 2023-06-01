from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def findSimilarityScores(inputClaim, urlContentList, cosineSimilarityModel):

  # append claim in front of url body/content list
  sentences = list(urlContentList)
  sentences.insert(0, inputClaim)
  sentenceEmbeddings = cosineSimilarityModel.encode(sentences)

  similarityScores = cosine_similarity(
      [sentenceEmbeddings[0]],
      sentenceEmbeddings[1:]
  )

  return similarityScores[0]

def findNumberOfEvidences(urlContentList):

  numberOfArticles = len(urlContentList)

  if numberOfArticles > 5:
    numberOfEvidences = 5
  else:
    numberOfEvidences = numberOfArticles

  return numberOfEvidences

def findHighestSimilarityScores(inputClaim, urlContentList, cosineSimilarityModel):

  numberOfEvidences = findNumberOfEvidences(urlContentList)

  similarityScores = findSimilarityScores(inputClaim, urlContentList, cosineSimilarityModel)
  highestSimilarityScoresIndex = np.argpartition(similarityScores,-numberOfEvidences)[-numberOfEvidences:]
  highestSimilarityScores = similarityScores[highestSimilarityScoresIndex]
  
  return  highestSimilarityScores, highestSimilarityScoresIndex

def sortIndexBasedOnOriginalList(originalList, indexList):
  sortedIndexList = indexList[np.argsort(originalList)[::-1]]
  return sortedIndexList

def findTopList(givenList, topIndex):
  numpyList = np.array(givenList)
  topList = numpyList[topIndex].tolist()
  return topList

def evidenceSelector(inputClaim, urlContentList, urlList, cosineSimilarityModel):

  highestSimilarityScores, highestSimilarityScoresIndex = findHighestSimilarityScores(inputClaim, urlContentList, cosineSimilarityModel)
  sortedHighestSimilarityScoresIndex  = sortIndexBasedOnOriginalList(highestSimilarityScores, highestSimilarityScoresIndex)

  topEvidences = findTopList(urlContentList, sortedHighestSimilarityScoresIndex)
  topEvidencesUrl = findTopList(urlList, sortedHighestSimilarityScoresIndex)

  return topEvidences, topEvidencesUrl
