from openai import OpenAI
from pathlib import Path


client = OpenAI()

class ChatBot:
    def __init__(self):
        self.count = 0
        self.conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
        ]
    
    
    #Chat Function 
    def Chat(self,input):    
        self.conversation.append({"role": "user", "content": input})
        response =  client.chat.completions.create(
        model="gpt-5",
        messages= self.conversation
        )
      
         # Get assistant reply
        reply = response.choices[0].message.content
    
         # Add assistant reply to conversation
        self.conversation.append({"role": "assistant", "content": reply})
    
    
        
        return reply
    
    
    #Text To Speach Funtion
    def textToSpeach(self,input):
        speech_file_path = Path(__file__).parent / "speech.mp3"

        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="coral",
            input=input,
            instructions="Make it sound like your singing",
        ) as response:
            response.stream_to_file(speech_file_path)
            
    