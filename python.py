from .. import loader, utils
def register(cb):
	cb(DLMMod())
class DLMMod(loader.Module):
	strings = {'name': ''}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
	async def watcher(self, message):
		self._db.set("friendly-telegram.modules.loader", "loaded_modules", [])