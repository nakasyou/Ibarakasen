from utils.request_from_async import request_from_async

async def bing(keyword: str):
    await request_from_async("https://www.bing.com/search", {
        "q": keyword,
    })
