import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "$", intents=intents)

@bot.event
async def on_ready():
    print("Я готов!")


@bot.command()
async def hello(ctx):
    await ctx.send("Привет, человек!")


@bot.command()
async def bye(ctx):
    await ctx.send("Пока, человек!")


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run("MTE1NTQ0MzU1MzIzMzc5NzE0MA.GKD7u5.-hfEHSAXao3KiJLwH-vMxa3BVkAzCeuUHF--KE")


