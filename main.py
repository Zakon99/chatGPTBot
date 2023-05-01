import os

import openai
from twitchio.ext import commands
#Oauth URL
oAuth_Url = 'https://id.twitch.tv/oauth2/authorize?client_id=<CLIENT_ID>&redirect_uri=http://localhost:3000&response_type=token&scope=chat:read+chat:edit'
#Twitch Credentials
twitch_username = '<BOTNAME>'
twitch_oauth_token = '<oAUTH_TOKEN>'
twitch_channel = 'marlonroyale'
twitch_clientId = '<CLIENT_ID>'
# OpenAI API-Konfiguration
openai_key = '<OPEN_API_KEY>'
chatgpt_model = 'gpt-3.5-turbo'

# Twitch-Client erstellen
bot = commands.Bot(
    token = twitch_oauth_token,
    client_id=twitch_clientId,
    nick=twitch_username,
    prefix='!',
    initial_channels=[twitch_channel]
)
# OpenAI-Client erstellen
openai.api_key = openai_key

@bot.command(name='gpt')
async def event_message(ctx):
    if ctx.author.name.lower != twitch_username.lower:
        message_content = ctx.message.content[6:]  # Remove the command prefix

        # OpenAI-ChatGPT-Anfrage stellen
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": message_content},
            ]
        )

        # Antwort vom ChatGPT-Modell erhalten
        answer = response.choices[0].message.content

        # Antwort im Twitch-Chat senden
        await ctx.reply(answer)

# Twitch-Client starten
bot.run()
