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

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "24817837")
    API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8074880690:AAFQF0e2354OrOIe3e4qyDZWPnkMxo0PyXo") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","Digital_Rename_Bot")     
    DB_URL = os.environ.get("DB_URL","mongodb+srv://tgbot:4KzEdxEl4YldwwFR@tg.vr8ef.mongodb.net/?retryWrites=true&w=majority&appName=Tg")
 
    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/iw0.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7428552084').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002376378205"))

    # free upload limit 
    FREE_UPLOAD_LIMIT = 6442450944 # calculation 6*1024*1024*1024=results
    
    #vforce subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "BotZFlix")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "o_rename")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # part of text configuration
    START_TXT = """<b>Salut, {}👋

Je suis Yor Renamer Bot. un outil avancé et puissant. En utilisant ce bot, vous pouvez renommer et changer la miniature de votre fichier. Vous pouvez également convertir une vidéo en fichier et un fichier en vidéo. Ce bot prend également en charge les miniatures personnalisées et les légendes personnalisées

<blockquote> Crée par : @BotZFlix 🤪</blockquote> </b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 Mon Nom : {}
├🖥️ Développeur : <a href='t.me/Kingcey'>◡̈⃝ㅤ🇰ιηg¢єу</a>
├👨‍💻 Programmeur : <a href='t.me/Botzflix'>BotZFlix</a>
├📕 Lɪʙʀᴀʀie : {}
├✏️ Lᴀɴɢᴜᴀɢᴇ: {}
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: {}
├📊 ᴠᴇʀsɪᴏɴ: 3.5.1 </b>
╰───────────────⍟ """

    HELP_TXT = """
<b>•></b> /start Démarrer le bot.

✏️ <b><u>Comment renommer un fichier ?</u></b>
<b>•></b> Envoyez un fichier et tapez le nouveau nom du fichier, puis sélectionnez le format [document, vidéo, audio].           
ℹ️ Pour tout aide, contacte-nous :- <a href=https://t.me/Botzflix_Support>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

    UPGRADE= """
•⪼ ★𝘗𝘭𝘢𝘯𝘴     -    ⏳𝘋𝘢𝘵𝘦 -  💸prix - limite
•⪼ 🏆𝘗ro -    1mois -   1000f - 100gb
•⪼ 💎 Ultra Pro  -   1mois -   2000f - 1000gb

- <i> Pour nos plans sont en France CFA </i>
    """
    THUMBNAIL = """
🌌 <b><u>Comment Ajouter une vignette</u></b>

<b>•></b> Envoyer n'importe quel photo jpg, puis elle sera automatiquement ajoutée comme vignette.
<b>•></b> /del_thumb Utilise cette commande pour supprimer ton ancienne vignette.
<b>•></b> /view_thumb Utilise cette commande pour voir ta vignette.
"""
    CAPTION= """
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Utilise cette commande pour définir une légende
<b>•></b> /see_caption - Utilise cette commande pour voir ta légende
<b>•></b> /del_caption - utilise cette commande pour supprimer ta légende définie

Exᴀᴍᴩʟᴇ:- `/set_caption 📕 Nom Du fıchıer: {filename}
💾 Taille: {filesize}
⏰ Durée: {duration}`
"""
    BOT_STATUS = """
⚡️ Status du bot ⚡️

⌚️ Temps de fonction: `{}`
👭 Total utilisateurs: `{}`
💸 Utilisateurs premium: `{}`
֍ Total téléversé: `{}`
⊙ Total téléchargez: `{}`
"""
    LIVE_STATUS = """
⚡ ʟɪᴠᴇ sᴇʀᴠᴇʀ sᴛᴀᴛᴜs ⚡

ᴜᴘᴛɪᴍᴇ: `{}`
ᴄᴘᴜ: `{}%`
ʀᴀᴍ: `{}%` 
ᴛᴏᴛᴀʟ ᴅɪsᴋ: `{}`
ᴜsᴇᴅ sᴘᴀᴄᴇ: `{} {}%`
ғʀᴇᴇ sᴘᴀᴄᴇ: `{}`
ᴜᴘʟᴏᴀᴅ: `{}`
ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
V𝟹.𝟶.𝟶 [STABLE]
"""
    DIGITAL_METADATA = """
❪ Personnalisé la metadata ❫

- /metadata - pour définir ou changer le code de la méta-donnée

☞ Par exemple:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @BotZFlix" -metadata author="@Kingcey" -metadata:s:s title="Subtitled By :- @BotZFlix" -metadata:s:a title="By :- @kingcey" -metadata:s:v title="By:- @kingcey" </code>

📥 Pour tout aide. @BotZFlix
"""
    
    CUSTOM_FILE_NAME = """
<u>🖋️ Custom File Name</u>

you can pre-add a prefix and suffix along with your new filename

➢ /set_prefix - pour ajouter une préfixe.
➢ /see_prefix - Pour voir votre prefixe !!
➢ /del_prefix - Supprimé le prefixe !!
➢ /set_suffix - pour ajouter une suffixe.
➢ /see_suffix - Pour voir votre suffixe !!
➢ /del_suffix - Pour supprimer votre suffixe !!

Exᴀᴍᴩʟᴇ:- `/set_suffix @BotZFlix`
Exᴀᴍᴩʟᴇ:- `/set_prefix @BotZFlix`
"""
    
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @RknDeveloper🙏🥲
    # ᴡʜᴏᴇᴠᴇʀ ɪs ᴅᴇᴘʟᴏʏɪɴɢ ᴛʜɪs ʀᴇᴘᴏ ɪs ᴡᴀʀɴᴇᴅ ⚠️ ᴅᴏ ɴᴏᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛs ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʀᴇᴘᴏ #ғɪʀsᴛ ᴀɴᴅ ʟᴀsᴛ ᴡᴀʀɴɪɴɢ ⚠️
    DEV_TXT = """<b><u>Spécial merci pour mon développeur</b></u>
    
Y'a pas beaucoup à voir ici 

• ❣️ Bon à plus """
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Par exemple:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @BotZFlix" -metadata author="@Kingcey" -metadata:s:s title="Subtitled By :- @BotZFlix" -metadata:s:a title="By :- @Kingcey" -metadata:s:v title="By:- @Kingcey" </code>

📥 Pour tout aide. @BotZFlix
"""
    
    RKN_PROGRESS = """<b>\n
╭━━━━❰RKN PROCESSING...❱━➣
┣⪼ 🗃️ Poids: {1} | {2}
┣⪼ ⏳️ pourcentage: {0}%
┣⪼ 🚀 Vitesse: {3}/s
┣⪼ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
