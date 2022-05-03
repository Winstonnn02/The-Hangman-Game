import pygame


def create_image():
    pass


def remember_word():

    # Rewrite request in game screen

    # word = input('Input the word (3 and more letters): ')
    # if len(word) < 5:
    #     print('Word length must be more than 2 letters!')
    # return word
    pass


def create_word_box(word):
    pass


def get_letter():
    pass


def check_letter():
    pass


def main():
    background_color = (0, 225, 200)
    pygame.display.init()
    pygame.display.set_caption("The Hangman Game")
    screen = pygame.display.set_mode((800, 600))
    screen.fill(background_color)
    pygame.display.flip()


if __name__ == '__main__':
    main()
