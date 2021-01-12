from .. import loader, utils
import requests
from fake_useragent import UserAgent as ua
import requests


def register(cb):
    cb(lztMod())

class lztMod(loader.Module):
    """Lolzteam Api"""
    strings = {'name': 'Lolzteam Api'}

    async def lztprofilecmd(self, message):
        """ищет профиль лзт"""
        arg = utils.get_args_raw(message)
        x = requests.get("https://lolz.guru/api/index.php?users/find&username="+arg, headers={"User-Agent":ua().chrome}).json()['users']
        if x == []:
            await utils.answer(message, 'Пользователь не найден!')
            return
        x = x[0]
        text = "👤 Информация о пользователе <b>"+str(x['username'])+"</b>\n\n🆔 Айди: <b>"+str(x['user_id'])+"</b>\n💙 Количество симпатий: <b>"+str(x['user_like_count'])+"</b>\n💬 Количество сообщений: <b>"+str(x['user_message_count'])+"</b>\n"
        await utils.answer(message, text)