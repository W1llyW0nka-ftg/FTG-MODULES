from .. import loader, utils


def register(cb):
    cb(tiktoknwMod())

class tiktoknwMod(loader.Module):
    """Скачивает видео с тиктока без вотермарки."""
    strings = {'name': 'TikTok no WaterMark'}

    async def ttcmd(self, message):
        """ну отправляет видос получаеца."""
        await utils.answer(message, 'Минуточку...')
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "где ссылка дебил")
            return
        r = await message.client.inline_query('tikdobot', args)
        await message.client.send_file(message.to_id, r[1].result.content.url)
        await message.delete()