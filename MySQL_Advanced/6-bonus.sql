-- Procedure for adding new correction for a student

DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INT,          -- ID of the user
    IN project_name VARCHAR(255), -- Name of the project
    IN score INT            -- Score
)
BEGIN
    DECLARE project_id INT;

    -- Checkif project already exists
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    -- If project does not exist create new
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID(); -- Get id of the new project
    END IF;

    -- Add correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;
//

DELIMITER ; 