from operator import itemgetter


class Construct:
    def __init__(self, id, name, freq, lang_id):
        self.id = id
        self.name = name
        self.freq = freq
        self.lang_id = lang_id


class Lang:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ConstructLang:
    def __init__(self, lang_id, construct_id):
        self.lang_id = lang_id
        self.construct_id = construct_id


langs = [
    Lang(1, 'Алгол'),
    Lang(2, 'Паскаль'),
    Lang(3, 'Ада'),
    Lang(4, 'Си'),
    Lang(11, 'Алгол-68'),
    Lang(22, 'Модула-2'),
    Lang(33, 'Ассемблер'),
]

constructs = [
    Construct(1, 'Цикл for', 85, 1),
    Construct(2, 'Условный оператор if', 95, 2),
    Construct(3, 'Цикл while', 70, 3),
    Construct(4, 'Оператор case', 40, 3),
    Construct(5, 'Оператор goto', 10, 4),
    Construct(6, 'Блок begin-end', 60, 1),
]

constructs_langs = [
    ConstructLang(1, 1),
    ConstructLang(1, 6),
    ConstructLang(2, 2),
    ConstructLang(2, 6),
    ConstructLang(3, 3),
    ConstructLang(3, 4),
    ConstructLang(4, 5),
    ConstructLang(4, 2),
    ConstructLang(11, 1),
    ConstructLang(11, 5),
    ConstructLang(22, 4),
    ConstructLang(22, 3),
    ConstructLang(33, 5),
]


def main():
    one_to_many = [(c.name, c.freq, l.name) for l in langs for c in constructs if c.lang_id == l.id]

    many_to_many_temp = [(l.name, cl.lang_id, cl.construct_id) for l in langs for cl in constructs_langs if l.id == cl.lang_id]

    many_to_many = [(c.name, c.freq, lang_name) for lang_name, lang_id, construct_id in many_to_many_temp for c in constructs if c.id == construct_id]

    print('Задание Г1')
    res_1 = {l.name: [c for c, _, ln in one_to_many if ln == l.name] for l in langs if l.name.startswith('А') and any(ln == l.name for _, _, ln in one_to_many)}
    print(res_1)

    print('\nЗадание Г2')
    res_2_unsorted = []
    for l in langs:
        l_freqs = [f for _, f, ln in one_to_many if ln == l.name]
        if l_freqs:
            res_2_unsorted.append((l.name, max(l_freqs)))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание Г3')
    res_3 = sorted(many_to_many, key=itemgetter(2))
    print(res_3)


if __name__ == '__main__':
    main()
