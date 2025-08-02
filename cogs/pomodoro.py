import discord
import asyncio
from discord.ext import commands

class PomodoroCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pomodoro(self, ctx, cycles: int = 4):
        if cycles < 1 or cycles > 8:
            await ctx.send("O número de ciclos deve estar entre 1 e 8.")
            return

        await ctx.send(f"Iniciando Pomodoro: {cycles} ciclos de 25 min de trabalho + 5 min de pausa.")

        for i in range(cycles):
            # Trabalho: 25 minutos
            await ctx.send(f"Ciclo {i+1}/{cycles}: Iniciando 25 minutos de trabalho!")
            await asyncio.sleep(25 * 60)  # 25 minutos
            await ctx.send(f"Ciclo {i+1}/{cycles}: Fim do trabalho! Iniciando 5 minutos de pausa.")
            await asyncio.sleep(5 * 60)  # 5 minutos
            await ctx.send(f"Ciclo {i+1}/{cycles}: Fim da pausa!")

        await ctx.send("Pomodoro concluído! Ótimo trabalho!")