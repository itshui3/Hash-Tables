def word_count(s, cache=None):
    # Implement me.
    cache = {}
    
    sanitized = map(lambda i : i.strip('":;,.-+=/\\|[]{}()*^&').lower(), s.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ').split(' '))

    for i in sanitized:
        if i == "":
            continue
        if i not in cache:
            cache[i] = 1
        else:
            cache[i] += 1

    print('cache return', cache)
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))