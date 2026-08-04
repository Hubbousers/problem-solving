-- select MAX(case when dr = 2 then salary end) as SecondHighestSalary  from
-- (
-- select salary, DENSE_RANK() OVER (order by salary desc) as dr from Employee where salary is not null
-- ) t;

# Write your MySQL query statement below
select max(salary) as SecondHighestSalary from Employee where salary not in (select max(salary) from Employee);

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna