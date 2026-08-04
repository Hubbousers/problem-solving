CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
     select max(case when dr=N then salary end) as "getNthHighestSalary(2)" from (
        select salary, DENSE_RANK() OVER (ORDER BY salary desc) as dr from Employee where salary is not null
     ) t

  );
END

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna