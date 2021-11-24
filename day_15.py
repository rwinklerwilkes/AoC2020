from aocd import get_data

input_data = get_data(year=2020, day=15)
test_data = """0,3,6"""

def process_input(input_data):
    return [int(i) for i in input_data.split(',')]

def play_game(input_data, last_turn):
    processed = process_input(input_data)
    all_prior_said = {val:[i] for i, val in enumerate(processed)}
    day = len(processed)
    last_number_said = processed[-1]
    while day < last_turn:
        day_said = all_prior_said.get(last_number_said, []).copy()
        if len(day_said) <= 1:
            #today's number is 0
            today_number = 0
            today_said = all_prior_said.get(today_number, []).copy()
            today_said.append(day)
            all_prior_said[today_number] = today_said
        else:
            today_number = day_said[-1] - day_said[-2]
            today_said = all_prior_said.get(today_number, []).copy()
            today_said.append(day)
            all_prior_said[today_number] = today_said
        last_number_said = today_number
        day += 1
    print(last_number_said)
    return all_prior_said

all_prior_said = play_game(input_data, 2020)