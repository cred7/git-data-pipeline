SELECT repo, COUNT(*)
FROM github_events
GROUP BY repo
ORDER BY COUNT(*) DESC
LIMIT 10;

SELECT user_login, COUNT(*)
FROM github_events
GROUP BY user_login
ORDER BY COUNT(*) DESC
LIMIT 10;

SELECT event_type, COUNT(*)
FROM github_events
GROUP BY event_type
ORDER BY COUNT(*) DESC;