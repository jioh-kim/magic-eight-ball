import discord 
import os
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()

#client = discord.Client()
client = commands.Bot(command_prefix='!')

embed_color=0xD13CDE

# do stuff
@Client.event 
async def on_ready():
    print("We are online!")

    general_channel = client.get_channel()
    await general_channel.send("Hello!")
    
@Client.command(name='magic8')
async def magic8(ctx):
    info_embed = discord.Embed(title='The magic 8-ball has been summoned',
    description='', color=embed_color)
    
    info_embed.add_field(name='Want to see your future?', value='Type !future', inline=False)
    
    info_embed.set_thumbnail(url-'https://giphy.com/clips/studiosoriginals-no-8LGaJzBF3aSgMcRkdt')
    
    await ctx.send(embed=info_embed)

@client.command(name='forture')
async def fortune(ctx,*question):
    if len(question) == 0:
        await ctx.send('I need you to ask a question!')
        
    index = randint(0,len(fortunes) -1)
    
    fortune_embed = discord.Embed(title = fortunes[index], description='', color=embed_color)
    
    await ctx.send(embed=fortune_embed)
    


BOT_TOKEN = os.getenv("TOKEN")
client.run(BOT_TOKEN)