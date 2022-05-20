# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    result = ''

    for i in range(len(str)):
        result += str[:i+1]
        # result += "\n"

    return result


print(string_splosion("Code"))
print(string_splosion("01234"))
