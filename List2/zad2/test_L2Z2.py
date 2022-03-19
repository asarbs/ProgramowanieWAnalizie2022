from l2z2 import *
import hashlib


def test_counter():
    assert letter_counter() == 3345


def test_split():
    assert len(word_split()) == 495


def test_word_counter():
    assert word_counter() == 495


def test_cast_to_set():
    assert len(cast_to_set()) == 238


def test_word_occurrence():
    o = word_occurrence()
    res = {'felis.': 1, 'odio.': 1, '\nLorem': 1, 'tempus.': 1, 'varius,': 1, 'non': 3, 'risus': 4, 'Sed': 4, 'in': 7, 'aliquam,': 1, 'Nulla': 1, 'ac': 3, 'vulputate.\n\nCras': 1, 'nunc.': 1, 'feugiat': 1, 'primis': 1, 'diam': 1, 'viverra': 1, 'leo': 2, 'dignissim.': 1, 'placerat,': 1, 'quam': 1, 'Ut': 3, 'massa.': 2, 'id': 7, 'metus,': 1, 'luctus.': 1, 'mauris,': 1, 'commodo.': 1, 'et,': 2, 'Aliquam': 1, 'porttitor,': 1, 'justo,': 1, 'lectus': 2, 'ut': 5, 'ligula': 4, 'convallis': 3, 'quis': 6, 'Fusce': 2, 'mattis': 1, 'vulputate': 1, 'dignissim': 3, 'eleifend': 2, 'In': 1, 'odio': 4, 'ornare': 1, 'eget.\n\nIn': 1, 'cubilia': 1, 'platea': 1, 'egestas': 1, 'vestibulum': 2, 'Etiam': 3, 'lectus.': 2, 'enim': 5, 'dui': 4, 'ut.': 1, 'molestie': 2, 'Phasellus': 2, 'eros': 1, 'dolor.': 1, 'dictum,': 1, 'nisl,': 1, 'mollis': 2, 'eu.': 1, 'vestibulum.': 1, 'ex,': 2, 'vel,': 1, 'habitasse': 1, 'blandit': 1, 'turpis': 2, 'Aenean': 1, 'magna.': 1, 'ligula,': 1, 'ipsum': 7, 'sapien,': 1, 'metus.\n\nMorbi': 1, 'nisl': 2, 'tellus.': 2, 'volutpat': 1, 'bibendum.': 1, 'dui.': 1, 'neque': 1, 'dictumst.': 1, 'amet,': 3, 'amet': 4, 'nunc': 1, 'Curabitur': 3, 'efficitur': 1, 'erat': 4, 'sem,': 1, 'convallis.': 1, 'Proin': 1, 'laoreet': 1, 'varius': 2, 'eu,': 1, 'eros,': 1, 'maximus': 1, 'tortor.': 2, 'Quisque': 1, 'placerat': 2, 'ante,': 1, 'auctor.': 1, 'tortor': 2, 'sagittis': 1, 'ultrices': 4, 'pretium': 3, 'finibus': 2, 'curae;': 1, 'suscipit': 2, 'condimentum': 2, 'enim,': 1, 'mollis.\n\nQuisque': 1, 'purus': 1, 'Duis': 2, 'Donec': 5, 'aliquet.': 1, 'vehicula': 1, 'congue': 1, 'ultricies': 1, 'iaculis': 3, 'aliquam': 2, 'libero.': 1, 'adipiscing': 3, 'lorem': 1, 'elementum.': 1, 'est': 3, 'vel.': 1, 'dapibus.': 1, 'aliquet': 1, 'mauris.': 1, 'lobortis': 3, 'urna': 2, 'Vestibulum': 1, 'hendrerit': 2, 'consequat': 3, 'lacinia': 3, 'Maecenas': 4, 'Nam': 2, 'Pellentesque': 1, 'vulputate,': 1, 'augue': 4, 'fringilla': 2, 'orci': 2, 'sed': 7, 'metus.': 3, 'sagittis,': 1, 'Morbi': 2, 'arcu.': 1, 'Cras': 1, 'neque.': 1, 'tincidunt': 7, 'massa': 1, 'metus': 1, 'diam,': 1, 'dolor': 4, 'dictum': 1, 'ipsum.': 1, 'eget': 6, 'blandit.': 1, 'Vivamus': 6, 'volutpat,': 1, 'commodo': 1, 'ultrices.': 1, 'Suspendisse': 3, 'vitae': 4, 'gravida': 2, 'sit': 7, 'malesuada': 1, 'consequat.': 1, 'arcu': 2, 'mauris': 3, 'justo': 3, 'tempus': 4, 'lacinia,': 1, 'luctus': 3, 'tellus': 1, 'porta.': 2, 'posuere': 1, 'enim.': 1, 'euismod': 1, 'consectetur.': 1, 'Lorem': 2, 'mi': 1, 'nec': 5, 'porttitor': 6, 'id,': 1, 'felis': 2, 'velit': 1, 'consectetur': 7, 'magna': 4, 'nisi,': 1, 'euismod.': 1, 'mi.': 1, 'vel': 11, 'et': 8, 'elit.': 3, 'nibh': 2, 'tempor': 2, 'at': 9, 'ante': 4, 'elementum,': 1, 'Integer': 2, 'quam,': 1, 'diam.': 1, 'nisl.': 1, 'elementum': 3, 'semper': 3, 'pulvinar': 2, 'cursus': 2, 'euismod,': 1, 'venenatis': 3, 'ante.': 1, 'Nunc': 3, 'auctor': 2, 'sem': 2, 'lacus': 3, 'accumsan': 3, 'bibendum,': 1, 'tincidunt.': 1, 'elit': 3, 'rutrum': 1, 'orci,': 1, 'aliquam.': 1, 'Sed.\n': 1, 'pellentesque': 1, 'interdum': 2, 'interdum.\n\nMaecenas': 1, 'eu': 6, 'scelerisque.': 1, 'non,': 1, 'bibendum': 1, 'faucibus': 2, 'nulla': 5, 'a': 1, 'semper.': 1, 'pulvinar.': 1, 'eget,': 1, 'hac': 1}
    for x in res.keys():
        assert o[x] == res[x]


def test_word3():
    o = word_3()
    res = ['\nLorem', 'sit', 'adipiscing', 'aliquam,', 'convallis', 'odio', 'ac', 'neque', 'Donec', 'varius', 'eu,', 'neque.', 'ut', 'blandit.', 'lacus', 'elementum,', 'accumsan', 'vulputate', 'eget', 'fringilla', 'Donec', 'mauris', 'Suspendisse', 'enim', 'Vestibulum', 'primis', 'orci', 'ultrices', 'curae;', 'ex,', 'consectetur', 'nec', 'ipsum', 'amet,', 'elit.', 'malesuada', 'semper', 'vitae', 'in', 'et', 'Cras', 'massa.', 'porttitor', 'porttitor', 'eu.', 'dui', 'interdum.\n\nMaecenas', 'tincidunt', 'cursus', 'metus.', 'magna', 'lacinia', 'ut', 'vestibulum', 'aliquam', 'luctus', 'hendrerit', 'molestie', 'augue', 'Nam', 'enim.', 'urna', 'placerat,', 'rutrum', 'iaculis', 'non', 'sem,', 'nulla', 'hendrerit', 'sed', 'Curabitur', 'et', 'aliquet.', 'amet', 'lacinia', 'fringilla', 'ac', 'urna', 'quis', 'Vivamus', 'at', 'commodo.', 'velit', 'sed', 'elit', 'aliquet', 'Donec', 'tincidunt', 'quis', 'vulputate.\n\nCras', 'vel', 'placerat', 'amet', 'mollis', 'nulla', 'Etiam', 'porttitor', 'non,', 'nunc.', 'luctus', 'at', 'Sed', 'ex,', 'tellus', 'Fusce', 'nisi,', 'tempor', 'eget.\n\nIn', 'augue', 'Curabitur', 'ipsum.', 'feugiat', 'aliquam.', 'dignissim', 'varius', 'non', 'at', 'enim', 'in', 'Integer', 'in', 'porta.', 'quam,', 'condimentum', 'quis', 'sed', 'sem', 'in', 'Vivamus', 'volutpat', 'vel,', 'lectus.', 'habitasse', 'Suspendisse', 'vitae', 'vestibulum.', 'dui', 'convallis', 'ultricies', 'mi', 'volutpat,', 'lobortis', 'ipsum', 'in', 'erat', 'Integer', 'ac', 'scelerisque.', 'magna', 'eros', 'ut', 'Lorem', 'sit', 'adipiscing', 'lacinia', 'Proin', 'sed', 'porta.', 'nisl', 'auctor', 'vel.', 'odio', 'venenatis', 'blandit', 'tincidunt']
    assert o == res


def test_letter3():
    o = letter_3()
    print(hashlib.md5(o.encode('utf-8')))
    res = "a1da61cbb6ec1582db34e6600e32c4bb"
    assert hashlib.md5(o.encode('utf-8')).hexdigest() == res