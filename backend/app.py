import logging
import os
import socket

from flask import Flask, jsonify, request
from psycopg2 import OperationalError

from db import (
    database_is_ready,
    get_connection,
    initialize_database,
    release_connection,
)

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.get("/healthz")
def health():
    return jsonify({
        "status": "alive",
        "pod": socket.gethostname()
    }), 200


@app.get("/readyz")
def readiness():
    if database_is_ready():
        return jsonify({"status": "ready"}), 200

    return jsonify({
        "status": "not ready",
        "reason": "database unavailable"
    }), 503


@app.get("/loans")
def list_loans():
    connection = None

    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, borrower_name, loan_amount,
                       property_city, status, created_at
                FROM loans
                ORDER BY id;
            """)

            rows = cursor.fetchall()

        loans = [
            {
                "id": row[0],
                "borrower_name": row[1],
                "loan_amount": float(row[2]),
                "property_city": row[3],
                "status": row[4],
                "created_at": row[5].isoformat()
            }
            for row in rows
        ]

        return jsonify({
            "loans": loans,
            "pod": socket.gethostname()
        }), 200

    except (OperationalError, RuntimeError):
        if connection is not None:
            connection.rollback()

        app.logger.exception("Failed to fetch loans")
        return jsonify({"error": "Database unavailable"}), 503

    finally:
        if connection is not None:
            release_connection(connection)


@app.post("/loans")
def add_loan():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON body"}), 400

    name = data.get("borrower_name")
    amount = data.get("loan_amount")
    city = data.get("property_city")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Borrower name is required"}), 400

    if not isinstance(city, str):
        return jsonify({"error": "Property city is required"}), 400

    try:
        from decimal import Decimal, InvalidOperation

        if isinstance(amount, bool) or amount is None:
            raise InvalidOperation

        loan_amount = Decimal(str(amount))

        if not loan_amount.is_finite():
            raise InvalidOperation

        if loan_amount <= 0:
            raise ValueError

        if loan_amount.as_tuple().exponent < -2:
            raise ValueError

        if loan_amount >= Decimal("1000000000000"):
            raise ValueError

    except (InvalidOperation, ValueError, TypeError):
        return jsonify({"error": "Invalid loan amount"}), 400

    connection = None

    try:
        connection = get_connection()

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO loans (
                    borrower_name,
                    loan_amount,
                    property_city
                )
                VALUES (%s, %s, %s)
                RETURNING id;
            """, (
                name.strip(),
                loan_amount,
                city.strip()
            ))

            loan_id = cursor.fetchone()[0]

        connection.commit()

        return jsonify({
            "message": "Loan created",
            "id": loan_id
        }), 201

    except Exception:
        if connection is not None:
            connection.rollback()

        app.logger.exception("Failed to create loan")
        return jsonify({"error": "Unable to create loan"}), 503

    finally:
        if connection is not None:
            release_connection(connection)


if __name__ == "__main__":
    initialize_database()

    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=False
    )
