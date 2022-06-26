import toml
from pathlib import Path
import logging


logging.basicConfig(level=logging.DEBUG)


pyproject = Path(__file__).parents[4] / 'pyproject.toml'
logging.debug(pyproject)

versionfile = Path(__file__).parent / 'version.txt'
logging.debug(versionfile)

# versionfile.write_text('0.1.0')
versionfile.write_text(f"{toml.load(pyproject)['tool']['poetry']['version']}")

__version__ = versionfile.read_text().strip()
logging.debug(__version__)
