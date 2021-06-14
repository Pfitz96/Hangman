import random
from Stages import stages
from words import words


class Hangman:
    tries = 7
    word = ''
    field = []
    hidden_word = []
    wasted_letters = set()

    def run(self):
        self.word_to_list()

        while '_' in self.field:
            print(''.join(self.field))
            letter = input('Pick a letter: ').upper()

            if self.valid_input(letter) == letter and letter not in self.wasted_letters:
                self.wasted_letters.add(letter)
                print("You have used these letters: " + ' '.join(self.wasted_letters))

                if letter in self.hidden_word:
                    while letter in self.hidden_word:
                        place = self.hidden_word.index(letter)
                        self.field[place] = letter
                        self.hidden_word[place] = '_'

                else:
                    print(f'{letter} is not in the word chosen!')
                    self.tries -= 1
                    print(self.stagies())
                    print(f'You have {self.tries} tries left!')
                    if self.tries == 0:
                        break

            else:
                if letter in self.wasted_letters:
                    print("You have already used this letter, try with another one!")
                else:
                    print("Please try again with a letter this time!")

        self.the_end()

    def valid_input(self, letter):
        if letter.isalpha() and len(letter) == 1:
            return letter
        else:
            pass

    def get_word(self, words):
        pick = random.choice(words)
        self.word = pick.upper()
        return self.word

    def get_rdy(self):
        self.tries = 7
        self.field = []
        self.hidden_word = []
        self.wasted_letters = set()

    def word_to_list(self):
        self.get_rdy()
        self.get_word(words)
        for i in self.word:
            self.hidden_word.append(i)
            self.field.append('_')

    def stagies(self):
        return stages[self.tries]

    def the_end(self):
        if self.tries == 0:
            print(f'You ran out of tries! The word was: "{self.word}"')
            self.play_again()
        else:
            print(f'Not bad at all kid, you guessed the word, "{self.word}"!')
            self.play_again()


    def play_again(self):
        while input("Play again? (Y/N): ").upper() == "Y":
            obj.run()


if __name__=='__main__':
    obj = Hangman()
    obj.run()


