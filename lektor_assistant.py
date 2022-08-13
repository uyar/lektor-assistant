# Copyright (C) 2022 H. Turgut Uyar <uyar@tekir.org>
#
# lektor-assistant is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# lektor-assistant is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with lektor-assistant.  If not, see <http://www.gnu.org/licenses/>.

"""A dashboard for Lektor."""

from pathlib import Path

import webview
from lektor.admin.modules.serve import render_template
from lektor.admin.webui import Flask


__version__ = "0.1.0"


server = Flask(__name__,
               static_folder=Path(__file__).with_name("assets"),
               template_folder=Path(__file__).with_name("templates"))


@server.route("/")
def landing():
    return render_template("landing.html")


def main():
    webview.create_window("Lektor Assistant", server)
    webview.start()


if __name__ == "__main__":
    main()
