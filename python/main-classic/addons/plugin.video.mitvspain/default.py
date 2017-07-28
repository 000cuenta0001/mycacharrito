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
# XBMC entry point
# ------------------------------------------------------------


import os
import sys

import xbmc
from core import config
from core import logger

logger.info("init...")

librerias = xbmc.translatePath(os.path.join(config.get_runtime_path(), 'lib'))
sys.path.append(librerias)

from platformcode import launcher

if sys.argv[2] == "":
    launcher.start()
    launcher.run()
else:
    launcher.run()
