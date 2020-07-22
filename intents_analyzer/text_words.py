import csv

class Text:
    def __init__(self,text_file):
        self.words_list = []
        with open(text_file) as f:
            lines = f.readlines()
            for ll in lines:
                for ww in ll.split():
                    self.words_list.append(ww)

        for ww in self.words_list:
            print(ww)


def text_words_main():
    text = Text('data-results/benefits-utterances-texts-72.txt')

