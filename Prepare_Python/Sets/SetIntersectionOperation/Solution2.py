_ = input()
english_subscribers = set(input().split())


_ = input()
french_subscribers = set(input().split())

print(len(english_subscribers.intersection(french_subscribers)))
