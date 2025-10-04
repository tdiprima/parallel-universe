# 🌊 Async wizardry! Watch tasks flow like water, never blocking the stream.
# Uses asyncio.gather() to fetch data concurrently - all tasks start together,
# finish when they're ready, like a well-choreographed dance! 💃

import asyncio


async def fetch_data(n):
    print(f"Fetching {n}...")
    await asyncio.sleep(2)  # non-blocking sleep
    print(f"Done {n}")
    return n * 10


async def main():
    tasks = [fetch_data(i) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print("Results:", results)


if __name__ == "__main__":
    asyncio.run(main())
