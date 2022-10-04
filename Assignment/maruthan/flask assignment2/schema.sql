DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    password TEXT NOT NULL
);

INSERT INTO users (username, password, name, email) VALUES (
    "21","Kuberan@3"
);