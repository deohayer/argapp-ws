from .core import *


def test_returns_1_0000():
    assert AppHelper().section_epilog('Title', App()) == ''


def test_returns_2_0000():
    # Title.
    title = 'Title'
    app = App(epilog='This is epilog.')
    assert AppHelper().section_epilog(title, app) == str(
        'Title:\n'
        'This is epilog.'
    )


def test_returns_2_0001():
    # No title.
    title = ''
    app = App(epilog='This is epilog.')
    assert AppHelper().section_epilog(title, app) == str(
        'This is epilog.'
    )
