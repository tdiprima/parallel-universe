# 🚀 Best of both worlds! Async event loop meets thread pool power.
# When asyncio needs to talk to the synchronous world (like requests),
# threads become the helpful translators! 🌐

import asyncio
from concurrent.futures import ThreadPoolExecutor

import requests


def fetch(url):
    return requests.get(url).text[:100]


async def main():
    urls = ["https://example.com"] * 5
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        tasks = [loop.run_in_executor(pool, fetch, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)


if __name__ == "__main__":
    asyncio.run(main())
