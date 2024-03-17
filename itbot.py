import discord
import random

# Discordクライアントを作成
client = discord.Client(intents=discord.Intents.all())


# 質問リスト
question_list = [
    "どこに住んできますか？",
    "なにの食べ物が好きですか",
    "どこで病みサー知ったんですか？",
    "趣味は何ですか？",
    "おすすめの本はありますか？",
    "結婚していますか？",
    "結婚しますか？",
    "イケメン興味ありますぅぅぅぅぅぅ？",
    "付き合いの長いネットの人いますか？",
    "僕のこと好きですか？",
    "チョコください",
    "僕はりゅうさんのことが好きなのですが誰か好きな人います？　あっ、僕でもいいんですよ？",
    "毎朝味噌汁作ったりしますか？",
    "注意行ってるんですけど一緒にお茶しません？",
    "質問しても大丈夫ですか？",
    "傲慢ですが大丈夫ですか？",

]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # メッセージがBOT自身の場合は無視する
    if message.author == client.user:
        return
    
    # メッセージが質問リストに含まれている場合はランダムで質問する
    if message.content.lower() == "itさん":
        question = random.choice(question_list)
        await message.channel.send(question)
    
    #なんかしらんけど蚊取り線香の話ししてたらしいよ
    if "おもしろいこといって" in message.content:
        response = "蚊取り線香の話します？"
        await message.channel.send(response)
    
    #もっと面白い話してくださいね
    if "刺激がない" in message.content:
        response = "しょうがないですよぉ"
        await message.channel.send(response)

# Discordボットを起動する
client.run('YOUR_DISCORD_BOT_TOKEN')