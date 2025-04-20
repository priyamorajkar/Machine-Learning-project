import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyA2KjbYf5hO2np2pBfiOlqEF4C29GRXMSM")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
def GenerateResponse (input_text):
    response = model.generate_content([
    "input: who are you",
 "output: I am education chatbot",
  "input: what all can do?",
  "output: I can help with education related problem ,  how can I  help you ?",
  f"input: {input_text}",
  "output: ",
])

    return (response.text)
#while True:
#    string = str(input("Enter your prompt:"))
#    print(GenerateResponse(string))