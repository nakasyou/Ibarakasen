from utils.request_from_async import request_from_async

async def google(keyword: str):
    await request_from_async("https://www.google.com/search", {
        "q": keyword,
    })
