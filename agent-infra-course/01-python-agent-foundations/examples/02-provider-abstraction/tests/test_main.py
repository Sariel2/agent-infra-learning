from app.main import EchoProvider, FakeLLMProvider, run_generation


def test_run_generation_with_echo_provider() -> None:
    assert run_generation(EchoProvider(prefix="p"), "x") == "p:x"


def test_run_generation_with_fake_provider() -> None:
    assert run_generation(FakeLLMProvider(answer="ok"), "x") == "ok|x"
