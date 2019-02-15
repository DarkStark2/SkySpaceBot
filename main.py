import discord
from discord.ext import commands

token = 'NTQzODcwODA2MDIzNzMzMjc2.D0Dg-Q.SaisMmTREyHOmSSX-uIHXYlY3KI'

client = commands.Bot(command_prefix = "!")

extensions = ['cogs.ip', 'cogs.help']

@client.event
async def on_ready():
    game = discord.Game("!help | SkySpace")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print("Bot is ready.")

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print("Loaded {}".format(extension))
    except Exception as error:
        print ("{} cannot be loaded. [{}]".format(extension, error))

@client.command()
async def unload(extension): 
    try:
        client.load_extension(extension)
        print("Unloaded {}".format(extension))
    except Exception as error:
        print ("{} cannot be unloaded. [{}]".format(extension, error))

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
           print ("{} cannot be loaded. [{}]".format(extension, error)) 

    client.run(token)