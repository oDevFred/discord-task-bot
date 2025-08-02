import discord
import asyncio
from discord.ext import commands, tasks
from database import Database
from datetime import datetime, date

class TaskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()
        self.check_reminders.start()

    def cog_unload(self):
        self.check_reminders.cancel()

    @tasks.loop(minutes=60) # Verifica a cada hora
    async def check_reminders(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            today = datetime.now().strftime('%Y-%m-%d')
            cursor.execute('SELECT id, user_id, description FROM tasks WHERE due_date = ?', (today,))
            tasks = cursor.fetchall()

        for task in tasks:
            task_id, user_id, description = task
            user = self.bot.get_user(user_id)
            if user:
                try:
                    await user.send(f"Lembrete: A tarefa '{description}' (ID: {task_id}) vence hoje!")
                except discord.errors.Forbidden:
                    print(f"Não foi possível enviar DM para o usuário {user_id}")

    @check_reminders.before_loop
    async def before_check_reminders(self):
        await self.bot.wait_until_ready()

    @commands.command()
    async def add_task(self, ctx, *, description_and_date=None):
        if not description_and_date:
            await ctx.send('Porfavor, forneça uma descrição para a tarefa.')
            return

        # Separar descrição e data
        parts = description_and_date.rsplit(' ', 1)
        description = description_and_date
        due_date = None
        if len(parts) == 2:
            description, due_date = parts
            try:
                datetime.fromisoformat(due_date)
            except ValueError:
                await ctx.send('Formato de data inválido. Use AAAA-MM-DD (e.g., 2025-08-10)')
                return

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO tasks (user_id, description, due_date) VALUES (?, ?, ?)',
                (ctx.author.id, description, due_date)
            )
            conn.commit()
            await ctx.send(f'Tarefa adicionada: {description}')

    @commands.command()
    async def list_tasks(self, ctx):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, description, due_date FROM tasks WHERE user_id = ?', (ctx.author.id,))
            tasks = cursor.fetchall()

        if not tasks:
            await ctx.send("Você não tem tarefas.")
            return

        response = "Suas tarefas:\n"
        for task in tasks:
            task_id, description, due_date = task
            due_date_str = f" (Vence: {due_date})" if due_date else ""
            response += f"ID: {task_id} - {description}{due_date_str}\n"
        await ctx.send(response)

    @commands.command()
    async def remove_task(self, ctx, task_id: int):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', (task_id, ctx.author.id))
            if cursor.rowcount == 0:
                await ctx.send("Tarefa não encontrada ou não pertence a você.")
                return
            conn.commit()
            await ctx.send(f"Tarefa ID {task_id} removida.")