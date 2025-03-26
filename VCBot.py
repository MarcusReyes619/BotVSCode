# This example requires the 'message_content' intent.
import VC 
import discord
from discord.ext import commands
from discord import app_commands


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if(message.content == 'Luv Chaewon'):
            print('I NEED HER PLZ LORD')
            



intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

client = MyClient(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id= 1352515685028331530)

tree = app_commands.CommandTree(client)

@tree.command(name="hello", description = "Say Hello", guild=discord.Object(id= 1352515685028331530))
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("CHAEWON IS YOURS!!")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id= 1352515685028331530))
    print("Ready!")





client.run('MTM1MjUxMzYyNzI0NDA3Mjk3MQ.GpdsuV.N9hwtN15CUQNOjfU5uFfcEz6xAvryrqcwvpDUA')