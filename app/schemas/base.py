from marshmallow import validate

TRANSACTION_TYPES = ["expense", "income"]

TransactionTypeValidator = validate.OneOf(
    TRANSACTION_TYPES, error="Type must be 'expense' or 'income'."
)