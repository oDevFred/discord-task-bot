import discord
import asyncio
import logging

from discord.ext import commands

logger = logging.getLogger(__name__)

class PomodoroCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        logger.info("PomodoroCog inicializado")

    @commands.command()
    async def pomodoro(self, ctx, cycles: int = 4):
        if cycles < 1 or cycles > 8:
            await ctx.send("O número de ciclos deve estar entre 1 e 8.")
            logger.warning(f"Número de ciclos inválido em !pomodoro por {ctx.author}: {cycles}")
            return

        await ctx.send(f"Iniciando Pomodoro: {cycles} ciclos de 25 min de trabalho + 5 min de pausa.")
        logger.info(f"Pomodoro iniciado por {ctx.author}: {cycles} ciclos")

        for i in range(cycles):
            # Trabalho: 25 minutos
            await ctx.send(f"Ciclo {i+1}/{cycles}: Iniciando 25 minutos de trabalho!")
            logger.info(f"Ciclo {i+1}/{cycles} iniciado para {ctx.author}")
            await asyncio.sleep(25 * 60)  # 25 minutos
            await ctx.send(f"Ciclo {i+1}/{cycles}: Fim do trabalho! Iniciando 5 minutos de pausa.")
            logger.info(f"Pausa do ciclo {i+1}/{cycles} iniciada para {ctx.author}")
            await asyncio.sleep(5 * 60)  # 5 minutos
            await ctx.send(f"Ciclo {i+1}/{cycles}: Fim da pausa!")
            logger.info(f"Pausa do ciclo {i+1}/{cycles} finalizada para {ctx.author}")

        await ctx.send("Pomodoro concluído! Ótimo trabalho!")
        logger.info(f"Pomodoro concluído por {ctx.author}")