import os

def main():
    for dirpath, dirlist, filelist in os.walk("./folder"):
        for filename in filelist:
            if filename.endswith(".txt"):
                with open(os.path.join(dirpath, filename), "a") as file:
                    file.write(f"Hej {filename}")



if __name__ == '__main__':
    main()
