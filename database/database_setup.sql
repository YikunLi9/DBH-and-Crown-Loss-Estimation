-- Create the database
CREATE DATABASE IF NOT EXISTS TreeData;

-- Use the newly created database
USE TreeData;

-- Create the table to store tree measurement data
CREATE TABLE IF NOT EXISTS TreeMeasurements (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-incrementing unique ID
    tree_serial_number VARCHAR(50) NOT NULL,  -- Tree serial number
    measurement_date DATE NOT NULL,  -- Date of measurement
    dbh DECIMAL(5,2) NOT NULL,  -- Diameter at Breast Height (DBH) with two decimal precision
    crown_loss DECIMAL(5,2) NOT NULL,  -- Crown loss percentage with two decimal precision
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create indexes to optimize common queries
CREATE INDEX idx_tree_serial_date ON TreeMeasurements (tree_serial_number, measurement_date);
CREATE INDEX idx_measurement_date ON TreeMeasurements (measurement_date);
CREATE INDEX idx_dbh ON TreeMeasurements (dbh);

-- Create a trigger to update the 'updated_at' field whenever a record is updated
DELIMITER $$
CREATE TRIGGER before_update_tree_measurements
BEFORE UPDATE ON TreeMeasurements
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END$$
DELIMITER ;
