from typing import Final
import os
import discord
from dotenv import load_dotenv
from discord import Client, Message, Intents
from discord.ext import commands


load_dotenv()
TOKEN : Final = os.getenv("DISCORD_TOKEN")
flag : Final = os.getenv("FLAG")

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

def private_message_only():
    async def predicate(ctx):
        return isinstance(ctx.channel, discord.DMChannel)
    return commands.check(predicate)

bot = commands.Bot(command_prefix="!", intents = intents)


@bot.command()
@private_message_only()
async def galf(ctx):
    await ctx.send(flag)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

def main() -> None:
    bot.run(token=TOKEN)

if __name__ == "__main__":
    main()
