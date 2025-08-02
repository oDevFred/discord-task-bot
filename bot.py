import os
import discord

from discord.ext import commands
from dotenv import load_dotenv
from cogs.tasks import TaskCog

# Carrega as variáveis de ambiente
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configura intents
intents = discord.Intents.default()
intents.message_content = True

# Iniciar o bot com o prefixo !
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento: Bot está pronto
@bot.event
async def on_ready():
    print(f'Bot conectado com {bot.user.name}')
    print('Carregando TaskCog...')
    await bot.add_cog(TaskCog(bot))
    print('TaskCog carregado!')

# Comando: !ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Iniciar bot
bot.run(TOKEN)