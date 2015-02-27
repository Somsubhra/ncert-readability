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
        minsyl = 0
        maxsyl = 0
        lastchar = None

        word = word.lower()
        for c in word:
            is_vowel = c in vowels

            if on_vowel == None:
                on_vowel = is_vowel

            if c == 'y':
                is_vowel = not on_vowel

            if is_vowel:
                if not on_vowel:
                    minsyl += 1
                    maxsyl += 1
                elif on_vowel and not in_diphthong and c != lastchar:
                    in_diphthong = True
                    maxsyl += 1

            on_vowel = is_vowel
            lastchar = c

        if word[-1] == 'e':
            minsyl -= 1

        if word[-1] == 'y' and not on_vowel:
            maxsyl += 1

        return int((minsyl + maxsyl) / 2)

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
            count +=1

        for index in range(1,len(word)):
            if word[index] in vowels and word[index-1] not in vowels:
                count +=1

        if word.endswith('e'):
            count -= 1
        if word.endswith('le'):
            count+=1
        if count == 0:
            count +=1

        return count
