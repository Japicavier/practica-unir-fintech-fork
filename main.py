import sys


def sort_list(words):
    return sorted(words)


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py palabra1 palabra2 palabra3 ...")
        return

    words = sys.argv[1:]
    sorted_words = sort_list(words)

    print("Palabras ordenadas:")
    for word in sorted_words:
        print(word)


if __name__ == "__main__":
    main()
