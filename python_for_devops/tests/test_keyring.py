import pytest
import random


@pytest.fixture
def mon_keyring():
    def make_keyring(default=False):
        if default:
            key = "AQBvaBFZAAAAABAA9VHgwCg3rWn8fMaX8KL01A=="
        else:
            key = "%032x==" % random.getrandbits(128)
        return """
    [mon.]
        key = %s
            caps mon = "allow *"
        """ % key
    return make_keyring


@pytest.fixture
def keyring_file(mon_keyring, tmpdir):
    def generate_file(default=False):
        keyring = tmpdir.join('keyring')
        keyring.write_text(mon_keyring(default=default))
        return keyring.strpath
    return generate_file


def test_default_key(mon_keyring):
    contents = mon_keyring(default=True)
    assert "AQBvaBFZAAAAABAA9VHgwCg3rWn8fMaX8KL01A==" in contents


def test_keyring_file_contents(keyring_file):
    keyring_path = keyring_file(default=True)
    with open(keyring_path) as fp:
        contents = fp.read()
    assert "AQBvaBFZAAAAABAA9VHgwCg3rWn8fMaX8KL01A==" in contents
