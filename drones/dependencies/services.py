from django.core.validators import RegexValidator


VALIDATE_CHARACTER = RegexValidator(
                        r'^(?=[0-9_]*[A-Z])\b[A-Z0-9_]+\b$', 
                        'only upper case letters, underscore, and numbers are valid characters'
                    )
