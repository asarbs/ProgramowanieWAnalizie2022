lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas aliquam, purus id convallis lacinia, magna odio finibus sapien, ac auctor dui neque eget felis. Donec augue ligula, varius sed ligula eu, pellentesque elementum neque. Ut consequat ut enim et blandit. Pellentesque euismod, lacus vitae bibendum elementum, elit justo accumsan mauris, quis vulputate turpis justo eget diam. Vivamus fringilla lobortis consequat. Donec dignissim eget mauris quis tempus. Suspendisse interdum consectetur enim nec bibendum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Fusce erat ex, tincidunt id consectetur varius, accumsan nec metus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tincidunt malesuada elementum. Nunc semper in risus vitae dapibus. Etiam in molestie nisl, et tempus lectus. Cras vel suscipit massa. Ut tempus porttitor eros, vel porttitor arcu pretium eu. Vivamus euismod dui vel dignissim interdum.

Maecenas vitae quam tincidunt nunc porttitor cursus eget nec metus. Vivamus a magna at ante lacinia semper. Duis ut lacus dictum, vestibulum nulla et, aliquam magna. Phasellus luctus ligula et hendrerit euismod. Phasellus molestie risus et augue aliquam tincidunt. Nam iaculis tempus enim. Vivamus bibendum, urna vel egestas placerat, justo metus rutrum orci, id iaculis lectus ante non metus.

Morbi arcu sem, tempus maximus nulla eget, suscipit hendrerit mauris. Nam sed pulvinar massa. Curabitur id turpis et lacus ultrices aliquet. Nunc sit amet nulla vulputate, lacinia nibh id, fringilla tortor. Donec ac ipsum eget urna venenatis ornare quis vel arcu. Vivamus finibus ante at felis interdum commodo. Morbi at velit dolor. Quisque sed nibh at elit elementum ultrices aliquet vel libero. Donec efficitur magna tincidunt augue porttitor, quis laoreet mauris vulputate.

Cras quis tortor vel erat consequat placerat eget sit amet odio. Nulla mollis elit id nulla commodo auctor. Etiam est metus, porttitor vel massa non, pretium porttitor nunc. Sed consequat luctus convallis. Sed at leo dui. Sed tempor tincidunt ex, sed eleifend tellus dictum luctus. Fusce congue est nisi, sit amet tempor nisl iaculis eget.

In gravida id augue vel ultrices. Curabitur at faucibus ipsum. Maecenas pulvinar feugiat diam eu aliquam. Maecenas eu dignissim metus. Morbi varius eu orci non pulvinar. Maecenas at odio placerat enim eleifend cursus in ut tellus. Integer vehicula lorem in lectus venenatis porta. Aenean felis quam, semper nec condimentum et, condimentum quis ante. Etiam sed tortor at sem convallis lobortis in eu mi. Vivamus leo enim, volutpat eu dolor vel, consectetur elementum lectus. In hac habitasse platea dictumst. Suspendisse porttitor erat vitae ligula accumsan vestibulum. Suspendisse nec dui eu mauris convallis dignissim. Donec ultricies enim vel mi vestibulum mollis.

Quisque volutpat, nulla et lobortis sagittis, ligula ipsum tincidunt ante, in mollis odio erat ut nisl. Integer id risus ac dui semper scelerisque. Sed non magna sit amet eros mattis ultrices ut at tellus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur lacinia gravida consectetur. Proin sed est sed sem pretium porta. Duis consectetur nisl justo, et auctor ipsum viverra vel. Nunc vel odio tortor. Aliquam venenatis enim diam, blandit sagittis risus tincidunt ut. Sed.
"""


def letter_counter():
    return len(lorem_ipsum)


def word_split():
    return lorem_ipsum.split(" ")


def word_counter():
    return len(word_split())


def cast_to_set():
    return set(word_split())


def word_occurrence():
    out = {}
    for w in cast_to_set():
        out[w] = 0
        for te in word_split():
            if w == te:
                out[w] = out[w] + 1
    return out


def word_3():
    return word_split()[::3]


def letter_3():
    return lorem_ipsum[::3]
