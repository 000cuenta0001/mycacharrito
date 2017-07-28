# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# MiTvSpain
# Copyright 2017

#
# Distributed under the terms of GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------------------
# This file is part of MiTvSpain.
#
# MiTvSpain is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MiTvSpain is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MiTvSpain.  If not, see <http://www.gnu.org/licenses/>.
# ------------------------------------------------------------
import traceback
import BaseHTTPServer
from SocketServer import ThreadingMixIn
from threading import Thread


class Server(ThreadingMixIn, BaseHTTPServer.HTTPServer):
    daemon_threads = True
    timeout = 1
    def __init__(self, address, handler, client):
        BaseHTTPServer.HTTPServer.__init__(self,address,handler)
        self._client = client
        self.file=None
        self.running=True
        self.request = None

    def stop(self):
        self.running=False

    def serve(self):
        while self.running:
            try:
                self.handle_request()
            except:
                print traceback.format_exc()

    def run(self):
        t=Thread(target=self.serve, name='HTTP Server')
        t.daemon=True
        t.start()
    def handle_error(self, request, client_address):
      if not "socket.py" in traceback.format_exc():
        print traceback.format_exc()