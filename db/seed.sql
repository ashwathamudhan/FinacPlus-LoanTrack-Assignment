
INSERT INTO loans (
    borrower_name,
    loan_amount,
    property_city,
    status
)
SELECT
    seed.borrower_name,
    seed.loan_amount,
    seed.property_city,
    seed.status
FROM (
    VALUES
        ('Arun Kumar', 250000.00, 'Chennai', 'PENDING'),
        ('Priya Sharma', 500000.00, 'Bengaluru', 'APPROVED'),
        ('Rahul Verma', 175000.00, 'Hyderabad', 'PENDING'),
        ('Sneha Iyer', 750000.00, 'Chennai', 'APPROVED'),
        ('Karthik Raj', 320000.00, 'Coimbatore', 'REJECTED')
) AS seed (
    borrower_name,
    loan_amount,
    property_city,
    status
)
WHERE NOT EXISTS (SELECT 1 FROM loans);
