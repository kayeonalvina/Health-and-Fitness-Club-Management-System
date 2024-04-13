-- Adding sample data for all tables

INSERT INTO People (first_name, last_name, phone_number, email, age, gender, address) VALUES
('John', 'Doe', '123-456-7890', 'john.doe@example.com', 30, 'M', '123 Main St'),
('Jane', 'Smith', '234-567-8901', 'jane.smith@example.com', 25, 'F', '456 Oak Ave'),
('Bob', 'Johnson', '345-678-9012', 'bob.johnson@example.com', 35, 'M', '789 Pine Ln'),
('Alice', 'Williams', '456-789-0123', 'alice.williams@example.com', 28, 'F', '321 Elm St'),
('Charlie', 'Brown', '567-890-1234', 'charlie.brown@example.com', 32, 'M', '654 Spruce Dr'),
('David', 'Davis', '678-901-2345', 'david.davis@example.com', 29, 'M', '987 Birch Rd'),
('Eve', 'Evans', '789-012-3456', 'eve.evans@example.com', 27, 'F', '210 Cedar Ave'),
('Frank', 'Franklin', '890-123-4567', 'frank.franklin@example.com', 31, 'M', '543 Maple St');

INSERT INTO ExerciseRoutines (description) VALUES
('Cardio and strength training'),
('Yoga and meditation'),
('High-intensity interval training'),
('Weightlifting and bodybuilding'),
('Pilates and core exercises');

INSERT INTO Members (person_id, routine_id, init_weight, final_weight, height, body_fat, goal, time_weeks, balance) VALUES
(1, 1, 200, 180, 72, 15.0, 'Lose weight', 12, 1000.00),
(2, 2, 150, 140, 65, 20.0, 'Maintain weight', 6, 4500.00),
(3, 3, 180, 170, 70, 18.0, 'Gain muscle', 8, 500.00),
(4, 4, 160, 155, 68, 22.0, 'Lose weight', 10, 700.00),
(5, 5, 190, 185, 74, 17.0, 'Maintain weight', 4, 25.00);

INSERT INTO FitnessAchievements (description) VALUES
('Ran a marathon'),
('Completed a triathlon'),
('Climbed a mountain'),
('Won a bodybuilding competition'),
('Achieved a black belt in martial arts');

INSERT INTO MemberAchievements (member_id, achievement_id, date_achieved) VALUES
(1, 1, '2021-01-15'),
(2, 2, '2021-02-20'),
(3, 3, '2021-03-25'),
(4, 4, '2021-04-30'),
(5, 5, '2021-05-05');

INSERT INTO Trainers (person_id) VALUES
(6),
(7),
(8);

INSERT INTO Availability (trainer_id, day_of_week, start_hour) VALUES
(1, 1, 8),
(1, 2, 9),
(1, 3, 10),
(1, 4, 11),
(1, 5, 12),
(1, 6, 13),
(1, 7, 14),
(2, 1, 9),
(2, 2, 10),
(2, 3, 11),
(2, 4, 12),
(2, 5, 13),
(2, 6, 14),
(2, 7, 15),
(3, 1, 10),
(3, 2, 11),
(3, 3, 12),
(3, 4, 13),
(3, 5, 14),
(3, 6, 15),
(3, 7, 16);

INSERT INTO Events (trainer_id, room, cost, available, total_capacity) VALUES
(1, 101, 50.00, 0, 1),
(2, 102, 75.00, 0, 1),
(3, 103, 100.00, 1, 1),
(1, 104, 125.00, 2, 5),
(2, 105, 25.00, 0, 1),
(3, 105, 150.00, 0, 5);

INSERT INTO MemberEvents (member_id, event_id, day_of_week, start_hour) VALUES
(1, 3, 1, 8),
(2, 1, 2, 9),
(3, 2, 3, 10),
(1, 4, 4, 11),
(3, 4, 4, 11),
(4, 4, 4, 11),
(5, 5, 5, 12),
(1, 6, 6, 13),
(2, 6, 6, 13),
(3, 6, 6, 13),
(4, 6, 6, 13),
(5, 6, 6, 13);

INSERT INTO Equipment (label, defective_count, total_quantity) VALUES
('Dumbbells', 0, 10),
('Kettlebells', 1, 5),
('Resistance bands', 0, 10),
('Yoga mats', 0, 5),
('Medicine balls', 0, 5),
('Jump ropes', 0, 5);

INSERT INTO EquipmentUsage (equipment_id, event_id, num_in_use) VALUES
(1, 3, 4),
(2, 4, 5),
(3, 5, 2),
(4, 6, 1),
(5, 6, 5),
(6, 6, 0);