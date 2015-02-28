__author__ = 's7a'


# The syllable counter
class SyllableCounter:

    # Constructor for the Syllable Counter class
    def __init__(self):
        # Unused
        pass

    # Count the number of syllables in word
    # Taken from https://github.com/akkana/scripts/blob/master/countsyl
    @staticmethod
    def count_syllables_alt(word):

        if word == "":
            return 0

        vowels = ['a', 'e', 'i', 'o', 'u']

        on_vowel = False
        in_diphthong = False
        min_syl = 0
        max_syl = 0
        last_char = None

        word = word.lower()
        for c in word:
            is_vowel = c in vowels

            if on_vowel is None:
                on_vowel = is_vowel

            if c == 'y':
                is_vowel = not on_vowel

            if is_vowel:
                if not on_vowel:
                    min_syl += 1
                    max_syl += 1
                elif on_vowel and not in_diphthong and c != last_char:
                    in_diphthong = True
                    max_syl += 1

            on_vowel = is_vowel
            last_char = c

        if word[-1] == 'e':
            min_syl -= 1

        if word[-1] == 'y' and not on_vowel:
            max_syl += 1

        return int((min_syl + max_syl) / 2)

    # Count the number of syllables in word
    # Taken from http://stackoverflow.com/q/14541303
    @staticmethod
    def count_syllables(word):

        if word == "":
            return 0

        count = 0

        vowels = 'aeiouy'
        word = word.lower().strip(".:;?!")

        if word[0] in vowels:
            count += 1

        for index in range(1,len(word)):
            if word[index] in vowels and word[index-1] not in vowels:
                count += 1

        if word.endswith('e'):
            count -= 1
        if word.endswith('le'):
            count += 1
        if count == 0:
            count += 1

        return count
