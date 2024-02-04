from .core import *


def test_returns_1_0000():
    assert AppHelper().section_prolog('Title', App()) == ''


def test_returns_2_0000():
    # Title.
    title = 'Title'
    app = App(prolog='This is prolog.')
    assert AppHelper().section_prolog(title, app) == str(
        'Title:\n'
        'This is prolog.'
    )


def test_returns_2_0001():
    # No title.
    title = ''
    app = App(prolog='This is prolog.')
    assert AppHelper().section_prolog(title, app) == str(
        'This is prolog.'
    )
