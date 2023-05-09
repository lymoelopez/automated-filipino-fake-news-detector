from webSearcher import *
from articleExtractor import *
from findTopFiveEvidences import *


def evidenceCollector(inputClaim, model):

  filteredUrlList = webSearcher(inputClaim, 20)
  extractedArticlesList = createExtractedArticlesList(filteredUrlList)
  topFiveEvidences = findTopFiveEvidences(inputClaim, extractedArticlesList, model)

  return filteredUrlList, extractedArticlesList, topFiveEvidences
