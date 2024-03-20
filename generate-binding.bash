#!/usr/bin/env bash

# Generates the openAPI specification
(cd backend && python manage.py generate)


# Generates the typescript API binding
(cd frontend && npm run generate-client)
