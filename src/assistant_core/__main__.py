import sys
from assistant_core.config import load_settings
from assistant_core.knowledge import OfficeDirectory, Handbook
from assistant_core.responder import StubLLMResponder
from assistant_core.service import AssistantService
from assistant_core.models import Message
from assistant_core.logging_setup import setup_logging

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m assistant_core <prompt>")
        sys.exit(1)

    settings = load_settings()
    setup_logging(settings.log_level)

    offices = OfficeDirectory.from_csv(settings.data_dir / "offices.csv")
    handbook = Handbook.from_json(settings.data_dir / "handbook.json")
    responder = StubLLMResponder()

    service = AssistantService(settings, offices, handbook, responder)
    response = service.handle(Message(text=sys.argv[1]))
    print(response.answer)

if __name__ == "__main__":
    main()