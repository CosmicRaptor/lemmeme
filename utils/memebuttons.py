import discord
import random

class Buttons(discord.ui.View):
    def __init__(self, user: discord.User, memes: list):
        super().__init__()
        self.user = user
        self.memes = memes
        self.user_dict = {
            user: 0
        }

    @discord.ui.button(label='Previous', style=discord.ButtonStyle.danger)
    async def previousmemebutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user == self.user:
            try:
                memes = self.memes
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
                memes = self.memes
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
    def __init__(self, user: discord.User, memes: list):
        super().__init__()
        self.user = user
        self.memes = memes

    @discord.ui.button(label="New", style=discord.ButtonStyle.blurple)
    async def randombutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user == self.user:
            meme = random.choice(self.memes)
            embed = discord.Embed(title=meme["title"], url=meme["id"], color=discord.Color.random())
            embed.set_image(url=meme["link"])
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message("Not your meme, run your own command!", ephemeral=True)