import Constance
import discord
from discord.ext import commands 
import json
import asyncio
import os



intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.voice_states = True
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

#voice recorder class
class VoiceRecorder(discord.AudioSink):
    def __init__(self,filename="recording.waw"):
        self.filename = filename
        self.file = open(filename, "wb")
        
    def write(self, data):
        self.file.write(data)

    def cleanup(self):
        self.file.close()
        

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    


@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        
        await channel.connect()
        await ctx.send(f"Joined {channel}")
    else:
        await ctx.send("You need to be in a voice channel!")


@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Left the voice channel.")
    else:
        await ctx.send("I'm not in a voice channel!")
        
#Recording command
@bot.command()
async def record(ctx):
    vc = ctx.voice_client
    if vc and vc.is_connected():
        
        #makes audio file
        audioSink = VoiceRecorder("output.pcm")
        
        vc.start_recording(audioSink, lambda e: print(f"Recording ended : {e}") if e else None)
        
        await ctx.send("Recoding started")
    else:
        await ctx.send("U need to be in a VC monkey")
        

#Stop recoding command
@bot.command()
async def stop(ctx):
    vc = ctx.voice_client
    
    if vc and vc.is_connected():
        vc.stop_recording()
        await ctx.send("recoding stop")
        
        #converts the PCM to a WAW file using ffmpeg
        os.system("ffmpeg -f s16le -ar 48000 -ac 2 -i output.pcm output.wav")
        await ctx.send("recoding saved as output.waw")
        
    else:
        await ctx.send("recoding wasnt started monkey")
        
bot.run(Constance.API_KEY_SERVICE)

    