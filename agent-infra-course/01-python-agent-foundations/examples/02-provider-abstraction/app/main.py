from dataclasses import dataclass
from typing import Protocol


class Provider(Protocol):
    def generate(self, prompt: str) -> str: ...


@dataclass
class EchoProvider:
    prefix: str = "echo"

    def generate(self, prompt: str) -> str:
        return f"{self.prefix}:{prompt}"


@dataclass
class FakeLLMProvider:
    answer: str = "fake-answer"

    def generate(self, prompt: str) -> str:
        return f"{self.answer}|{prompt}"


def run_generation(provider: Provider, prompt: str) -> str:
    return provider.generate(prompt)


def main() -> None:
    print(run_generation(EchoProvider(), "agent infra"))


if __name__ == "__main__":
    main()
