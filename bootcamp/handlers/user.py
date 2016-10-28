from __future__ import absolute_import

from bootcamp.services.user_service import UserService

from tornado.gen import coroutine

from .base import BaseHandler


class UserHandler(BaseHandler):
    @coroutine
    def get(self):
        service = UserService()
        users = yield service.get_all()
        self.write('Number of users: {}'.format(len(users)))