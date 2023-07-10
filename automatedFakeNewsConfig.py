from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline
from datetime import date


def findCurrentDateInText():
  currentDate = date.today()
  currentDataInText = currentDate.strftime("%B %d %Y")
  return currentDataInText 

def findLLMHuggingFacePipeline(llmModelID, task="text2text-generation"):
  llmTokenizer = AutoTokenizer.from_pretrained(llmModelID)
  llmModel = AutoModelForSeq2SeqLM.from_pretrained(llmModelID)

  llmHuggingFacePipeline = pipeline(
      task,
      model=llmModel, 
      tokenizer=llmTokenizer, 
      max_length=100
  )

  return llmHuggingFacePipeline

def findLLM(llmModelID, promptStringTemplate):

  llmPromptTemplate = PromptTemplate(
    input_variables=["evidence", "claim"],
    template=promptStringTemplate
  )

  llmHuggingFacePipeline = findLLMHuggingFacePipeline(llmModelID)
  llm = HuggingFacePipeline(pipeline=llmHuggingFacePipeline)

  llmWithPromptTemplate = LLMChain(prompt=llmPromptTemplate, llm=llm)

  return llm, llmWithPromptTemplate

def automatedFakeNewsConfig(
    urlBanList = ["facebook.com", "twitter.com", "youtube.com", "blogspot.com", "tiktok.com", 
                  "instagram.com", "youtu.be","spotify.com", "slideshare.net", "github.com", "huggingface.com,", 
                  "reddit.com", "bible.com", "dailymotion.com", "/opinyon", "/opinion", 
                  "brainly.com", "quizlet.com", "dutertedefender.com", "dutertenews.com",
                  "du30worldwide.com", "du30newsblog.blogspot.com", "trendingbalita.info", 
                  "pinoyviralissues.net", "pinoyspeak.info", "newstitans.com", "mindanation.com", 
                  "phppoliticsnews.blogspot.com", "tahonews.com", "pinoynewsblogger.blogspott.com", 
                  "liberalpartysite.wordpress.com", "pinoyworld.net", "newsmediaph.com", 
                  "thevolatiliian.com", "socialnewsph.com", "leaknewsph.com", "du30newsinfo.com", 
                  "hotnewsphil.blogspot.com", "iampilipino.com", "trendingnewsportal-ph.blogspot.com", 
                  "kalyepinoy.com", "classifiedtrents.net", "ilikeyquotes.blogspot.com", "filipinewsph.com", 
                  "newsfeedsociety.tk", "pinoyfreedomwall.com", "philnewsportal.com", "ilikeyouquotes.blogspot.com", 
                  "pinoytrending.altervista.org", "pinoytrendingnews.net", "newstrendph.com", "asianpolicy.press", 
                  "publictrending.net", "trendingviral.tk", "newsinfolearn.com", "allthingspinoy.com", "todayinmanila.ga", 
                  "definitelyfilipino.com", "trendingnewsportal.net", "classifiedtrends.net", "philippinesinfinity.com", 
                  "reportph.com", "topnewsphil.com", "pilipinasnewsnetwork.com", "du30newsportal.com", "bidyoko.com", 
                  "philnewstrend.com", "food-health-365.com", "netizensph.com", "superworld18.xyz", "rap-fr.fr", 
                  "real8scoop.blogspot.com", "netviral.com", "ignitepinoy.com", "angatpinoy.info", "viralhubph.com", 
                  "artikuloph.com", "balitaph.info", "globalnews.favradiofm.com", "globalnews.favradio.fm", "themaharlikan.info", 
                  "inewser.com", "pinoythinking.info", "duterteviral.info", "balitangpinas.net", "okd2.com", "bbc101.c0m", 
                  "dwtcv3.com", "da1lymail.com", "thet1mes.com", "guard1an.com", "ondamic.com", "da1lymail.com", 
                  "sowhatsnews.wordpress.com", "adobochronicles.com", "thephilippinechronicle.com", "Balitangmaharlika.com", 
                  "GetRealPhilippines.com", "Thinkingpinoy.net", "Pinasheadlines.com", "Pinoytribune.blogspot.com", 
                  "trendsenthusiast.blogspot.com", "Newsinfomanila.com", "MNLTrend.blogspot.com", "Tribune.net.ph", 
                  "amazon.com", "olx.com", "wattpad.com", "ask.fm", "ebay.com", "twitch.tv", "discord.com"],
    cosineSimilarityModelID = "danjohnvelasco/filipino-sentence-roberta-v1", 
    llmModelID = "google/flan-t5-base",
    currentDate = findCurrentDateInText(),
    llmQuestion = "Question: is the claim true based on the given evidence? ",
):
  
  promptStringTemplate = """Evidence: {evidence}

      Claim: {claim}

      """ + f"""Current Date: {currentDate}

      """ + llmQuestion

  cosineSimilarityModel = SentenceTransformer(cosineSimilarityModelID)
  llm, llmWithPromptTemplate  = findLLM(llmModelID, promptStringTemplate)

  return urlBanList, cosineSimilarityModel, llm, llmWithPromptTemplate
