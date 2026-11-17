#!/usr/bin/env python3
"""Validate an AI Training Data Supplier Declaration against its schema (JSON Schema 2020-12).

Install: pip install jsonschema rfc3339-validator
Usage: python3 validate.py supplier-declaration.schema.json declaration.json
Exit 0 when valid; 1 with every error listed when not; 2 when the validator cannot
run. The validator refuses to run without the date and date-time format checks, or
with a library whose date check accepts a date that is not written YYYY-MM-DD.
MIT License.
"""
import json, sys

def cannot_run(message):
    print(message, file=sys.stderr)
    sys.exit(2)

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
    import rfc3339_validator  # noqa: F401  (enables the date-time format check)
except ImportError:
    cannot_run("install the validator and its format checks: pip install jsonschema rfc3339-validator")

def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except OSError as e:
        cannot_run(f"cannot read {path}: {e.strerror}")
    except ValueError as e:
        cannot_run(f"cannot read {path} as JSON: {e}")

def main(schema_path, doc_path):
    schema = load(schema_path)
    doc = load(doc_path)
    if not isinstance(schema, dict) or "$id" not in schema:
        cannot_run(f"{schema_path} is not a schema with an $id; the schema is the first argument")
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as e:
        cannot_run(f"{schema_path} is not a valid schema: {e.message}")
    checker = FormatChecker()
    strict = ({"date", "date-time"} <= set(checker.checkers)
              and checker.conforms("2000-01-01", "date") and checker.conforms("2000-01-01T00:00:00Z", "date-time")
              and not checker.conforms("20000101", "date") and not checker.conforms("yesterday", "date-time"))
    if not strict:
        cannot_run("format checks unavailable or lenient: pip install --upgrade jsonschema rfc3339-validator")
    v = Draft202012Validator(schema, format_checker=checker)
    errors = sorted(v.iter_errors(doc), key=lambda e: list(e.path))
    if not errors:
        print(f"valid: {doc_path} conforms to {schema.get('title')} ({schema.get('$id')})")
        return 0
    for e in errors:
        where = "/".join(str(p) for p in e.path) or "(root)"
        print(f"invalid at {where}: {e.message}")
    return 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        cannot_run(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
