from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from myapp.api import api
import json


class Command(BaseCommand):
    help = "Generates the OpenAPI specification and plantUML diagram"

    def add_arguments(self, parser):
        parser.add_argument('--output', required=False)

    def handle(self, *args, **options):
        output_file = options["output"]
        if not output_file:
            output_file = Path("openapi") / "openapi.json"
        else:
            output_file = Path(output_file)

        self.generate_openapi_file(output_file)
        # self.generate_plantuml(api, output_file.parent)


    def generate_openapi_file(self, output_file: Path):
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(json.dumps(api.get_openapi_schema(), indent=2))
        self.stdout.write(f"OpenAPI specification written in {output_file}, located at {output_file.resolve()}")

    # def generate_plantuml(self, ninja_api, out_folder):
    #     spec = out_folder / "spec.plantuml"
    #     self.generate_plantml_model(ninja_api)
    #     import ipdb; ipdb.set_trace()  # fmt: skip


    # def generate_plantml_model(self, ninja_api):
    #     import ipdb; ipdb.set_trace()  # fmt: skip
