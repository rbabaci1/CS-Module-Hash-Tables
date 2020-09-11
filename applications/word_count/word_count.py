def word_count(s):
    separators = '":;,.-+=/\|[]{}()*^&'
    words = s.split()
    res = {}

    for word in words:
        word = word.strip(separators).lower()
        if not word:
            break
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello."))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )

