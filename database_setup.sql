DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    performance_rating INTEGER
);

INSERT INTO employees VALUES
(1, 'Aman', 'IT', 60000, 4),
(2, 'Riya', 'HR', 45000, 3),
(3, 'Rahul', 'IT', 75000, 5),
(4, 'Neha', 'Finance', 50000, 4),
(5, 'Arjun', 'IT', 72000, 5),
(6, 'Simran', 'HR', 48000, 4),
(7, 'Vikas', 'Finance', 52000, 3),
(8, 'Pooja', 'IT', 68000, 4);
