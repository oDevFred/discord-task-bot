import os
import discord
import logging

from discord.ext import commands
from dotenv import load_dotenv
from cogs.tasks import TaskCog
from cogs.pomodoro import PomodoroCog

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

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
    await bot.add_cog(TaskCog(bot))
    await bot.add_cog(PomodoroCog(bot))

# Comando: !ping
@bot.command()
async def ping(ctx):
    logger.info(f'Comando !ping executado por {ctx.author}')
    await ctx.send('Pong!')

# Iniciar bot
bot.run(TOKEN)