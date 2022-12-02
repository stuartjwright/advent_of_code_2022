from utils.data import read_data_as_list


loss = 0
draw = 3
win = 6
shape_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
outcomes = {
    'X': {
        'A': draw,
        'B': loss,
        'C': win
    },
    'Y': {
        'A': win,
        'B': draw,
        'C': loss
    },
    'Z': {
        'A': loss,
        'B': win,
        'C': draw
    }
}
choices = {
    'A': {
        'X': 'Z',
        'Y': 'X',
        'Z': 'Y'
    },
    'B': {
        'X': 'X',
        'Y': 'Y',
        'Z': 'Z'
    },
    'C': {
        'X': 'Y',
        'Y': 'Z',
        'Z': 'X'
    }
}

data = read_data_as_list(day=2)
games = [line.split() for line in data]

# Part 1
scores = []
for opponent, me in games:
    shape_score = shape_points[me]
    outcome_score = outcomes[me][opponent]
    scores.append(shape_score + outcome_score)
total = sum(scores)
print(f'Part 1 Solution: {total}')


# Part 2
scores = []
for opponent, intention in games:
    me = choices[opponent][intention]
    shape_score = shape_points[me]
    outcome_score = outcomes[me][opponent]
    scores.append(shape_score + outcome_score)
total = sum(scores)
print(f'Part 2 Solution: {total}')
