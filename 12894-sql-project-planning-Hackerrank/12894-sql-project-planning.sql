with start as (
    select start_date, row_number() over (order by start_date) as rn from projects where start_date not in (select distinct end_date from projects)
),
end as (
    select end_date, row_number() over (order by end_date) as rn from projects where end_date not in (select distinct start_date from projects)
)

select start.start_date, end.end_date from start inner join end on start.rn = end.rn order by DATEDIFF(end.end_date, start.start_date) asc, start.start_date asc;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna