CREATE TABLE People (
    person_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(255) NOT NULL UNIQUE,
    age INT,
    gender VARCHAR(1) NOT NULL,
    address VARCHAR(255)
);

CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    person_id INT REFERENCES People(person_id),
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
    person_id INT REFERENCES People(person_id),
    events[]
);

CREATE TABLE Admin (
    admin_id SERIAL PRIMARY KEY
    person_id INT REFERENCES People(person_id)
);

CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,
    trainer_name VARCHAR(255) NOT NULL,
    room INT,
    equipment[]
    members[]
    cost FLOAT,
    available INT,
    total_capacity INT
);

CREATE TABLE Inventory (
    inventory_id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(255) NOT NULL,
    defective_count INT,
    total_quantity INT,
    in_use INT
);

CREATE TABLE Calendar (
    time_week VARCHAR(11) NOT NULL,
    monday INT,
    tuesday INT,
    wednesday INT,
    thursday INT,
    friday INT,
    saturday INT,
    sunday INT,
);

INSERT INTO Calendar (time_week, monday, tuesday, wednesday, thursday, friday, saturday, sunday)
VALUES
(9:00-10:00, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(10:00-11:00, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(11:00-12:00, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(13:00-15:00, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(15:00-17:00, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(17:00-19:00, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(19:00-21:00, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(21:00-22:00, NULL, NULL, NULL, NULL, NULL, NULL, NULL);