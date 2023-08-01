import discord
from discord.ext import commands
import json
import random

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual bot token from the Discord Developer Portal
DISCORD_BOT_TOKEN 
QUESTIONS_FILE = 'questions.json'


# Initialize the Discord bot
intents = discord.Intents.default()
intents.message_content = True  # This will allow the bot to listen for message content
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description="Send `!fermi`. Then you have 2 minutes to answer the question. Remember that your answer should be the power of ten that is closest to the answer to the question. Good luck :grin: !!")
    await ctx.send(embed=embed)

@bot.command()
async def fermi(ctx):
    print("Function Called")
    with open(QUESTIONS_FILE, 'r') as file:
        data = json.load(file)
    print("JSON Parsed")
    question_set = random.choice(list(data['questions'].keys()))
    print(question_set)
    question = random.choice(list(data['questions'][question_set].keys()))
    answer = data['questions'][question_set][question]
    
    embed=discord.Embed(title="Fermi Question", description=question, color=0xFF5733)
    await ctx.send(embed=embed)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        # Wait for the correct answer for 30 seconds
        user_response = await bot.wait_for('message', timeout=120.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Time's up! The correct answer was: **" + answer + "**")
    else:
        if int(user_response.content) == answer:
            await ctx.send(f"Correct! The answer was: **{answer}**")
        else:
            await ctx.send(f"Sorry, that's incorrect. The correct answer was: **{answer}**")

bot.run(DISCORD_BOT_TOKEN)
    
    
