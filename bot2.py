from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = "7953398458:AAHSfgX8eU7F4HfBadFFCDoztzJTtxRqKMM"

PLAYER_DATA = {
    "fallen": {
        "stats": ("Estatísticas de FalleN:\n"
                 "👤 Nome: Gabriel Toledo\n"
                 "🇧🇷 Nacionalidade: Brasileiro\n"
                 "📈 Rating: 1.05\n"
                 "🔫 K/D Ratio: 1.13\n"
                 "🎮 Função: IGL / Rifler"),
        "social": ("Redes Sociais de FalleN:\n"
                  "📷Instagram: https://www.instagram.com/fallen\n"
                  "🐦‍⬛X: https://x.com/FalleNCS\n"
                  "🎥Twitch: https://www.twitch.tv/gafallen\n"
                  "📺Youtube: https://www.youtube.com/@fallenINSIDER")
    },
    "yuurih": {
        "stats": ("Estatísticas de yuurih:\n"
                 "👤 Nome: Yuri Santos\n"
                 "🇧🇷 Nacionalidade: Brasileiro\n"
                 "📈 Rating: 1.16\n"
                 "🔫 K/D Ratio: 1.16\n" 
                 "🎮 Função: Rifler"),
        "social": ("Redes Sociais de yuurih:\n"
                  "📷Instagram: https://www.instagram.com/yuurihfps\n"
                  "🐦‍⬛X: https://x.com/yuurih\n"
                  "🎥Twitch: https://www.twitch.tv/yuurih")
    },
    "kscerato": {
        "stats": ("Estatísticas de KSCERATO:\n"
                 "👤 Nome: Kaike Cerato\n"
                 "🇧🇷 Nacionalidade: Brasileiro\n"
                 "📈 Rating: 1.19\n"
                 "🔫 K/D Ratio: 1.25\n"
                 "🎮 Função: Rifler"),
        "social": ("Redes Sociais de KSCERATO:\n"
                  "📷Instagram: https://www.instagram.com/kscerato\n"
                  "🐦‍⬛X: https://x.com/kscerato\n"
                  "🎥Twitch: https://www.twitch.tv/kscerato")
    },
    "yekindar": {
        "stats": ("Estatísticas de YEKINDAR:\n"
                 "👤 Nome: Mareks Gaļinskis\n"
                 "🇱🇻 Nacionalidade: Letão\n"
                 "📈 Rating: 1.12\n"
                 "🔫 K/D Ratio: 1.05\n"
                 "🎮 Função: Entry Fragger"),
        "social": ("Redes Sociais de YEKINDAR:\n"
                  "📷Instagram: https://www.instagram.com/yek1ndar\n"
                  "🐦‍⬛X: https://x.com/yek1ndar\n"
                  "🎥Twitch: https://www.twitch.tv/yekindar")
    },
    "molodoy": {
        "stats": ("Estatísticas de molodoy:\n"
                 "👤 Nome: Danil Golubenko\n"
                 "🇰🇿 Nacionalidade: Cazaquistanês\n"
                 "📈 Rating: 1.21\n"
                 "🔫 K/D Ratio: 1.35\n"
                 "🎮 Função: AWPer"),
        "social": ("Redes Sociais de molodoy:\n"
                  "📷Instagram: https://www.instagram.com/danil.molodoy_\n"
                  "🐦‍⬛X: https://x.com/tvoy_molodoy\n"
                  "🎥Twitch: https://www.twitch.tv/molodoy1818")
    },
    "sidde":{
        "stats": ("Estatísticas de Sidde:\n"
                 "👤 Nome: Sid Macedo\n"
                 "🇧🇷 Nacionalidade: Brasileiro\n"
                 "🎮 Função: Coach"),
        "social": ("Redes Sociais de Sidde:\n"
                  "📷Instagram: https://www.instagram.com/siddecs\n"
                  "🐦‍⬛X: https://x.com/siddecs\n"
                  "🎥Twitch: https://www.twitch.tv/siddecs")
    }
}

TEAM_DATA = {
    "stats": ("Estatísticas da FURIA:\n"
             "🟠 Valve ranking: #20\n"
             "🌐 World ranking: #17\n"
             "👥 Line-up atual: FalleN, yuurih, KSCERATO, YEKINDAR, molodoy\n"
             "👨‍💼 Coach: Sidde"),
    "social": ("Redes Sociais da FURIA:\n"
              "📷Instagram: https://www.instagram.com/furiagg\n"
              "🐦‍⬛X: https://x.com/FURIA\n"
              "🎵Tiktok: https://www.tiktok.com/@furiagg\n"
              "🎥Twitch: https://www.twitch.tv/furiatv\n"
              "📺Youtube: https://www.youtube.com/@FURIAggCS")
}

NEXT_GAME_INFO = ("🎮PRÓXIMOS JOGOS DA FURIA🎮\n\n"
                 "🏆Campeonato: PGL Astana 2025\n"
                 "⚔️Partida: FURIA vs The MongolZ\n" \
                 "📅Data: 10/05\n"
                 "⏰Horário: 5:00\n"
                 "🎥Assistir: Twitch/Youtube: Gaules")

SHOP_URL = "https://www.furia.gg/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando de inicialização do bot."""
    keyboard = [
        [
            InlineKeyboardButton("Jogadores 👤", callback_data="menu_players"),
            InlineKeyboardButton("Próximo Jogo 🎮", callback_data="next_game")
        ],
        [
            InlineKeyboardButton("Redes Sociais 🌐", callback_data="menu_social"),
            InlineKeyboardButton("Loja FURIA 🛒", callback_data="shop")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard) 
    mensagem = ("Fala, fã da Furia! 👊 Preparado para dominar o servidor?\n\n"
                "Escolha uma opção abaixo ou utilize /help para ver a lista de comandos disponíveis!📋")
    await update.message.reply_text(mensagem, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "📋 Lista de comandos disponíveis:\n\n"
        "/start - Inicia o bot e mostra o menu principal 🚀\n"
        "/player [nome] - Saber mais sobre um jogador da FURIA 👤\n"
        "/redes - Redes sociais de nossos players 🌐\n"
        "/nextgame - Ver o próximo jogo 🎯\n"
        "/loja - Acessar a loja oficial da FURIA 🛒")
    await update.message.reply_text(mensagem)

async def player_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        mensagem = ("Digite /player seguido pelo nome do jogador para ver suas estatísticas.\n\n"
                   "Opções disponíveis:\n"
                   "• FURIA (sobre o time)\n"
                   "• FalleN\n"
                   "• yuurih\n"
                   "• KSCERATO\n"
                   "• YEKINDAR\n"
                   "• molodoy\n"
                   "• Sidde\n\n"
                   "Exemplo: /player FalleN")
        await update.message.reply_text(mensagem)
        return
        
    player_name = " ".join(context.args).lower()
    player_found = False
    
    if player_name in ["furia", "time", "equipe", "team"]:
        await update.message.reply_text(TEAM_DATA["stats"])
        player_found = True
    else:
        for name, data in PLAYER_DATA.items():
            if player_name == name or player_name in name:
                await update.message.reply_text(data["stats"])
                player_found = True
                break
    
    if not player_found:
        mensagem = f"Informação sobre '{' '.join(context.args)}' não encontrada. Use /player para ver todas as opções disponíveis."
        await update.message.reply_text(mensagem)

async def redes_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("FURIA (Time)", callback_data="social_furia")],
        [
            InlineKeyboardButton("FalleN", callback_data="social_fallen"),
            InlineKeyboardButton("yuurih", callback_data="social_yuurih")
        ],
        [
            InlineKeyboardButton("KSCERATO", callback_data="social_kscerato"),
            InlineKeyboardButton("YEKINDAR", callback_data="social_yekindar")
        ],
        [
            InlineKeyboardButton("molodoy", callback_data="social_molodoy"),
            InlineKeyboardButton("Sidde", callback_data="social_sidde")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    mensagem = "Selecione para ver as redes sociais:"
    await update.message.reply_text(mensagem, reply_markup=reply_markup)

async def nextgame_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔔 Lembrar deste jogo", callback_data="reminder_next_game")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(NEXT_GAME_INFO, reply_markup=reply_markup)

async def loja_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🛒 Acessar a Loja Oficial", url=SHOP_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    mensagem = "🛒 LOJA OFICIAL FURIA 🛒\n\nClique abaixo para acessar a loja oficial da FURIA:"
    await update.message.reply_text(mensagem, reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    
    if callback_data == "menu_main":
        await show_main_menu(query)
    elif callback_data == "menu_players":
        await show_players_menu(query)
    elif callback_data.startswith("player_"):
        player_name = callback_data.split("_")[1]
        await show_player_stats(query, player_name)
    elif callback_data == "next_game":
        await show_next_game(query)
    elif callback_data == "reminder_next_game":
        await set_game_reminder(query)
    elif callback_data == "menu_social":
        await show_social_menu(query)
    elif callback_data.startswith("social_"):
        name = callback_data.split("_")[1]
        await show_social_media(query, name)
    elif callback_data == "shop":
        await redirect_to_shop(query)

async def show_main_menu(query):
    keyboard = [
        [
            InlineKeyboardButton("Jogadores 👤", callback_data="menu_players"),
            InlineKeyboardButton("Próximo Jogo 🎮", callback_data="next_game")
        ],
        [
            InlineKeyboardButton("Redes Sociais 🌐", callback_data="menu_social"),
            InlineKeyboardButton("Loja FURIA 🛒", callback_data="shop")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    mensagem = ("Fala, fã da Furia! 👊 O que mais você gostaria de saber?\n\n"
                "Escolha uma opção abaixo:")
    
    await query.edit_message_text(mensagem, reply_markup=reply_markup)

async def show_players_menu(query):
    keyboard = [
        [InlineKeyboardButton("FURIA (Time)", callback_data="player_furia")],
        [
            InlineKeyboardButton("FalleN", callback_data="player_fallen"),
            InlineKeyboardButton("yuurih", callback_data="player_yuurih")
        ],
        [
            InlineKeyboardButton("KSCERATO", callback_data="player_kscerato"),
            InlineKeyboardButton("YEKINDAR", callback_data="player_yekindar")
        ],
        [
            InlineKeyboardButton("molodoy", callback_data="player_molodoy"),
            InlineKeyboardButton("Sidde (Coach)", callback_data="player_sidde")
        ],
        [InlineKeyboardButton("Voltar", callback_data="menu_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Selecione para ver estatísticas:", reply_markup=reply_markup)

async def show_player_stats(query, player_name):
    keyboard = [[InlineKeyboardButton("Voltar para jogadores", callback_data="menu_players")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if player_name in PLAYER_DATA:
        await query.edit_message_text(PLAYER_DATA[player_name]["stats"], reply_markup=reply_markup)
    elif player_name == "furia":
        await query.edit_message_text(TEAM_DATA["stats"], reply_markup=reply_markup)
    else:
        await query.edit_message_text(f"Informações para {player_name} não encontradas.", reply_markup=reply_markup)

async def show_next_game(query):
    keyboard = [
        [InlineKeyboardButton("🔔 Lembrar deste jogo", callback_data="reminder_next_game")],
        [InlineKeyboardButton("Voltar ao Menu", callback_data="menu_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(NEXT_GAME_INFO, reply_markup=reply_markup)

async def set_game_reminder(query):
    keyboard = [[InlineKeyboardButton("Voltar ao Menu", callback_data="menu_main")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    mensagem = ("✅ Lembrete configurado!\n\n"
                "Vamos te avisar 30 minutos antes do jogo da FURIA vs The MongolZ")
    
    await query.edit_message_text(mensagem, reply_markup=reply_markup)

async def show_social_menu(query):
    keyboard = [
        [InlineKeyboardButton("FURIA (Time)", callback_data="social_furia")],
        [
            InlineKeyboardButton("FalleN", callback_data="social_fallen"),
            InlineKeyboardButton("yuurih", callback_data="social_yuurih")
        ],
        [
            InlineKeyboardButton("KSCERATO", callback_data="social_kscerato"),
            InlineKeyboardButton("YEKINDAR", callback_data="social_yekindar")
        ],
        [
            InlineKeyboardButton("molodoy", callback_data="social_molodoy"),
            InlineKeyboardButton("Sidde", callback_data="social_sidde")
        ],
        [InlineKeyboardButton("Voltar", callback_data="menu_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Selecione para ver as redes sociais:", reply_markup=reply_markup)

async def show_social_media(query, name):
    keyboard = [[InlineKeyboardButton("Voltar às redes sociais", callback_data="menu_social")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if name in PLAYER_DATA:
        await query.edit_message_text(PLAYER_DATA[name]["social"], reply_markup=reply_markup)
    elif name == "furia":
        await query.edit_message_text(TEAM_DATA["social"], reply_markup=reply_markup)
    else:
        await query.edit_message_text(f"Redes sociais para {name} não encontradas.", reply_markup=reply_markup)

async def redirect_to_shop(query):
    keyboard = [
        [InlineKeyboardButton("🛒 Acessar a Loja Oficial", url=SHOP_URL)],
        [InlineKeyboardButton("Voltar ao Menu", callback_data="menu_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    mensagem = "🛒 LOJA OFICIAL FURIA 🛒\n\nClique abaixo para acessar a loja oficial da FURIA:"
    await query.edit_message_text(mensagem, reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("player", player_command))
    app.add_handler(CommandHandler("redes", redes_command))
    app.add_handler(CommandHandler("nextgame", nextgame_command))
    app.add_handler(CommandHandler("loja", loja_command))
    app.add_handler(CallbackQueryHandler(button_callback))

    print("Bot está funcionando...")
    app.run_polling()

if __name__ == "__main__":
    main()