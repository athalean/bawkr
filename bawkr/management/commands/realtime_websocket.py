import gevent
from gevent import monkey
import json
from bawkr.celery import save_bawk

monkey.patch_all()

import random
from django.core.management.base import BaseCommand
from geventwebsocket import WebSocketServer, WebSocketApplication, WebSocketError, Resource


def save_message(user, message):
    save_bawk.apply_async((user, message))


def send_ping(app):
    while True:
        try:
            app.ws.send('PING')
            gevent.sleep(10)
        except WebSocketError:
            app.on_close()
            return


class BawkrApplication(WebSocketApplication):
    greeter = None

    def on_open(self):
        print "Connection opened"
        gevent.spawn(send_ping, self)

    def on_message(self, message):
        if message is None:
            return

        if not message.startswith('MSG\n'):
            return

        header, user, message = message.split('\n')
        gevent.spawn(save_message, user, message)

        for client in self.ws.handler.server.clients.values():
            client.ws.send(json.dumps({
                'name': user,
                'message': message
            }))

    def on_close(self, reason=''):
        if self.greeter:
            self.greeter.kill()
        print "Connection closed"


class Command(BaseCommand):
    help = 'Runs realtime server'

    def handle(self, *args, **options):
        print "Server up!"
        WebSocketServer(
            ('127.0.0.1', 8888),

            Resource({'^/.*': BawkrApplication}),
            debug=False
        ).serve_forever()
        print "Server down!"