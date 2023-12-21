INPUT_FILE = 'day01.txt'

NUMBERS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_digit_index(s, is_first):
    n = len(s)
    idx = -1
    for i in range(n):
        if not s[i].isdigit():
            continue
        if is_first:
            return i
        idx = i
        
    return idx


def get_word_index(s, is_first):
    pos = 0x7FFFFFFF if is_first else -1
    num = None
    for number in NUMBERS:
        skip = 0
        while True:
            position = s.find(number, skip)
            if position == -1:
                break
            if is_first and position < pos or not is_first and position > pos:
                pos, num = position, number
            skip += len(number)
        
    return pos, num


def get_digit(line, is_first):
    digit_index = get_digit_index(line, is_first)
    word_index, word = get_word_index(line, is_first)
    
    if digit_index != -1 and word_index != -1:
        return line[digit_index] if is_first and digit_index < word_index or not is_first and digit_index > word_index else NUMBERS[word]
    elif digit_index != -1 and word_index == -1:
        return line[digit_index]
    else:
        return NUMBERS[word]


def part1():
    calibration = 0

    with open(INPUT_FILE) as lines:
        for line in lines:
            first_digit = line[get_digit_index(line, True)]
            last_digit = line[get_digit_index(line, False)]
            calibration += int(first_digit + last_digit)

    return calibration


def part2():
    calibration = 0

    with open(INPUT_FILE) as lines:
        for line in lines:
            first_digit = get_digit(line, True)
            last_digit = get_digit(line, False)
            calibration += int(first_digit + last_digit)

    return calibration


def main():
    print(f'Answer #1: {part1()}')

    print(f'Answer #2: {part2()}')
        

if __name__ == '__main__':
    main()
