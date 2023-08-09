import asyncio
import time

async def print_after(message, delay):
   """ Print a message after the specified delay (in seconds)"""
   await asyncio.sleep(delay)
   print(f"{time.ctime()} - {message}")

async def main():
   # Start coroutine twice (hopefully they start!)
   second_awaitable = asyncio.create_task(print_after("Hello", 1))
   first_awaitable = asyncio.create_task(print_after("world!", 2))
   # Wait for coroutines to finish
   await second_awaitable
   await first_awaitable

asyncio.run(main())


#
# Wed Aug  9 13:31:03 2023 - Hello
# Wed Aug  9 13:31:04 2023 - world!