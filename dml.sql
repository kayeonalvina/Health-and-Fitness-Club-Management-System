CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    init_weight INT,
    final_weight INT,
    height INT,
    body_fat FLOAT,
    goal VARCHAR(255),
    time_weeks INT,
    balance FLOAT,
    events[]
);

CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,
    events[]
);

CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,
    trainer_name INT,
    room INT,
    equipment[]
    members[]
    cost FLOAT,
    available INT,
    total_capacity INT
);

CREATE TABLE People (
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(255) NOT NULL UNIQUE,
    age INT,
    gender VARCHAR(1) NOT NULL,
    address VARCHAR(255)
);

CREATE TABLE Admin (
    admin_id SERIAL PRIMARY KEY
);

CREATE TABLE Calendar (
    time_week SERIAL PRIMARY KEY
);

CREATE TABLE Inventory (
    inventory_id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(255) NOT NULL,
    defective_count INT,
    total_quantity INT,
    in_use INT
);