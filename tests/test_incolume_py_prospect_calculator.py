from incolume.py.prospect.calculator import __version__, pyproject


def test_assert_config():
    assert pyproject.is_file(), f"{pyproject}"
    assert pyproject.name == 'pyproject.toml'


def test_version():
    __version__ == '0.1.0'
