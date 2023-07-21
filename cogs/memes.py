import discord
from discord.ext import commands,tasks
from discord import app_commands
from utils.memes_aiohttp_parser import getMemes
from collections import deque
import random

class Buttons(discord.ui.View):
    def __init__(self, user: discord.User):
        super().__init__()
        self.user = user
        self.user_dict = {
            user: 0
        }

    @discord.ui.button(label='Previous', style=discord.ButtonStyle.danger)
    async def previousmemebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user == self.user:
            try:
                memes = Memes.memes
                index = self.user_dict[interaction.user]
                self.user_dict[interaction.user] = index - 1
                meme = memes[index-1]
                embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
                embed.set_image(url=meme["link"])
                await interaction.response.edit_message(embed=embed)
            except IndexError:
                self.user_dict[interaction.user] = 0
                meme = memes[0]
                embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
                embed.set_image(url=meme["link"])
                await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message("Not your meme, run your own command!", ephemeral=True)

    @discord.ui.button(label='Next', style=discord.ButtonStyle.green)
    async def nextmemebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user == self.user:
            try:
                memes = Memes.memes
                index = self.user_dict[interaction.user]
                self.user_dict[interaction.user] = index + 1
                meme = memes[index+1]
                embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
                embed.set_image(url=meme["link"])
                await interaction.response.edit_message(embed=embed)
            except IndexError:
                self.user_dict[interaction.user] = -1
                meme = memes[-1]
                embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
                embed.set_image(url=meme["link"])
                await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message("Not your meme, run your own command!", ephemeral=True)
        



class RandomButtons(discord.ui.View):
    def __init__(self, user: discord.User):
        super().__init__()
        self.user = user

    @discord.ui.button(label="New", style=discord.ButtonStyle.blurple)
    async def randombutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user == self.user:
            meme = random.choice(Memes.memes)
            embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
            embed.set_image(url=meme["link"])
            await interaction.response.edit_message(embed=embed, view=RandomButtons())
        else:
            await interaction.response.send_message("Not your meme, run your own command!", ephemeral=True)

class Memes(commands.Cog):
    memes = []
    def __init__(self, client: commands.Cog):
        self.client = client
        self.meme_url = ['https://lemmy.ml/feeds/c/memes.xml?sort=Active' , 'https://lemmy.world/feeds/c/lemmyshitpost.xml?sort=Active']
        self.memesTask.start()

    @tasks.loop(minutes=15)
    async def memesTask(self):
        Memes.memes = await getMemes(self.meme_url)

    @app_commands.command(name='meme')
    async def meme(self, interaction: discord.Interaction, randomness: bool = None):
        if randomness is None or not randomness :
            meme = Memes.memes[0]
            embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
            embed.set_image(url=meme["link"])
            await interaction.response.send_message(embed=embed, view=Buttons(interaction.user))
        else:
            meme = random.choice(Memes.memes)
            embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
            embed.set_image(url=meme["link"])
            await interaction.response.send_message(embed=embed, view=RandomButtons(interaction.user))

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