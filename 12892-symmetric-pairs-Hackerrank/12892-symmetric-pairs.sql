select ot1.X as X, ot1.Y as Y from Functions ot1 inner join Functions ot2 on 
ot1.X = ot2.Y AND
ot1.Y = ot2.X
WHERE ot1.X <= ot1.Y
GROUP BY ot1.X, ot1.Y
HAVING
    ot1.X <> ot1.Y
    OR COUNT(*) >= 2
    order by ot1.X asc; 


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna