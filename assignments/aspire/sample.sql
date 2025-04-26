-- // Design a query that safely deducts a wallet balance, preventing overdraws and race conditions, assuming the table:
-- // CREATE TABLE wallet (
-- //   user_id INT PRIMARY KEY,
-- //   balance DECIMAL(10,2) NOT NULL
-- // );
-- // Requirements:
-- // - Prevent negative balances.
-- // - Allow concurrent updates on different users.

TRANSACTION BEGIN

UPDATE WALLET SET BALANCE = BALANCE + 10 WHERE USER_ID = {USER_ID}

TRANSACTION END