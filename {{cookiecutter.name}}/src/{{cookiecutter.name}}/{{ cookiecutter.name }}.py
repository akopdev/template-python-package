import aiohttp

async def my_func(name) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://example.com/api.json", params={"name": name}) as response:
            data = await response.json()
            return data["message"]
