rom sentence_transformers import SentenceTransformer
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
    # input_variables=["evidence", "claim", "currentDate"],
    input_variables=["evidence", "claim"],
    template=promptStringTemplate
  )

  llmHuggingFacePipeline = findLLMHuggingFacePipeline(llmModelID)
  llm = HuggingFacePipeline(pipeline=llmHuggingFacePipeline)

  llmWithPromptTemplate = LLMChain(prompt=llmPromptTemplate, llm=llm)

  return llm, llmWithPromptTemplate

def automatedFakeNewsConfig(
    urlBanList = ["facebook", "twitter", "youtube", "blog", "tiktok", "instagram", "youtu.be", "mp4", "mp3", "audiobook", "podcast", "spotify", "slideshare", "github", "huggingface", "reddit", "bible", "dailymotion"],
    cosineSimilarityModelID = "danjohnvelasco/filipino-sentence-roberta-v1", 
    llmModelID = "google/flan-t5-base",
    currentDate = findCurrentDateInText(),
    llmQuestion = "Question: can the Claim be inferred from the given Evidence? ",
):
  
  promptStringTemplate = """Evidence: {evidence}

      Claim: {claim}

      """ + f"""Current Date: {currentDate}

      """ + llmQuestion

  cosineSimilarityModel = SentenceTransformer(cosineSimilarityModelID)
  llm, llmWithPromptTemplate  = findLLM(llmModelID, promptStringTemplate)

  return urlBanList, cosineSimilarityModel, llm, llmWithPromptTemplate
