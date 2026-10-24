
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "invoices.json"


def load_invoices():
    """Read previously saved invoices from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            invoices = json.load(file)

        if not isinstance(invoices, list):
            return []

        return invoices

    except (json.JSONDecodeError, OSError):
        return []


def save_invoice(invoice):
    """Add an invoice and save the updated list."""
    invoices = load_invoices()
    invoices.append(invoice)

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(invoices, file, indent=4)

    return invoice
