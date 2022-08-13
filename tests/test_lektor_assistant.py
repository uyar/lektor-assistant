import sys
from pathlib import Path

from pkg_resources import get_distribution

import lektor_assistant


def test_installed_version_should_match_tested_version():
    assert get_distribution("lektor_assistant").version == lektor_assistant.__version__


def test_installation_should_create_executable():
    assert Path(sys.executable).with_name("lektor-assistant").exists()
