import asyncio

#coroutine
async def say_hello(nome):
    print(f"{nome} vai dizer...")
    await asyncio.sleep(3) #Simulando IO
    print(f"{nome} disse olá")

async def main():
    await say_hello("João")
    await say_hello("Victor")
    
asyncio.run(main())