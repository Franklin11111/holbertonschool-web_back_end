-- Creating 'users' table with unique attributes and not null

-- Verify if the table exists already
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, -- unique identifier for the user
    email VARCHAR(255) NOT NULL UNIQUE, -- unique email address
    name VARCHAR(255), -- user's name
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US' -- User's country, default value is 'US'
);
