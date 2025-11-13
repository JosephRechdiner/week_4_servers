class CaeserManager:
    def caeser_encrypter(text, offset):      
        result = ""
        for letter in text:
            if not letter.isalpha():
                result += letter
                continue

            stay_in_alphabet = ord(letter) + offset 
            if stay_in_alphabet > ord('z') or stay_in_alphabet > ord('z'):
                stay_in_alphabet -= 26

            result += chr(stay_in_alphabet)
        return result


    def caeser_decrypter(text, offset):
        result = ""
        for letter in text:
            if not letter.isalpha():
                result += letter
                continue

            stay_in_alphabet = ord(letter) - offset 
            if stay_in_alphabet < ord('a') or stay_in_alphabet < ord('A'):
                stay_in_alphabet += 26
                
            result += chr(stay_in_alphabet)
        return result