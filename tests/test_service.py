import pytest
from assistant_core.config import Settings
from assistant_core.knowledge import Handbook, OfficeDirectory
from assistant_core.models import Intent, Message
from assistant_core.responder import StubLLMResponder
from assistant_core.service import AssistantService


@pytest.fixture
def service(tmp_path):
    settings = Settings(data_dir=tmp_path)
    offices = OfficeDirectory({})
    handbook = Handbook([])
    responder = StubLLMResponder()
    return AssistantService(settings, offices, handbook, responder)


def test_handle_greeting(service):
    res = service.handle(Message(text="hi"))
    assert res.intent == Intent.GREETING
    assert "Hello" in res.answer


def test_fallback_when_provider_fails(tmp_path):
    settings = Settings(data_dir=tmp_path)
    offices = OfficeDirectory({})
    handbook = Handbook([])
    responder = StubLLMResponder(fail=True)
    svc = AssistantService(settings, offices, handbook, responder)

    res = svc.handle(Message(text="some question"))
    assert res.intent == Intent.UNKNOWN or res.degraded