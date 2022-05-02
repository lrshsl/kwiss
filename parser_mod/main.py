from parser import Parser


# def main():
#     file = 'lernsets/lat_verba_prima.txt'
#     question_pairs = Parser().get_question_pairs(file)
#     output = formated(question_pairs)
#     with open('output', 'w+') as f:
#         f.write(output)


def main():
    file = 'lernsets/lat_verba_undecima.txt'
    question_pairs = Parser().get_question_pairs(file)
    for pair in question_pairs:
        print(pair, end=',\n')


if __name__ == '__main__':
    main()
