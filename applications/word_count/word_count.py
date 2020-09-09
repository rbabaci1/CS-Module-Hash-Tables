import re


def word_count(s):
    # U
    # "Hello, "there" Rabah. We're there." ==> {"hello": 1, "there": 2, "rabah": 1 "we're": 1}
    separators = list('":;,.-+=/\|[]{}()*^&')

    # P
    # ignored characters: [ " : ; , . - + = / \ | [ ] { } ( ) * ^ & ]
    # if none of the ignored characters exists in s, return {}
    # 1- split s into words on any white spaces
    for c in separators:
        s = s.replace(c, "")
    words = s.split()
    # 2- create an empty dictionary
    res = {}
    # 3- iterate over the words list, count each word repetition num and save it into {}
    # while iterating, don't include the ignored characters and all keys must be lowercase
    for word in words:
        word = word.lower()
        if word not in res:
            res[word] = 1
        else:
            res[word] += 1
    return res


if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(
    #     word_count(
    #         "This is a test of the emergency broadcast network. This is only a test."
    #     )
    # )

