from engines import bing, google
import asyncio

class Suggest:
    def __init__(self, keywords):
        self.keywords = keywords
        pass
    async def pollution(self):
        async_requests = []
        for keyword in self.keywords:
            async_requests.extend([
                bing(keyword),
                google(keyword),
            ])
        
        await asyncio.gather(*async_requests)