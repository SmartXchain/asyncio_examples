import asyncio

async def say_hello():
    print("Hello!")
    # Simulates as asynchronous operation
    await asyncio.sleep(5)
    print ("Hello again!")

# Running the event loop
asyncio.run(say_hello())