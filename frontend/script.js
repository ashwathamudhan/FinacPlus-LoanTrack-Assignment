
const API_BASE = "/api";

const form = document.getElementById("loanForm");
const table = document.getElementById("loansTable");
const message = document.getElementById("message");
const refreshBtn = document.getElementById("refreshBtn");

async function loadLoans() {
    table.innerHTML = "";

    try {
        const response = await fetch(`${API_BASE}/loans`);

        if (!response.ok) {
            throw new Error("Failed to fetch loans");
        }

        const data = await response.json();

        if (data.loans.length === 0) {
            const row = table.insertRow();
            const cell = row.insertCell();
            cell.colSpan = 5;
            cell.textContent = "No loans found";
            return;
        }

        data.loans.forEach((loan) => {
            const row = table.insertRow();

            const values = [
                loan.id,
                loan.borrower_name,
                Number(loan.loan_amount).toFixed(2),
                loan.property_city || "-",
                loan.status
            ];

            values.forEach((value) => {
                const cell = row.insertCell();
                cell.textContent = value;
            });
        });

    } catch (error) {
        const row = table.insertRow();
        const cell = row.insertCell();
        cell.colSpan = 5;
        cell.textContent = "Unable to load loans";
        console.error(error);
    }
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    message.textContent = "";

    const loan = {
        borrower_name: document.getElementById(
            "borrower_name"
        ).value.trim(),

        loan_amount: document.getElementById(
            "loan_amount"
        ).value,

        property_city: document.getElementById(
            "property_city"
        ).value.trim()
    };

    try {
        const response = await fetch(`${API_BASE}/loans`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(loan)
        });

        if (!response.ok) {
            throw new Error("Unable to create loan");
        }

        message.textContent = "Loan added successfully!";
        message.style.color = "green";

        form.reset();
        await loadLoans();

    } catch (error) {
        message.textContent = "Failed to add loan";
        message.style.color = "red";
        console.error(error);
    }
});

refreshBtn.addEventListener("click", loadLoans);

loadLoans();
