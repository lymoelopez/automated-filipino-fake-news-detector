from datetime import date


def findCurrentDateInText():
  currentDate = date.today()
  currentDataInText = currentDate.strftime("%B %d %Y")
  return currentDataInText 

def findLLMmmessage(evidence, claim, llmWithPromptTemplate):
  currentDate = findCurrentDateInText()
  message = llmWithPromptTemplate.run({"evidence": evidence, "claim": claim, "currentDate": currentDate})
  return message

def llmClassifier (inputClaim, evidence, llmWithPromptTemplate):
  
  message = findLLMmmessage(evidence, inputClaim, llmWithPromptTemplate)

  if ("true" in message.strip().lower()) or ("yes" in message.strip().lower()):
    return 0
  else:
    return 1
