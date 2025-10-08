-- Procedure ComputeAverageScoreForUser that computes average score

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT           -- user ID
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate mean score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update mean score of the user
    UPDATE users
    SET average_score = avg_score
    WHERE users.id = user_id;
END;
//

DELIMITER ;