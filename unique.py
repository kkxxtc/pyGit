with open('/Users/apple/Desktop/ Uniqtext.txt') as text:
    words = list(map(lambda x: x.strip('!?().,'),text.read().lower().split()))
    let = dict(zip(words,map(lambda x:words.count(x),words)))
    print(*sorted(let.items(),key = lambda x:x[1],reverse=True))
