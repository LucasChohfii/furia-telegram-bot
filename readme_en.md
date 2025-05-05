# FURIA CS Bot

A Telegram bot for FURIA Counter-Strike team fans, providing information about players, upcoming matches, and social media links.

## Features

- View player statistics
- Check team information
- View upcoming matches
- Access social media of players and team
- Access the official store

## Available Commands

- `/start` - Start the bot and show the main menu
- `/help` - Show the list of available commands
- `/player [name]` - Show statistics for a specific player
- `/redes` - Show links to social media
- `/nextgame` - Show information about the next match
- `/loja` - Link to the official FURIA store

## Installation

1. Clone this repository
```
git clone https://github.com/your-username/furia-cs-bot.git
cd furia-cs-bot
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Configure your Telegram token
   - Edit the `bot.py` file and replace the TOKEN with yours
   - Or set it as an environment variable

4. Run the bot
```
python bot.py
```

## Technologies Used

- Python 3.9+
- python-telegram-bot 20.4

## Project Structure

- `bot.py` - Main bot code
- `requirements.txt` - Project dependencies
- `README.md` - This file

## Security Note

⚠️ **IMPORTANT**: The Telegram token in the code is just an example and has been revoked. Never share your real token in public repositories. Use environment variables or separate configuration files that are not sent to GitHub.