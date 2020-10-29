
def lower_decorator(func):
    def function_wrapper(word1, word2):
        return word1.lower() + " " + word2.lower()
    return function_wrapper

@lower_decorator
def quiet(word1, word2):
    return word1 + " " + word2

print(quiet('SHOUT', "LOUD"))