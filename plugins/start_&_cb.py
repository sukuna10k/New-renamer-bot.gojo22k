# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support
"""
Apache License 2.0
Copyright (c) 2022 @Digital_Botz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/Digital_Botz 
Repo Link : https://github.com/DigitalBotz/Digital-Rename-Bot
License Link : https://github.com/DigitalBotz/Digital-Rename-Bot/blob/main/LICENSE
"""

# extra imports
import random, asyncio, datetime, pytz, time, psutil, shutil

# pyrogram imports
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery

# bots imports
from helper.database import digital_botz
from config import Config, rkn
from helper.utils import humanbytes
from plugins import __version__ as _bot_version_, __developer__, __database__, __library__, __language__, __programer__

upgrade_button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('Acheter premium ✓', user_id=int(6705898491)),
         ],[
        InlineKeyboardButton("Retour", callback_data = "start")
]])

upgrade_trial_button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('Acheter premium ✓', user_id=int(6705898491)),
         ],[
        InlineKeyboardButton("Gratuit - 𝟷𝟸 heures ✓", callback_data = "give_trial"),
        InlineKeyboardButton("Retour", callback_data = "start")
]])

start_button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('Mis à jour🤪', url='https://t.me/Botzflix'),
        InlineKeyboardButton('Support🤗', url='https://t.me/BotzflixSupport')
        ],[
        InlineKeyboardButton('À propos', callback_data='about'),
        InlineKeyboardButton('Aide', callback_data='help')
        ],[
        InlineKeyboardButton('🔮 Mis à jour Premium 🏆', callback_data='upgrade')
         ]])
        
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await digital_botz.add_user(client, message) 
    if Config.RKN_PIC:
        await message.reply_photo(Config.RKN_PIC, caption=rkn.START_TXT.format(user.mention), reply_markup=start_button)       
    else:
        await message.reply_text(text=rkn.START_TXT.format(user.mention), reply_markup=start_button, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command("myplan"))
async def myplan(client, message):
    user_id  = message.from_user.id
    user = message.from_user.mention        
    await digital_botz.reset_uploadlimit_access(user_id)        
    if await digital_botz.has_premium_access(user_id):
        user_data = await digital_botz.get_user_data(user_id)
        limit = user_data.get('uploadlimit', 0)
        used = user_data.get('used_limit', 0)
        remain = int(limit)- int(used)
        type = user_data.get('usertype', "Free")
            
        data = await digital_botz.get_user(user_id)
        expiry_str_in_ist = data.get("expiry_time")
        time_left_str = expiry_str_in_ist - datetime.datetime.now()
       # time_left_str = await digital_botz.checking_remaining_time(user_id)
        #expiry_str_in_ist = time_left_str + datetime.datetime.now()
        
        await message.reply_text(f"👤 Toi :- {user}\n⚡ Ton ID :- <code>{user_id}</code>\nPlan :- `{type}`\nLimite quotidienne :- `{humanbytes(limit)}`\nUtilisé aujourd'hui :- `{humanbytes(used)}\n`Remain:- `{humanbytes(remain)}`\n⏰ Dernière Heures : {time_left_str}\n⌛️ Date d'expiration : {expiry_str_in_ist}", quote=True)
    else:
        user_data = await digital_botz.get_user_data(user_id)
        limit = user_data.get('uploadlimit', 0)
        used = user_data.get('used_limit', 0)
        remain = int(limit)- int(used)
        type = user_data.get('usertype', "Free")
        await message.reply_text(f"👤 Toi :- {user}\n⚡ Ton ID :- <code>{user_id}</code>\nPlan :- `{type}`\nLimite journalière :- `{humanbytes(limit)}`\nUtilisé aujourd'hui :- `{humanbytes(used)}\n`Remain :- `{humanbytes(remain)}`\n⏰ Date d'expiration:- Temps de vie\n\nSi tu veux un plan Premium, clique sur le. Bouton 👇",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("♨️ Obtenir le plan premium ♨️", callback_data='upgrade')]]), quote=True)			 
 

@Client.on_message(filters.private & filters.command("plans"))
async def plans(client, message):
    user = message.from_user
    free_trial_status = await digital_botz.get_free_trial_status(user.id)
    if not await digital_botz.has_premium_access(user.id):
        if not free_trial_status:
            await message.reply_text(text=rkn.UPGRADE.format(user.mention), reply_markup=upgrade_trial_button, disable_web_page_preview=True)
        else:
            await message.reply_text(text=rkn.UPGRADE.format(user.mention), reply_markup=upgrade_button, disable_web_page_preview=True)
    else:
        await message.reply_text(text=rkn.UPGRADE.format(user.mention), reply_markup=upgrade_button, disable_web_page_preview=True)
   
  
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=rkn.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = start_button)
        
    elif data == "help":
        await query.message.edit_text(
            text=rkn.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("Vignette", callback_data = "thumbnail"),
                InlineKeyboardButton("Légende", callback_data = "caption")
                ],[          
                InlineKeyboardButton("Personnalisé le nom de fichier", callback_data = "custom_file_name")    
                ],[          
                InlineKeyboardButton("À propos", callback_data = "about"),
                InlineKeyboardButton("Meta-Donnéé", callback_data = "digital_meta_data")
                                     ],[
                InlineKeyboardButton("Retour", callback_data = "start")
                  ]]))         
        
    elif data == "about":
        await query.message.edit_text(
            text=rkn.ABOUT_TXT.format(client.mention, __developer__, __programer__, __library__, __language__, __database__, _bot_version_),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("Contact", callback_data = "source_code"), #Whoever is deploying this repo is given a warning ⚠️ not to remove this repo link #first & last warning ⚠️
                InlineKeyboardButton("Status DU bot", callback_data = "bot_status")
                ],[
                InlineKeyboardButton("Status de vie", callback_data = "live_status"),
                InlineKeyboardButton("♨️ Premium ♨️", callback_data = "upgrade")
                ],[   
                InlineKeyboardButton("Retour", callback_data = "start")
            
           ]]))    
        
    elif data == "upgrade":
        free_trial_status = await digital_botz.get_free_trial_status(query.from_user.id)
        if not await digital_botz.has_premium_access(query.from_user.id):
            if not free_trial_status:
                await query.message.edit_text(text=rkn.UPGRADE, disable_web_page_preview=True, reply_markup=upgrade_trial_button)   
            else:
                await query.message.edit_text(text=rkn.UPGRADE, disable_web_page_preview=True, reply_markup=upgrade_button)
        else:
            await query.message.edit_text(text=rkn.UPGRADE, disable_web_page_preview=True, reply_markup=upgrade_button)
           
    elif data == "give_trial":
        await query.message.delete()
        free_trial_status = await digital_botz.get_free_trial_status(query.from_user.id)
        if not free_trial_status:            
            await digital_botz.give_free_trail(query.from_user.id)
            new_text = "**Ton plan de Premium a été ajouté pour 12 heures de temps.\n\nEssaie la fonctionnalité premium voir. C'est trop géniale 🤪**"
        else:
            new_text = "**🤣T'avais déjà ressue le plan gratuit mon gars😑. Clique sur 👉 /plans pour voir ton plan**"
        await client.send_message(query.from_user.id, text=new_text)

    elif data == "thumbnail":
        await query.message.edit_text(
            text=rkn.THUMBNAIL,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour", callback_data = "help")]])) 
      
    elif data == "caption":
        await query.message.edit_text(
            text=rkn.CAPTION,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Bᴀᴄᴋ", callback_data = "help")]])) 
      
    elif data == "custom_file_name":
        await query.message.edit_text(
            text=rkn.CUSTOM_FILE_NAME,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour", callback_data = "help")]])) 
      
    elif data == "digital_meta_data":
        await query.message.edit_text(
            text=rkn.DIGITAL_METADATA,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour", callback_data = "help")]])) 
      
    elif data == "bot_status":
        total_users = await digital_botz.total_users_count()
        total_premium_users = await digital_botz.total_premium_users_count()
        uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
        sent = humanbytes(psutil.net_io_counters().bytes_sent)
        recv = humanbytes(psutil.net_io_counters().bytes_recv)
        await query.message.edit_text(
            text=rkn.BOT_STATUS.format(uptime, total_users, total_premium_users, sent, recv),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour", callback_data = "about")]])) 
      
    elif data == "live_status":
        currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
        total, used, free = shutil.disk_usage(".")
        total = humanbytes(total)
        used = humanbytes(used)
        free = humanbytes(free)
        sent = humanbytes(psutil.net_io_counters().bytes_sent)
        recv = humanbytes(psutil.net_io_counters().bytes_recv)
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        await query.message.edit_text(
            text=rkn.LIVE_STATUS.format(currentTime, cpu_usage, ram_usage, total, used, disk_usage, free, sent, recv),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton(" Retour", callback_data = "about")]])) 
      
    elif data == "source_code":
        await query.message.edit_text(
            text=rkn.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
           #Whoever is deploying this repo is given a warning ⚠️ not to remove this repo link #first & last warning ⚠️   
                InlineKeyboardButton("💞 T'aime les films et séries ? 💞", url="https://t.me/ZFlixTeam")
            ],[
                InlineKeyboardButton("🔒 Fermer", callback_data = "close"),
                InlineKeyboardButton("◀️ Retour", callback_data = "start")
                 ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
