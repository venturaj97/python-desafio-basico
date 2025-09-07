import asyncio

#coroutine
async def say_hello(nome):
    print(f"{nome} vai dizer...")
    await asyncio.sleep(3) #Simulando IO
    print(f"{nome} disse olá")

async def main():
    await say_hello("Isis") #vai rodar sozinha primeiro

    await asyncio.gather(
        say_hello("João"),
        say_hello("Victor")
    )
    
asyncio.run(main())