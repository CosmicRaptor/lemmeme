import feedparser
import aiohttp


async def storeMemes(sort_algorithm: str):
    meme_url = ['https://lemmy.ml/feeds/c/memes.xml?sort=',
                'https://sopuli.xyz/feeds/c/memes.xml?sort=',
                'https://lemmy.world/feeds/c/lemmyshitpost.xml?sort=',
                'https://lemmy.blahaj.zone/feeds/c/196.xml?sort=']
    memes = []
    async with aiohttp.ClientSession() as session:
        for item in meme_url:
            async with session.get(item + sort_algorithm) as response:
                if response.status == 200:
                    html = await response.text()
                    feed = feedparser.parse(html)
                    for item1 in feed.entries:
                        memes.append(item1)

    return memes


async def getMemes():
    meme_dict = {}
    meme_dict["Hot"] = await storeMemes("Hot")
    meme_dict["Active"] = await storeMemes("Active")
    meme_dict["TopDay"] = await storeMemes("TopDay")
    meme_dict["New"] = await storeMemes("New")
    meme_dict["MostComments"] = await storeMemes("MostComments")
    return meme_dict
