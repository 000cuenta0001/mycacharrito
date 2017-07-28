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

import os
import sys

# Appends the main plugin dir to the PYTHONPATH if an internal package cannot be imported.
# Examples: In Plex Media Server all modules are under "Code.*" package, and in Enigma2 under "Plugins.Extensions.*"
try:
    #from core import logger
    import core
except:
    sys.path.append( os.path.abspath( os.path.join( os.path.dirname(__file__) , ".." ) ) )
