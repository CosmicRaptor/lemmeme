import discord
from discord.ext import commands, tasks
from discord import app_commands
from utils.memes_aiohttp_parser import getMemes
from utils.memebuttons import Buttons, RandomButtons
import random


class Memes(commands.Cog):
    memes = {}

    def __init__(self, client: commands.Cog):
        self.client = client
        self.memesTask.start()

    @tasks.loop(minutes=15)
    async def memesTask(self):
        Memes.memes = await getMemes()

    @app_commands.command(name='meme')
    @app_commands.choices(algorithm=[
        app_commands.Choice(name="Hot", value="Hot"),
        app_commands.Choice(name="Active", value="Active"),
        app_commands.Choice(name="TopDay", value="TopDay"),
        app_commands.Choice(name="New", value="New"),
        app_commands.Choice(name="MostComments", value="MostComments")
    ])
    async def meme(self, interaction: discord.Interaction, algorithm: app_commands.Choice[str], randomness: bool = None):
        if randomness is None or not randomness:
            meme = Memes.memes[algorithm.value][0]
            embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
            embed.set_image(url=meme["link"])
            await interaction.response.send_message(algorithm, embed=embed, view=Buttons(interaction.user, Memes.memes[algorithm.value]))
        else:
            meme = random.choice(Memes.memes[algorithm.value])
            embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
            embed.set_image(url=meme["link"])
            await interaction.response.send_message(embed=embed, view=RandomButtons(interaction.user, Memes.memes[algorithm.value]))

    @commands.command()
    @commands.is_owner()
    async def startMemeTask(self, ctx):
        self.memesTask.start()
        await ctx.send("started")

    @commands.command()
    @commands.is_owner()
    async def stopMemeTask(self, ctx):
        self.memesTask.stop()
        await ctx.send("stopped")


async def setup(client: commands.Bot):
    await client.add_cog(Memes(client))
