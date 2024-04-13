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

CREATE TABLE ExerciseRoutines (
    routine_id SERIAL PRIMARY KEY,
    description VARCHAR(1023)
);

CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
    person_id INT REFERENCES People(person_id),
    routine_id INT REFERENCES ExerciseRoutines(routine_id),
    init_weight INT,
    final_weight INT,
    height INT,
    body_fat FLOAT,
    goal VARCHAR(255),
    time_weeks INT,
    balance FLOAT
);

CREATE TABLE FitnessAchievements (
    achievement_id SERIAL PRIMARY KEY,
    description VARCHAR(255)
);

CREATE TABLE MemberAchievements (
    member_id INT REFERENCES Members(member_id),
    achievement_id INT REFERENCES FitnessAchievements(achievement_id),
    PRIMARY KEY (member_id, achievement_id),
    date_achieved DATE
);

CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,
    person_id INT REFERENCES People(person_id)
);

CREATE TABLE Availability (
    trainer_id INT REFERENCES Trainers(trainer_id),
    day_of_week INT,
    start_hour INT
);

CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,
    trainer_id INT REFERENCES Trainers(trainer_id),
    room INT,
    cost FLOAT,
    available INT,
    total_capacity INT
);

CREATE TABLE MemberEvents (
    member_id INT REFERENCES Members(member_id),
    event_id INT REFERENCES Events(event_id),
    PRIMARY KEY (member_id, event_id),
    day_of_week INT,
    start_hour INT
);

CREATE TABLE Equipment (
    equipment_id SERIAL PRIMARY KEY,
    label VARCHAR(255) NOT NULL,
    defective_count INT,
    total_quantity INT
);

CREATE TABLE EquipmentUsage (
    equipment_id INT REFERENCES Equipment(equipment_id),
    event_id INT REFERENCES Events(event_id),
    PRIMARY KEY (equipment_id, event_id),
    num_in_use INT
);
