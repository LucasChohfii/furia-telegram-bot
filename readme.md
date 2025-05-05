# FURIA CS Bot

Bot do Telegram para fãs do time FURIA de Counter-Strike, fornecendo informações sobre jogadores, próximos jogos e links para redes sociais.

## Funcionalidades

- Ver estatísticas de jogadores
- Consultar informações do time
- Verificar próximos jogos
- Acessar redes sociais dos jogadores e do time
- Acessar a loja oficial

## Comandos disponíveis

- `/start` - Inicia o bot e mostra o menu principal
- `/help` - Mostra a lista de comandos disponíveis
- `/player [nome]` - Mostra estatísticas de um jogador específico
- `/redes` - Mostra links para redes sociais
- `/nextgame` - Mostra informações sobre o próximo jogo
- `/loja` - Link para a loja oficial da FURIA

## Instalação

1. Clone este repositório
```
git clone https://github.com/seu-usuario/furia-cs-bot.git
cd furia-cs-bot
```

2. Instale as dependências
```
pip install -r requirements.txt
```

3. Configure seu token do Telegram
   - Edite o arquivo `bot.py` e substitua o TOKEN pelo seu
   - Ou configure como variável de ambiente

4. Execute o bot
```
python bot.py
```

## Tecnologias utilizadas

- Python 3.9+
- python-telegram-bot 20.4

## Estrutura do projeto

- `bot.py` - Código principal do bot
- `requirements.txt` - Dependências do projeto
- `README.md` - Este arquivo

## Observação de segurança

⚠️ **IMPORTANTE**: O token do Telegram no código é apenas para exemplo e já foi revogado. Nunca compartilhe seu token real em repositórios públicos. Use variáveis de ambiente ou arquivos de configuração separados que não são enviados ao GitHub.