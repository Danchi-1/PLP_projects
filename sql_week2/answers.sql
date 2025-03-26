--Create tables and its headings
CREATE TABLE offices(
    employeeNumber INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(100),
    lastName VARCHAR(100),
    email VARCHAR(255),
    job VARCHAR(100)
);

CREATE TABLE products(
    productID INT AUTO_INCREMENT PRIMARY KEY,
    productName VARCHAR(255),
    quantityInStock INT,
    buyPrice DECIMAL(10,2)
);
CREATE TABLE payments( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    checkNumber VARCHAR(500),
    orderDate DATETIME,
    requiredDate DATETIME,
    paymentDate DATETIME,
    amount DECIMAL(10,2),
    productID INT,
    employeeNumber INT,
    `status` ENUM('Pending', 'Completed', 'Failed', 'Refunded') NOT NULL,
    method ENUM('Cash', 'Credit Card', 'Bank Transfer', 'Mobile Payment', 'PayPal', 'Debit Card') NOT NULL,
    FOREIGN KEY (productID) REFERENCES products(productID),
    FOREIGN KEY (employeeNumber) REFERENCES offices(employeeNumber)
);

--Created values for tables
INSERT INTO offices(employeeNumber, firstName, lastName, email, job) VALUES
(1001, 'John', 'Doe', 'john.doe@example.com', 'Sales Rep'),
(1002, 'Alice', 'Johnson', 'alice.johnson@example.com', 'Manager'),
(1003, 'Bob', 'Smith', 'bob.smith@example.com', 'Sales Rep'),
(1004, 'Emma', 'Brown', 'emma.brown@example.com', 'Accountant'),
(1005, 'Liam', 'Williams', 'liam.williams@example.com', 'Sales Rep'),
(1006, 'Olivia', 'Jones', 'olivia.jones@example.com', 'Technician'),
(1007, 'Ethan', 'Garcia', 'ethan.garcia@example.com', 'HR Manager'),
(1008, 'Sophia', 'Miller', 'sophia.miller@example.com', 'Assistant'),
(1009, 'James', 'Martinez', 'james.martinez@example.com', 'Engineer'),
(1010, 'Isabella', 'Rodriguez', 'isabella.rodriguez@example.com', 'Intern');

INSERT INTO products(productName, quantityInStock, buyPrice) VALUES
('Laptop', 50, 1200.00),
('Smartphone', 120, 600.00),
('Tablet', 80, 1800.00),
('Monitor', 40, 850.00),
('Keyboard', 200, 8700.00),
('Mouse', 150, 5900.00),
('Printer', 30, 3800.00),
('Desk Chair', 25, 1400.00),
('Headphones', 90, 7800.00),
('Camera', 15, 2600.00);

INSERT INTO payments(checkNumber, orderDate, requiredDate, paymentDate, amount, productID, employeeNumber, `status`, method) VALUES
('CHK001', '2025-03-20', '2025-03-25', '2025-03-26', 1500.50, 1, 1001, 'Completed', 'Credit Card'),
('CHK002', '2025-03-18', '2025-03-22', '2025-03-25', 750.00, 2, 1002, 'Pending', 'Bank Transfer'),
('CHK003', '2025-03-15', '2025-03-19', '2025-03-24', 2000.75, 3, 1003, 'Failed', 'Mobile Payment'),
('CHK004', '2024-02-28', '2024-03-03', '2024-03-04', 1000.00, 4, 1004, 'Failed', 'Debit Card'),
('CHK005', '2024-03-01', '2024-03-06', '2024-03-05', 9200.30, 5, 1005, 'Completed', 'Mobile Payment'),
('CHK006', '2024-03-02', '2024-03-07', '2024-03-06', 6300.00, 6, 1006, 'Pending', 'Credit Card'),
('CHK007', '2024-03-03', '2024-03-08', '2024-03-07', 4100.20, 7, 1007, 'Completed', 'Bank Transfer'),
('CHK008', '2024-03-04', '2024-03-09', '2024-03-08', 1500.80, 8, 1008, 'Refunded', 'PayPal'),
('CHK009', '2024-03-05', '2024-03-10', '2024-03-09', 8300.00, 9, 1009, 'Completed', 'Debit Card'),
('CHK010', '2024-03-06', '2024-03-11', '2024-03-10', 2900.50, 10, 1010, 'Failed', 'Mobile Payment');

--Write an SQL query to retrieve the checkNumber, paymentDate, and amount from the payments table.
SELECT  checkNumber, paymentDate, amount FROM payments;

--Write an SQL query to retrieve the orderDate, requiredDate, and status of orders that are currently 'In Process' from the orders table. Sort the results in descending order of orderDate

SELECT orderDate, requiredDate FROM payments
WHERE `status` = "pending"
ORDER BY orderDate DESC;
--Write a query to display the firstName, lastName, and email of employees whose job title is 'Sales Rep' and order them in descending order of employeeNumber.
SELECT firstName, lastName, email FROM offices
WHERE job = "Sales Rep"
ORDER BY employeeNumber DESC;
--Write a query to retrieve all the columns and records from the offices table.
SELECT * FROM payments;
--Write a query to fetch the productName and quantityInStock from the products table. Sort the results in ascending order of buyPrice and limit the output to 5 records.
SELECT productName, quantityInStock FROM products
WHERE LIMIT 5
ORDER BY buyPrice ASC;