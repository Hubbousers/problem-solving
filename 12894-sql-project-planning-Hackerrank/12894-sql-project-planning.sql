WITH project_starts AS (
    SELECT Start_Date
    FROM projects
    WHERE Start_Date NOT IN (
        SELECT DISTINCT End_Date
        FROM projects
    )
),
projects_ends AS (
    SELECT End_Date
    FROM projects
    WHERE End_Date NOT IN (
        SELECT DISTINCT Start_Date
        FROM projects
    )
)
SELECT
    s.Start_Date,
    MIN(e.End_Date)
FROM project_starts s
INNER JOIN projects_ends e
    ON s.Start_Date < e.End_Date
GROUP BY s.Start_Date
ORDER BY
    (MIN(e.End_Date) - s.Start_Date) ASC,
    s.Start_Date ASC;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna