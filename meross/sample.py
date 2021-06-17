import asyncio
import os
from meross_iot.api import MerossHttpClient
from meross_iot.manager import MerossManager

EMAIL = os.environ.get('MEROSS_EMAIL') or "gch@meross.com"
PASSWORD = os.environ.get('MEROSS_PASSWORD') or "123456" 


async def main():
    # Setup the HTTP client API from user-password
    http_api_client = await MerossHttpClient.from_user_password(email="gch@meross.com", password="123456")
    print("done1")
    # Setup and start the device manager
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()
    print("done2")
    # Retrieve all the MSS310 devices that are registered on this account
    await manager.async_device_discovery()
    plugs = manager.find_devices(device_type="mss310")
    print("done3")
    if len(plugs) < 1:
        print("No MSS310 plugs found...")
    else:
        # Turn it on channel 0
        # Note that channel argument is optional for MSS310 as they only have one channel
        dev = plugs[0]
        
        # The first time we play with a device, we must update its status
        await dev.async_update()
        
        # We can now start playing with that
        print(f"Turning on {dev.name}...")
        await dev.async_turn_on(channel=0)
        print("Waiting a bit before turing it off")
        await asyncio.sleep(5)
        print(f"Turing off {dev.name}")
        await dev.async_turn_off(channel=0)

    # Close the manager and logout from http_api
    manager.close()
    await http_api_client.async_logout()

if __name__ == '__main__':
    # On Windows + Python 3.8, you should uncomment the following
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
