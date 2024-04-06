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
    balance FLOAT
);

CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,
    person_id INT REFERENCES People(person_id)
);

CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,
    trainer_name VARCHAR(255) NOT NULL,
    room INT,
    cost FLOAT,
    available INT,
    total_capacity INT
);

CREATE TABLE MemberEvents (
    member_id INT REFERENCES Members(member_id),
    event_id INT REFERENCES Events(event_id),
    PRIMARY KEY (member_id, event_id)
    day_of_week INT,
    start_hour INT,
    end_hour INT
);

CREATE TABLE Inventory (
    inventory_id SERIAL PRIMARY KEY,
    event_id INT REFERENCES Events(event_id),
    equipment_name VARCHAR(255) NOT NULL,
    defective_count INT,
    total_quantity INT,
    in_use INT
);
