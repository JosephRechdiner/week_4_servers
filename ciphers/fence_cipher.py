class FenceManager:
    def encrypter(text: str):
        new_text = text.replace(" ", "")
        evens = ""
        odds = ""
        for i in range(len(new_text)):
            if i % 2 == 0:
                evens += new_text[i]
            else:
                odds += new_text[i]
        return evens + odds

    def decrypter(text: str):
        result = ""
        if len(text) % 2 == 0:
            evens = text[:len(text) // 2]
            odds = text[len(text) // 2:]
        else:
            evens = text[:len(text) // 2 + 1]
            odds = text[len(text) // 2 + 1:]

        evens_pointer = 0
        odds_pointer = 0
        while evens_pointer < len(evens) and odds_pointer < len(odds):
            result += evens[evens_pointer]
            result += odds[odds_pointer]
            evens_pointer += 1
            odds_pointer += 1

        if evens_pointer == len(evens) - 1:
            result += evens[evens_pointer]
        if odds_pointer == len(odds) - 1:
            result += odds[odds_pointer]

        return result

