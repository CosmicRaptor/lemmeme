import feedparser
import aiohttp

async def getMemes(meme_url: list):
    meme_list = []
    async with aiohttp.ClientSession() as session:
        for item in meme_url:
            async with session.get(item) as response:
                if response.status == 200:
                    html = await response.text()
                    feed = feedparser.parse(html)
                    for item2 in feed.entries:
                        meme_list.append(item2)


    return meme_list
