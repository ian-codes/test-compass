
APP_SIGNUP_BODY_SCHEMA = {
    "type": "object",
    "properties": {
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string", "minLength": 8},
        "first_name": {"type": "string", "minLength": 2, "maxLength": 32},
        "last_name": {"type": "string", "minLength": 2, "maxLength": 32},
        "organization_name": {"type": "string", "maxLength": 150},
    },
    "required": [
        "email",
        "password",
        "first_name",
        "last_name",
    ],
}