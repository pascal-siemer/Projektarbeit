from Tools.Debouncer import Debouncer



async def doStuff():
    await asyncio.wait(500)



debouncer = Debouncer(2000)




