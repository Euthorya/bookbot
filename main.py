from stats import wordcount
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents =  f.read()
    print(f"{wordcount(file_contents)} words found in the document")
    report = letter_report(charactercount(file_contents))
    for i in report:
        print(f"The '{i[0]}: {i[1]}'")



def charactercount(text):
    result = {}
    for character in text:
        lower = character.lower()
        if lower not in result:
            result[lower] = 1
        else:
            result[lower] += 1
    return result

def letter_report(report):
    result = []
    for key in report:
        if key.isalpha():
            result.append((key, report[key]))
    result.sort(reverse=True, key=lambda x: x[1])
    return result


main()
