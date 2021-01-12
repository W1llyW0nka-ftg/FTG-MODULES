from .. import loader, utils
import json
import requests


def register(cb):
    cb(catMod())

class catMod(loader.Module):
    """ищет котика"""
    strings = {'name': 'Cats'}

    async def catcmd(self, message):
        """отправляет котика"""
        await message.client.send_file(message.to_id, json.loads(requests.get("http://aws.random.cat/meow").text)['file'])
        await message.delete()