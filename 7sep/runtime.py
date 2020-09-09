def main():
    times = []
    while True:
        while True:
            minutes = input("Enter minutes for this run: ")
            if minutes.isdigit():
                minutes = int(minutes)
                break
        while True:
            seconds = input("Enter seconds for this run: ")
            if seconds.isdigit():
                seconds = int(seconds)
                break
        if minutes == 0 and seconds == 0:
            break

        time = minutes * 60 + seconds
        times.append(time)

    avg = sum(times) / len(times)
    minutes = int(avg // 60)
    seconds = int(avg - minutes * 60)
    print(minutes)
    print(seconds)




if __name__ == '__main__':
    main()
