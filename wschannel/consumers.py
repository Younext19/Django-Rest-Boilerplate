from django.contrib.auth.models import User
from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer

from connect.serializers import GetUserInfoSerializer


class UserConsumer(AsyncAPIConsumer):

    async def connect(self):
        await self.model_change.subscribe()
        return await super().connect()
