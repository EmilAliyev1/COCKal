import asyncio, discord
import os
from typing import Final
from discord.ext import commands
from discord import *
from dotenv import load_dotenv
from responses import get_response
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient


load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)
tree = app_commands.CommandTree(client)


# @app_commands.command(name="play_cockal",description="DICKiy_pOs")
# async def ping(ctx: Interaction, have_account:bool, login_email:str=None, login_mobile:str=None):
#     user=ctx.message.author
#     voice_channel=user.voice.voice_channel
#     pass_context=True
#     channel=None
#     # only play music if user is in a voice channel
#     if voice_channel!= None:
#         # grab user's voice channel
#         channel=voice_channel.name
#         await client.say('User is in channel: '+ channel)
#         # create StreamPlayer
#         vc= await client.join_voice_channel(voice_channel)
#         player = vc.create_ffmpeg_player('COCKal.mp3', after=lambda: print('done'))
#         player.start()
#         while not player.is_done():
#             await asyncio.sleep(1)
#         # disconnect after the player has finished
#         player.stop()
#         await vc.disconnect()
#     else:
#         await client.say('User is not in a channel.')

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} priveDICK!')
    

# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


client.run(TOKEN)