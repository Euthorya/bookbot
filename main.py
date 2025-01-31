def main():
    with open("books/frankenstein.txt") as f:
        file_contents =  f.read()
    report = letter_report(charactercount(file_contents))
    for i in report:
        print(f"The '{i[0]}' character was found {i[1]} times")

def wordcount(text):
    return len(text.split())

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
