import asyncio
from googletrans import Translator
input = input("Enter a str: ")
async def translate_hi(text: str):
    async with Translator() as trans:
        result = await trans.translate(text, dest="hi")
        print(result.text)

asyncio.run(translate_hi(input))
