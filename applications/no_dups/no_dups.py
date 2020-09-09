def no_dups(s):
    res = []
    for w in s.split():
        if w not in res:
            res.append(w)

    return " ".join(res)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
