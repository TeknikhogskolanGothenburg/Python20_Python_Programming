def compare(value):
    return value[1]

def main():
    text = "Democratic nominee Joe Biden and President Donald Trump are going head-to-head on the hyper-sensitive issues of civic violence and racial justice in a potentially defining moment for a suddenly electrified battle for the White House. At a raw moment in modern American political history, the rivals are emerging from conventions that offered starkly different visions of the future, with every day in the campaign increasingly crucial -- as some states prepare to start sending out absentee ballots in the coming weeks."

    letter_count = {}

    for letter in text:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    sorted_order = sorted(letter_count.items(), key=compare, reverse=True)
    print(sorted_order)


if __name__ == '__main__':
    main()
