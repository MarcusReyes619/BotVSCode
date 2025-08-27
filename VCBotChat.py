import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from ChatTest import ChatBot
import Constance

# Setup intents
intents = discord.Intents.all()
intents.message_content = True  

# Create bot
bot = commands.Bot(command_prefix="!", intents=intents)

chat = ChatBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

# Command that takes an argument
@bot.command()
async def say(ctx, *, message: str):
    response = chat.Chat(message)
    await ctx.send(response)

@bot.command()
async def join(ctx):
    """Join the voice channel and play a file"""
    if ctx.author.voice:  # Check if user is in a VC
        channel = ctx.author.voice.channel

        # If already connected, reuse the voice client
        if ctx.voice_client is None:
            voice = await channel.connect()
        else:
            voice = ctx.voice_client

        # Play the file
        #source = FFmpegPCMAudio('lock in.mp3', executable="C:/Users/mreyes/Downloads/ffmpeg-master-latest-win64-gpl-shared/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe")
        #voice.play(source)
        playAduio('lock in.mp3', voice)
        await ctx.send("🎶 Now playing: lock in.mp3")
    else:
        await ctx.send("You must be in a voice channel!")

@bot.command()
async def leave(ctx):
    """Leave the voice channel"""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I’m not in a voice channel!")

#testing bot text to speach
@bot.command()
async def hotAndFun(ctx):
    chat.textToSpeach('All the girls are girling girling')
    
    
def playAduio(audio_file,voice):
    source = FFmpegPCMAudio(audio_file, executable="C:/Users/mreyes/Downloads/ffmpeg-master-latest-win64-gpl-shared/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe")
    voice.play(source)
    

# Run bot
bot.run(Constance.API_KEY_SERVICE)