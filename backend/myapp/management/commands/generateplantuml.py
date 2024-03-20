from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from myapp.api import api
import json


class Command(BaseCommand):
    help = "Generates the plantUML representation"

    def add_arguments(self, parser):
        parser.add_argument('--output', required=False)

    def handle(self, *args, **options):
        output_file = options["output"]
        if not output_file:
            output_file = Path("openapi") / "openapi.json"
        else:
            output_file = Path(output_file)

        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(json.dumps(api.get_openapi_schema(), indent=2))
        self.stdout.write(f"OpenAPI specification written in {output_file}, located at {output_file.resolve()}")
