# %%micropython

from typing import List, Protocol

l: List[int] = [1, 2, 3]


class Speak(Protocol):
    def speak(self): ...


class Parrot:
    def speak(self) -> None:
        print("Polly wants a cracker")


def say_something(speaker: Speak) -> None:
    speaker.speak()


polly = Parrot()

print(say_something(polly))
# %%
