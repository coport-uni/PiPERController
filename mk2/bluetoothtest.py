import asyncio
from bleak import BleakScanner

# FE:BE:2D:A2:35:1F (rssi=-49): Picus-46980628

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())