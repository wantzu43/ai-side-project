-- create users table with id and name, and insert 3 sample records
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
INSERT INTO users (name) VALUES
('Alice'),
('Bob'),
('Charlie');
