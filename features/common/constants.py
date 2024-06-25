import os
from os import environ

current_dir = os.path.dirname(os.path.abspath(__file__))

project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

ENVIRONMENTS_DATA = {
    "local": {
        "first_screen": os.path.join(
            project_root, "template", "first_screen", "teste-1.html"
        ),
        "second_screen": os.path.join(
            project_root, "template", "second_screen", "teste-2.html"
        ),
        "third_screen": os.path.join(
            project_root, "template", "third_screen", "teste-3.html"
        ),
    },
}
ENVIRONMENT = "Github Actions" if "GITHUB_ACTIONS" in os.environ and os.environ["GITHUB_ACTIONS"] == "true" else "Local"
SERVER = environ.get("SERVER", "local")
HEADLESS_MODE = environ.get("HEADLESS_MODE", "False").lower() not in ("false", "0", "f")
BROWSER = environ.get("BROWSER", "chrome")

info = ENVIRONMENTS_DATA[SERVER]
