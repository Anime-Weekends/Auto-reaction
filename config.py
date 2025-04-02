from os import environ as env

class Config:
    API_ID = int(env.get("API_ID", "28744454")) #TG API ID
    API_HASH = env.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7") #TG API HASH
    BOT_TOKEN = env.get("BOT_TOKEN", "7560586869:AAFvUk-fK8cnSiWfMHHjOjE1ZWWf4f-IwjQ") #Add Bot Token, get from botfather
    FSUB_ID = int(env.get("FSUB_ID", "-1002410513772"))  #Add Your FSub Channel Id -100xxxxxxxxx
    FSUB = bool(env.get("FSUB", True)) #Keep True If U Want Force Subscribe         
    SB_PIC = env.get("SB_PIC", "https://i.ibb.co/prW38Db2/photo-2025-04-02-10-08-04-7488655537937055748.jpg") # Add Link For Start Cmd Picture 
    BOT_USERNAME = env.get("BOT_USERNAME", "Emiting_Auto_Reaction_Bot") # Add Bot Username Without @
    EMOJIS = [
        "👍", "✌🏻", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "☺", "😢",
        "🥶", "🤩", "🤮", "☠️",
        "🙏", "👌", "🤣", "🤡",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "😲", "🏆",
        "💔", "🤨", "😐", "😡",
        "👅", "🆒", "🖕", "😈",
        "😴", "😭", "👻", "⚡",
        "💕", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]
