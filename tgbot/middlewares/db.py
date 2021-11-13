from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware


class DbMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, session):
        super().__init__()
        self.session = session

    async def pre_process(self, obj, data, *args):
        try:
            self.session.connection()
            data["session"] = self.session

        except Exception as e:
            print(e)
            self.session.rollback()
            await self.pre_process(obj, data, *args)

    async def post_process(self, obj, data, *args):
        session = data.get("session")
        if session:
            session.close()
