import discord

from discord.ext import commands
import os
import asyncio
import logging


client = commands.Bot(command_prefix=";", intents=discord.Intents.default())
client.help_command = commands.MinimalHelpCommand()

    
async def main():
    try:
        token=os.getenv("token")
        logging.basicConfig(level=logging.ERROR)
    except Exception as e:
        # Log exception to program logs
        print("Invalid Token: Set your token in token.env and rebuild")
        print(e)
    await load_cogs()
    await client.start(token)

    
async def load_cogs():
    for f in os.listdir("./cogs"):
        if f.endswith(".py"):
            await client.load_extension(f"cogs.{f[:-3]}")

            
@client.event
async def on_ready():
    print(f"Bot client has started")


    
@client.command()
@commands.is_owner()
async def syncLocally(ctx):
    ctx.bot.tree.copy_global_to(guild=ctx.guild)
    await ctx.bot.tree.sync(guild=ctx.guild)

@client.command()
@commands.is_owner()
async def syncGlobally(ctx):
    await ctx.bot.tree.sync()
    await ctx.send("Synced.")

    
@client.command()
@commands.is_owner()
async def reload(ctx):
    for f in os.listdir("./cogs"):
        if f.endswith(".py"):
            await client.reload_extension(f"cogs.{f[:-3]}")
    await ctx.send("Reloaded all cogs!")


asyncio.run(main())
