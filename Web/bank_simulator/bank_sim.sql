CREATE DATABASE bank_sim;
USE bank_sim;
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    password VARCHAR(20),
    name VARCHAR(100),
    mobile VARCHAR(15),
    email VARCHAR(100),
    aadhaar VARCHAR(20),
    pan VARCHAR(20),
    address TEXT
);

CREATE TABLE accounts (
    acc_no INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    type VARCHAR(20),
    balance DECIMAL(10,2),
    t_pin VARCHAR(10),

    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE transactions (
    txn_id INT PRIMARY KEY AUTO_INCREMENT,
    acc_no INT,
    amount DECIMAL(10,2),
    type VARCHAR(20),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT,

    FOREIGN KEY (acc_no) REFERENCES accounts(acc_no),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);