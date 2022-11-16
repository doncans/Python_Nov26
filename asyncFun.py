import asyncio
def fun(data):
    #
    #
    return "something"

async def async_fun(args):
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, fun, args)
    return res

async def async_fun1(*urls):
    tasks = []
    for url in urls:
        task = async_fun(url)
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res

