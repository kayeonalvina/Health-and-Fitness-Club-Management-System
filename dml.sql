-- Adding sample data for all tables

INSERT INTO People (first_name, last_name, phone_number, email, age, gender, address) VALUES
('John', 'Doe', '123-456-7890', 'john.doe@example.com', 30, 'M', '123 Main St'),
('Jane', 'Smith', '234-567-8901', 'jane.smith@example.com', 25, 'F', '456 Oak Ave'),
('Bob', 'Johnson', '345-678-9012', 'bob.johnson@example.com', 35, 'M', '789 Pine Ln'),
('Alice', 'Williams', '456-789-0123', 'alice.williams@example.com', 28, 'F', '321 Elm St'),
('Charlie', 'Brown', '567-890-1234', 'charlie.brown@example.com', 32, 'M', '654 Spruce Dr');
('David', 'Davis', '678-901-2345', 'david.davis@example.com', 29, 'M', '987 Birch Rd');
('Eve', 'Evans', '789-012-3456', 'eve.evans@example.com', 27, 'F', '210 Cedar Ave');
('Frank', 'Franklin', '890-123-4567', 'frank.franklin@example.com', 31, 'M', '543 Maple St');

INSERT INTO Members (person_id, init_weight, final_weight, height, body_fat, goal, time_weeks, balance) VALUES
(1, 200, 180, 72, 15.0, 'Lose weight', 12, 100.00),
(2, 150, 140, 65, 20.0, 'Maintain weight', 6, 50.00),
(3, 180, 170, 70, 18.0, 'Gain muscle', 8, 75.00),
(4, 160, 155, 68, 22.0, 'Lose weight', 10, 80.00),
(5, 190, 185, 74, 17.0, 'Maintain weight', 4, 25.00);

INSERT INTO Trainers (person_id) VALUES
(6),
(7),
(8);

INSERT INTO Events (trainer_id, room, cost, available, total_capacity) VALUES
(6, 101, 50.00, 0, 1),
(7, 102, 75.00, 0, 1),
(8, 103, 100.00, 1, 1);
(6, 104, 125.00, 2, 5);
(7, 105, 25.00, 0, 1);
(8, 105, 150.00, 0, 5);

INSERT INTO MemberEvents (member_id, event_id, day_of_week, start_hour, end_hour) VALUES
(1, 3, 1, 8, 9),
(2, 1, 2, 9, 10),
(3, 2, 3, 10, 11),
(1, 4, 4, 11, 12),
(3, 4, 4, 11, 12),
(4, 4, 4, 11, 12),
(5, 5, 5, 12, 13),
(1, 6, 6, 13, 14),
(2, 6, 6, 13, 14),
(3, 6, 6, 13, 14),
(4, 6, 6, 13, 14),
(5, 6, 6, 13, 14);

INSERT INTO Inventory (event_id, equipment_name, defective_count, total_quantity, in_use) VALUES
(3, 'Dumbbells', 0, 10, 0),
(4, 'Kettlebells', 1, 5, 1),
(5, 'Resistance bands', 0, 10, 0),
(6, 'Yoga mats', 0, 5, 0),
(6, 'Medicine balls', 0, 5, 0),
(6, 'Jump ropes', 0, 5, 0);