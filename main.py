import asyncio
import json
import os
from typing import List

import aiofiles
import aiohttp


async def download_image(image_url: str, session: aiohttp.ClientSession, path: str) -> str:
    file_name = os.path.join(path, image_url.split("/")[-1])
    async with session.get(image_url) as response:
        img_file = await aiofiles.open(file_name, mode="wb")
        await img_file.write(await response.read())
        await img_file.close()
        return file_name


async def read_file(file_name: str) -> List[str]:
    async with aiofiles.open(file_name) as urls:
        return json.loads(await urls.read()).get("urls")


async def main(path: str):
    urls = await read_file("images.json")
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(asyncio.ensure_future(download_image(url, session, path)))
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    output = "output"
    if not os.path.exists(output):
        os.mkdir(output)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(output))
