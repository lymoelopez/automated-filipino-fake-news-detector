from newspaper import Article
from newspaper import Config
import requests
import time


def articleExtractor(url, articleExtractorConfig):

  try:
    article = Article(url, config=articleExtractorConfig)
    article.download()
    article.parse()

  except requests.exceptions.HTTPError as error:

    if error.response.status_code == 429:
      print("Too many requests. Waiting for a while before trying again . . . ")
      time.sleep(5)
      return articleExtractor(url, articleExtractorConfig)
    else:
      raise error

  except:
    return ""

  return article.text

def createExtractedArticlesList(urlList):

  extractedArticlesList = []

  articleExtractorConfig = Config()
  articleExtractorConfig.requests_timeout = 30

  for url in urlList:
    extractedArticlesList.append(articleExtractor(url, articleExtractorConfig))

  return extractedArticlesList
