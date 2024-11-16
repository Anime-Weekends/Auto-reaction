from os import environ as env

class Config:
    API_ID = int(env.get("API_ID", "14680661")) #TG API ID
    API_HASH = env.get("API_HASH", "166f6e394021081c5cdb41c92344deb7") #TG API HASH
    BOT_TOKEN = env.get("BOT_TOKEN", "7211101354:AAGoPWssXZSvU5O5iWbjXJpI2R9EprAGr8s") #Add Bot Token, get from botfather
    FSUB_ID = int(env.get("FSUB_ID", "-1002104350566"))  #Add Your FSub Channel Id
    FSUB = bool(env.get("FSUB", True)) #Keep True If U Want Force Subscribe 
    PORT = env.get('PORT', '8080')          
    SB_PIC = env.get("SB_PIC", "https://i.ibb.co/c6vkVBP/photo-2024-11-15-12-13-41-7437478159336865812.jpg") #Add Link For Start Cmd Pic
    BOT_USERNAME = env.get("BOT_USERNAME", "Sb_reactionbot") #Add Bot Username Without @
    EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢",
        "🥶", "🤩", "🤮", "💩",
        "🙏", "👌", "🤣", "🤡",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "🍌", "🏆",
        "💔", "🤨", "😐", "😡",
        "👅", "🆒", "🖕", "😈",
        "😴", "😭", "👻", "⚡",
        "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]
