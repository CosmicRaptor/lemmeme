import discord
from discord.ext import commands
from discord import app_commands
from utils.dadjoke import DadJoke

class DadJokeCog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.joke = DadJoke("text")

    group = app_commands.Group(name="dadjoke", description="get some jokes!")
    @group.command(name="random")
    async def randomjoke(self, interaction: discord.Interaction):
        await interaction.response.defer()
        joke = self.joke.randomjoke()
        await interaction.followup.send(joke)

    @group.command(name="search")
    async def searchjoke(self, interaction: discord.Interaction, query: str, limit: int = 20, page: int = 1):
        await interaction.response.defer()
        joke = self.joke.search(query, page, limit)
        await interaction.followup.send(joke)

async def setup(client: commands.Bot):
    await client.add_cog(DadJokeCog(client))