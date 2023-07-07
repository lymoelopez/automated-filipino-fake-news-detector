import numpy as np
from sentence_transformers import util
import torch


def findSimilarityScores(inputClaim, urlContentList, cosineSimilarityModel):

  maxNumberOfEvidences = 5
  numberOfEvidences = min(maxNumberOfEvidences, len(urlContentList))

  claimSentenceEmbeddings = cosineSimilarityModel.encode(inputClaim, convert_to_tensor=True)
  candidateEvidenceSentenceEmbeddings =  cosineSimilarityModel.encode(urlContentList, convert_to_tensor=True)

  similarityScores = util.cos_sim(claimSentenceEmbeddings, candidateEvidenceSentenceEmbeddings)[0]
  highestSimilarityScores, highestSimilarityScoresIndex = torch.topk(similarityScores, k=numberOfEvidences)

  return highestSimilarityScores.cpu().numpy(), highestSimilarityScoresIndex.cpu().numpy()
  
def findTopList(givenList, topIndex):
  numpyList = np.array(givenList)
  topList = numpyList[topIndex].tolist()
  return topList

def evidenceSelector(inputClaim, filteredSearchResults, cosineSimilarityModel):
 
  urlList, urlTitleList, urlBodyList = filteredSearchResults
  urlContentList = [urlTitle + " " + urlBody for urlTitle, urlBody  in zip(urlTitleList, urlBodyList)]
  highestSimilarityScores, highestSimilarityScoresIndex = findSimilarityScores(inputClaim, urlContentList, cosineSimilarityModel)

  topEvidencesContent = findTopList(urlContentList, highestSimilarityScoresIndex)
  topEvidencesUrl = findTopList(urlList, highestSimilarityScoresIndex)
  topEvidencesTitle = findTopList(urlTitleList, highestSimilarityScoresIndex)
  topEvidencesBody = findTopList(urlBodyList, highestSimilarityScoresIndex)

  topEvidences = [topEvidencesContent, topEvidencesUrl, topEvidencesTitle, topEvidencesBody]

  return topEvidences, highestSimilarityScores
