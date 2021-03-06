from asyncio import sleep
from .. import utils, loader
import re


def register(cb):
    cb(glbogaMod())

class glbogaMod(loader.Module):
    """поиск в глаз бога"""
    strings = {'name': 'glazboga'}

    async def tgcmd(self, message):
        """ищет в каких чатах есть чел"""
        arg = utils.get_args_raw(message)
        reply = (await message.get_reply_message())
        if reply:
            arg = reply.from_id
        x = (await message.client.send_message("eyegodsbot", "/tg "+str(arg)))
        if "<strong>Для продолжения работы необходимо подписаться на наш телеграм канал.</strong>" in x.text or "<strong>Добро пожаловать в Глаз Бога.</strong>" in x.text:
            return await utils.answer("сначала перейди в бота, стартани его и подпишись на их канал, потому что я не буду работать.")
        x = x.id
        await sleep(5)
        x = (await message.client.get_messages("eyegodsbot", ids=x+int(2))).text
        if "💬 <strong>Участник сообществ:</strong>" not in x:
            return await utils.answer(message, "<b>Чаты пользователя не найдены!</b>")
        if "ID" in x:
            x = x.replace(re.findall("📧  <strong>ID:</strong>.*", x)[0], '')
        if "Email" in x:
            x = x.replace(re.findall("📧 <strong>Email:</strong>\n.*", x)[0], '')
        if "Телефон" in x:
            x = x.replace(re.findall("📱.*", x)[0], '')
        x = x.replace(re.findall("👮‍♂️ <strong>Интересовались:</strong> <code>\d+ человек</code>", x)[0], '')
        return await utils.answer(message, x)
