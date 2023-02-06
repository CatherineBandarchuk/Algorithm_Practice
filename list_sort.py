# my_sentence = ["love", "awesome", "great", "I", "words"]
my_sentence = "I love great awesome words"

def sort_by_length(sentence):

    if len(sentence) == 0:
        return []
        
    words_list = sentence.split(" ")

    for index in range(1, len(words_list)):
        temp = words_list[index]
        j = index - 1
        
        while j >= 0 and len(words_list[j]) > len(temp):
            words_list[j + 1] = words_list[j]
            j -= 1

        words_list[j + 1] = temp
        
    return words_list


def sort_by_length_2(sentence):
    array = sentence.split()
    i = 1
    while i < len(array):
        to_insert = array[i]
        j = i
        # Search in the sorted portion of the list
        # for the correct position to insert sentence[i]
        while j > 0 and len(array[j-1]) > len(to_insert):
            array[j] = array[j-1]
            j -= 1
        array[j] = to_insert
        i += 1
    return array