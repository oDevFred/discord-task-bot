# Discord Task Bot

Um bot do Discord desenvolvido em Python com `discord.py` para gerenciamento de tarefas e estudos. Ele permite adicionar, listar e remover tarefas, enviar lembretes automáticos para prazos e executar sessões de Pomodoro (técnica de produtividade com ciclos de 25 minutos de trabalho e 5 minutos de pausa). O bot usa SQLite para armazenar tarefas e inclui logging para facilitar a depuração.

## Funcionalidades

- **Gerenciamento de Tarefas**:
    - Adicionar tarefas com descrição e data de vencimento opcional.
    - Listar todas as tarefas de um usuário.
    - Remover tarefas pelo ID.
- **Lembretes Automáticos**:
    - Envia mensagens diretas (DMs) no dia do vencimento das tarefas, verificando a cada hora.
- **Sistema de Pomodoro**:
    - Executa ciclos de 25 minutos de trabalho seguidos de 5 minutos de pausa, com suporte a 1–8 ciclos.
- **Logging**:
    - Registra eventos, comandos e erros em um arquivo `bot.log` e no console para depuração.
- **Modularização**:
    - Usa cogs do `discord.py` para organizar a lógica em módulos (`TasksCog` para tarefas e lembretes, `PomodoroCog` para Pomodoro).
- **Banco de Dados**:
    - Armazena tarefas em um banco SQLite local (`tasks.db`), leve e sem necessidade de servidor.

## Pré-requisitos

- **Python 3.8+**: Certifique-se de ter o Python instalado. Verifique com `python --version`.
- **Conta no Discord**: Crie um bot no [Discord Developer Portal](https://discord.com/developers/applications).
- **Git**: Para clonar o repositório (`git --version` para verificar).
- **Permissões do Bot**:
    - Intents: `Guilds`, `Messages`, `Message Content` (habilitar no Developer Portal).
    - Permissões no servidor: Ler mensagens, enviar mensagens, gerenciar mensagens.
- **Editor de Código**: Recomenda-se VS Code ou outro editor para facilitar o desenvolvimento.
- **Opcional**: Ferramenta para visualizar SQLite (e.g., [DB Browser for SQLite](https://sqlitebrowser.org/)).

## Instalação

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/oDevFred/discord-task-bot.git
    cd discord-task-bot
    ```
2. **Crie e ative um ambiente virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure o token do bot**:
    - Crie um arquivo `.env` na raiz do projeto com o conteúdo:
    ```txt
    DISCORD_TOKEN=seu_token_aqui
    ```
    - Substitua `seu_token_aqui` pelo token do bot obtido no Discord Developer Portal.
5. **Inicie o bot**:
    ```bash
    python3 bot.py
    ```
    - No console, você verá: `Bot conectado como <nome_do_bot>`.

## Configuração do Bot no Discord

- **Acesse o Discord [Developer Portal](https://discord.com/developers/applications).**
- **Crie um novo aplicativo e adicione um bot na aba "Bot".**
- **Copie o token do bot e adicione ao arquivo `.env.`**
- **Na aba "Bot", habilite as intents**:
    - `Guilds`
    - `Messages`
    - `Message Content`

- **Na aba "OAuth2 > URL Generator"**:
    - Selecione **bot** como escopo.
    Escolha permissões: `Read Messages/View Channels`, `Send Messages`, `Manage Messages`.
    Copie o URL gerado e use-o para convidar o bot ao seu servidor.

## Estrutura do Projeto
```txt
    discord-task-bot/
    ├── cogs/                  # Módulos (cogs) para comandos
    │   ├── tasks.py           # Comandos de tarefas e lembretes
    │   └── pomodoro.py        # Comando Pomodoro
    ├── .env                   # Token do bot (não versionado)
    ├── .gitignore             # Arquivos a serem ignorados pelo Git
    ├── requirements.txt       # Dependências do projeto
    ├── bot.py                 # Script principal do bot
    ├── database.py            # Lógica de gerenciamento do SQLite
    ├── bot.log                # Logs de eventos e erros
    ├── tasks.db               # Banco de dados SQLite
    ├── README.md              # Documentação do projeto
```
## Comandos
| Comando                          | Descrição                                                                 | Exemplo de Uso                              |
|----------------------------------|---------------------------------------------------------------------------|---------------------------------------------|
| `!ping`                          | Testa se o bot está ativo, respondendo com "Pong!".                       | `!ping`                                     |
| `!add_task <descrição> [data]`   | Adiciona uma tarefa. A data (opcional) deve ser no formato `AAAA-MM-DD`.   | `!add_task Estudar Python 2025-08-10`       |
| `!list_tasks`                    | Lista todas as tarefas do usuário.                                        | `!list_tasks`                               |
| `!remove_task <id>`              | Remove uma tarefa pelo ID.                                                | `!remove_task 1`                            |
| `!pomodoro [ciclos]`             | Inicia uma sessão Pomodoro (padrão: 4 ciclos). Ciclos entre 1 e 8.        | `!pomodoro 2`                               |

### Exemplos de Uso

1. **Adicionar uma tarefa**:
   ```
   !add_task Estudar Python 2025-08-10
   ```
   **Resposta**:
   ```
   Tarefa adicionada: Estudar Python
   ```

2. **Listar tarefas**:
   ```
   !list_tasks
   ```
   **Resposta**:
   ```
   Suas tarefas:
   ID: 1 - Estudar Python (Vence: 2025-08-10)
   ```

3. **Remover uma tarefa**:
   ```
   !remove_task 1
   ```
   **Resposta**:
   ```
   Tarefa ID 1 removida.
   ```

4. **Lembrete (enviado via DM no dia do vencimento)**:
   ```
   Lembrete: A tarefa 'Estudar Python' (ID: 1) vence hoje!
   ```

5. **Iniciar Pomodoro**:
   ```
   !pomodoro 2
   ```
   **Resposta**:
   ```
   Iniciando Pomodoro: 2 ciclos de 25 min de trabalho + 5 min de pausa.
   Ciclo 1/2: Iniciando 25 minutos de trabalho!
   ```

## Lembretes

- O bot verifica tarefas com vencimento no dia atual a cada hora e envia mensagens diretas (DMs) aos usuários.
- Certifique-se de que as DMs estão habilitadas para o bot nas suas configurações de privacidade do Discord.

## Depuração

- **Logs**: Todos os eventos, comandos e erros são registrados em `bot.log` e exibidos no console. Exemplo de log:
  ```
  2025-08-02 00:45:00,000 - INFO - Bot conectado como TaskBot
  2025-08-02 00:45:05,000 - INFO - Tarefa adicionada por @usuário: Estudar Python
  ```
- **Verificar o banco SQLite**:
  - Use uma ferramenta como DB Browser for SQLite ou o comando:
    ```bash
    sqlite3 tasks.db "SELECT * FROM tasks;"
    ```
  - A tabela `tasks` contém: `id` (auto-incrementado), `user_id` (ID do usuário no Discord), `description` (texto), `due_date` (data no formato `AAAA-MM-DD` ou nulo).

### Problemas Comuns e Soluções

1. **Erro: `discord.errors.LoginFailure: Invalid token`**  
   - **Causa**: Token inválido no arquivo `.env`.  
   - **Solução**: Verifique o token no Discord Developer Portal, atualize `.env` e reinicie o bot.

2. **Erro: `discord.errors.PrivilegedIntentsRequired`**  
   - **Causa**: Intents (`Message Content`) não habilitadas.  
   - **Solução**: Habilite `Message Content Intent` na aba "Bot" do Developer Portal.

3. **Erro: Bot não responde a comandos**  
   - **Causa**: Permissões insuficientes ou intents incorretas.  
   - **Solução**:
     - Confirme que o bot tem permissões de leitura e escrita no canal.
     - Verifique se `intents.message_content = True` está em `bot.py`.
     - Adicione logs em `bot.py` para depuração: `logger.info("Comando recebido")`.

4. **Erro: `sqlite3.OperationalError: unable to open database file`**  
   - **Causa**: Permissões insuficientes ou caminho inválido para `tasks.db`.  
   - **Solução**:
     - Verifique permissões da pasta com `ls -l` (Linux/Mac) ou `dir` (Windows).
     - Use um caminho absoluto para `tasks.db` em `database.py` (e.g., `/caminho/para/projeto/tasks.db`).

5. **Erro: Lembretes não são enviados**  
   - **Causa**: Tarefa de verificação de lembretes não iniciada ou DMs bloqueadas.  
   - **Solução**:
     - Confirme que `check_reminders.start()` está em `TasksCog.__init__`.
     - Habilite DMs nas configurações de privacidade do Discord.
     - Adicione logs em `check_reminders` para depuração.

6. **Erro: `PermissionError` ao escrever em `bot.log`**  
   - **Causa**: Permissões insuficientes na pasta do projeto.  
   - **Solução**: Verifique permissões da pasta e execute o bot com permissões de escrita.

## Desenvolvimento

- **Tecnologias**:
  - **Python e discord.py**: Biblioteca assíncrona para interagir com a API do Discord, semelhante ao `discord.js` em Node.js.
  - **SQLite**: Banco de dados leve, sem servidor, armazenado em `tasks.db`. Comparado ao PostgreSQL, a sintaxe SQL é idêntica, mas o SQLite é mais simples, ideal para projetos pequenos.
  - **Cogs**: Módulos (`TasksCog`, `PomodoroCog`) organizam comandos e eventos, como módulos em Node.js ou classes em Python.
  - **Logging**: Usa o módulo `logging` do Python, análogo ao `winston` em Node.js.

- **Extensões Futuras**:
  - Adicionar comando para pausar/resumir Pomodoro.
  - Suporte a lembretes personalizados (e.g., 1 dia antes do vencimento).
  - Interface com embeds para melhor formatação de mensagens.

## Contribuindo

1. Faça um fork do repositório.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`.
3. Commit suas mudanças: `git commit -m "Adicionada funcionalidade X"`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um Pull Request descrevendo suas alterações.

Por favor, siga as boas práticas:
- Escreva código limpo e comentado.
- Adicione testes para novas funcionalidades.
- Atualize o `README.md` com novas instruções, se necessário.

## Deploy

Para hospedar o bot 24/7, considere:
- **VPS**: Use serviços como Heroku, DigitalOcean ou Railway.
- **Gerenciador de processos**: Use `nohup` (Linux) ou `pm2` para manter o bot ativo.
- **Monitoramento**: Verifique `bot.log` regularmente para identificar erros.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Veja o arquivo `LICENSE` para mais detalhes.

## Agradecimentos

- Desenvolvido com [discord.py](https://discordpy.readthedocs.io/).
- Inspirado na técnica Pomodoro e nas necessidades de estudantes e profissionais para gerenciar tarefas.

---

**Desenvolvido por**: [oDevFred](https://odevfred.github.io/portifolio/)
**Contato**: [Email](mailto:caio.frederico2001@outlook.com) 
**Última Atualização**: Agosto de 2025