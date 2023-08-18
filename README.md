# FermiBot

<a href="https://github.com/Nosma2520/FermiBot/blob/master/LICENSE">
    <img alt="GitHub" src="https://img.shields.io/github/license/Nosma2520/FermiBot">
  </a>
  <br/>
<a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Made%20With-Python%203.11.4-blue.svg?style=for-the-badge&logo=Python" alt="Made with Python 3.11.4">
  </a>     
  
  

   <br/>
This is a Discord bot specifically designed to practice for the Science Olympiad event Fermi Questions. In Fermi Questions, you are provided a type of estimation problem, where the answer is an educated guess using logical reasoning and minimal data. The bot will ask a Fermi question, and users have 2 minutes to respond with their answer in the form of the power of ten that is closest to the actual answer

## Prerequisites
1. Python 3.6 or higher is required.
2. `discord.py` library, which can be installed using pip:
```
pip install discord.py
```
## Setup
1. Obtain your Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

2. Clone or download this repository to your local machine.

3. Place your Discord bot token in the **`DISCORD_BOT_TOKEN`** variable inside the `bot.py` file.

## Usage
There are two options for using this bot: self-hosting  and using the hosted version. The main difference is that self-hosting is a bit more difficult, tedious, and expensive than using the hosted version. However, self-hosting give you more control over the bot and allows you to make your own customizations as you see fit.

### Using the Hosted Version
1. [Click the bot invite link here](https://discord.com/api/oauth2/authorize?client_id=714904355043803136&permissions=292058164288&scope=bot) and select the server you want to add the bot to. Also make sure you have the right permissions, Manage Server, to be able to add Discord Bots to your server.

### Self - Hosting:
1. Run the bot.py script:
```
python bot.py
```
2. The bot will log in and display a message indicating that it's ready.
3. Invite the bot to your Discord server using the OAuth2 URL generated in the [Discord Developer Portal](https://discord.com/developers/applications).
4. Type `!help` in any text channel on your server to get instructions.
5. Use the `!fermi` command to trigger the bot to ask a Scioly Fermi question.
6. The bot will present randomly selected question from the `questions.json` file and wait for a user response.
7. Users should respond with the power of ten that is closest to the actual answer within 2 minutes.
8. The bot will provide feedback on whether the answer is correct or incorrect.

## Important Note

Remember to keep your DISCORD_BOT_TOKEN private and ***DO NOT*** share them publicly. Also, ensure your bot has the necessary permissions to read messages and send messages in the channels where it will be active.

## Disclaimer
This bot is for educational and entertainment purposes only. The questions in the questions.json file have been used in previous Scioly competitions and are not of the bot owner's own making.

## License
This project is licensed under the [GNU General Public License v3.0](https://github.com/Nosma2520/FermiBot/blob/main/LICENSE)
