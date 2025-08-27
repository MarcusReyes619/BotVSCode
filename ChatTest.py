from openai import OpenAI
from pathlib import Path
client = OpenAI()

class ChatBot:
    def __init__(self):
        self.count = 0
        self.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
        ]
    
    
    #Chat Function 
    def Chat(self,input):    
        response = client.responses.create(
        model="gpt-4o-mini",
        input= input
        )
        #answer = response.choices[0].message.content
        #self.messages.append({"role": "assistant", "content": answer})
        
        return response.output_text
    
    
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