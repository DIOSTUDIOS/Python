from faker import Faker


def test():
    data = Faker(locale='zh_CN')

    print(data.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))
    print('\n')
    print(data.text(max_nb_chars=6000, ext_word_list=None))


if __name__ == '__main__':
    test()
