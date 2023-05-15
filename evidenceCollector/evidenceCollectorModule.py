from webSearcher import *
from articleExtractor import *
from findTopEvidences import * 


def evidenceCollector(inputClaim, model, numOfSearchResults=20):

  filteredUrlList = webSearcher(inputClaim, numOfSearchResults)
  extractedArticlesList = createExtractedArticlesList(filteredUrlList)
  topEvidences, topEvidencesUrl = findTopEvidences(inputClaim, extractedArticlesList, filteredUrlList,model)

  return topEvidences, topEvidencesUrl
