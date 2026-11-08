SELECT
    -- s.id as id,
    s.name as name
    -- p1.salary as salary,
    -- f.friend_id as friend_id,
    -- p2.salary as friend_salary
FROM students s
INNER JOIN friends f
    ON s.id = f.id
INNER JOIN packages p1
    ON s.id = p1.id
INNER JOIN packages p2
    ON f.friend_id = p2.id
WHERE p2.salary > p1.salary
ORDER BY p2.salary;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna