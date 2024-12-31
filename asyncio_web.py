import aiohttp
import asyncio

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://smartxchain.com", "https://example.com"]
    results = await asyncio.gather(*[fetch_page(url) for url in urls])
    print(results)

asyncio.run(main())