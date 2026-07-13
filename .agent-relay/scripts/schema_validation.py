from __future__ import annotations


def validate(instance, schema: dict, *, root: dict | None = None, path: str = "$"):
    """Validate the JSON-Schema subset used by relay control artifacts."""
    root = root or schema
    if "$ref" in schema:
        reference = schema["$ref"]
        if not reference.startswith("#/"): raise ValueError(f"{path}: unsupported external $ref {reference}")
        target = root
        for part in reference[2:].split("/"): target = target[part.replace("~1", "/").replace("~0", "~")]
        return validate(instance, target, root=root, path=path)
    if "oneOf" in schema:
        matches = 0
        for option in schema["oneOf"]:
            try: validate(instance, option, root=root, path=path); matches += 1
            except ValueError: pass
        if matches != 1: raise ValueError(f"{path}: expected exactly one oneOf match, got {matches}")
        return
    if "const" in schema and instance != schema["const"]: raise ValueError(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]: raise ValueError(f"{path}: value is outside enum")
    expected = schema.get("type")
    if expected:
        names = expected if isinstance(expected, list) else [expected]
        checks = {
            "object": lambda value: isinstance(value, dict),
            "array": lambda value: isinstance(value, list),
            "string": lambda value: isinstance(value, str),
            "integer": lambda value: isinstance(value, int) and not isinstance(value, bool),
            "number": lambda value: isinstance(value, (int, float)) and not isinstance(value, bool),
            "boolean": lambda value: isinstance(value, bool),
            "null": lambda value: value is None,
        }
        if not any(checks[name](instance) for name in names): raise ValueError(f"{path}: expected type {expected}")
    if isinstance(instance, dict):
        required = schema.get("required", [])
        missing = [key for key in required if key not in instance]
        if missing: raise ValueError(f"{path}: missing required properties {missing}")
        properties = schema.get("properties", {})
        additional = schema.get("additionalProperties", True)
        for key, value in instance.items():
            child = f"{path}.{key}"
            if key in properties: validate(value, properties[key], root=root, path=child)
            elif additional is False: raise ValueError(f"{child}: additional property is forbidden")
            elif isinstance(additional, dict): validate(value, additional, root=root, path=child)
    if isinstance(instance, list) and "items" in schema:
        for index, value in enumerate(instance): validate(value, schema["items"], root=root, path=f"{path}[{index}]")
    if isinstance(instance, (int, float)) and not isinstance(instance, bool) and "minimum" in schema and instance < schema["minimum"]:
        raise ValueError(f"{path}: value is below minimum {schema['minimum']}")
