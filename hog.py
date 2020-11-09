from random import randint

def make_fair_dice(sides):
    ''' Создание игральной кости с количеством сторон sides 
    >>> one_sided_dice = make_fair_dice(1)
    >>> one_sided_dice()
    1
    '''
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice(sides):
        return randint(1, sides)
    return dice
	
'''
four_sided_dice = make_fair_dice(4)
six_sided_dice = make_fair_dice(6)
>>> four_sided_dice()
1
>>> four_sided_dice()
2
>>> four_sided_dice()
3
'''

goal = 100

def roll_dice(num_rolls, dice=six_sided_dice, who='Grand Jedi Master Yoda'):
    ''' Вычисляет количество очков для игрока who после num_rolls бросков
    игральной кости dice.

    num_rolls:  Количество бросков, которое необходимо выполнить
    dice:       Функция без аргументов, которая возвращает целое число
    who:        Имя игрока
    '''
    assert type(num_rolls) == 'int', 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # *** YOUR CODE HERE ***
    pass

commentary = False

def take_turn(num_rolls, opponent_score, dice=six_sided_dice, who='Grand Jedi Master Yoda'):
    ''' Моделирует num_rolls бросоков (возможно 0) игральной кости 
    dice игрока who.

    num_rolls:      Количество бросков, которое необходимо выполнить
    opponent_score: Количество очков у оппонента
    dice:           Функция без аргументов, которая возвращает целое число
    who:            Имя текущего игрока
    '''
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    if commentary:
        print(who, 'is going to roll', num_rolls, 'dice')
    # *** YOUR CODE HERE ***
    pass



def is_prime(n):
    pass

def next_prime(n):
    pass


def announce(outcome, who):
    ''' Выводит на экран описание броска who с результатом outcome.'''
    print(who, 'rolled a', outcome)
    print(draw_number(outcome))


def draw_number(n, dot='*'):
    ''' Возвращает текстовое представление выпавших очков n. Если число имеет 
    несколько возможных представлений (например, 2 или 3), то выбрано может
    быть любое.

    >>> print(draw_number(3))
     -------
    |     * |
    |   *   |
    | *     |
     -------

    >>> print(draw_number(5))
     -------
    | *   * |
    |   *   |
    | *   * |
     -------

    >>> print(draw_number(6, '$'))
     -------
    | $   $ |
    | $   $ |
    | $   $ |
     -------
    '''
    #*** YOUR CODE HERE ***"
    pass


def draw_dice(c, f, b, s, dot):
    ''' Вовзращает ASCII рисунок, представляющий бросок кубика.

     -------
    | b   f |
    | s c s |
    | f   b |
     -------

    c, f, b, s -- булевы значения; нужно или нет поместить точки 
                  в соответствующие позиции.
    dot        -- строка длиной 1, для представления точки.
    '''
    assert len(dot) == 1, 'Dot must be a single symbol'
    border = ' -------'
    def draw(b):
        return dot if b else ' '
    c, f, b, s = map(draw, [c, f, b, s])
    top = ' '.join(['|', b, ' ', f, '|'])
    middle = ' '.join(['|', s, c, s, '|'])
    bottom = ' '.join(['|', f, ' ', b, '|'])
    return '\n'.join([border, top, middle, bottom, border])

def num_allowed_dice(score, opponent_score):
    ''' Возвращает максимальное количество кубиков, которое может выбрать игрок.
    Максимальное число кубиков 1, если сумма очков обоих игроков оканчивается 
    на 7, в противном случае 10.

    >>> num_allowed_dice(1, 0)
    10
    >>> num_allowed_dice(5, 7)
    10
    >>> num_allowed_dice(7, 10)
    1
    >>> num_allowed_dice(13, 24)
    1
    '''
    # *** YOUR CODE HERE ***
    pass


def select_dice(score, opponent_score):
    ''' Выбираем 4-х сторонний кубик, если сумма очков обоих игроков является
    множителем 7, иначе выбираем 6-и сторонний кубик.

    >>> select_dice(4, 24) == four_sided_dice
    True
    >>> select_dice(16, 64) == six_sided_dice
    True
    '''
    # *** YOUR CODE HERE ***
    pass

def play():
    ''' Игра '''
    pass
