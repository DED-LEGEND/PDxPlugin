import asyncio
from random import choice
from pyrogram.types import Message
from pyrogram import filters, Client
from Pbxbot.bad.sukh import RAID, PBRAID
from . import *

@on_message("raid", allow_stan=True)
async def raid(x: Client, e: Message):
      PbxTeam = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(PbxTeam) == 2:
          ok = await x.get_users(kex[1])
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(RAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(RAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("Rᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  

#pbiraid

@on_message("pbiraid", allow_stan=True)
async def raid(x: Client, e: Message):
      PbxTeam = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

      if len(PbxTeam) == 2:
          ok = await x.get_users(kex[1])
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(PBRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await x.get_users(user_id)
          counts = int(PbxTeam[0])
          for _ in range(counts):
                reply = choice(PBRAID)
                msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                await x.send_message(e.chat.id, msg)
                await asyncio.sleep(0.1)

      else:
            await e.reply_text("ᴘʙɪʀᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")  
