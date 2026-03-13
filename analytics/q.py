import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5445,
    database="github",
    user="postgres",
    password="postgres"
)
curr = conn.cursor()
curr.execute(
    """SELECT repo, COUNT(*)
FROM github_events
GROUP BY repo
ORDER BY COUNT(*) DESC
LIMIT 10; """
)

results = curr.fetchall()
print("Top 10 repositories by event count:")
for repo, count in results:
    print(f"{repo}: {count} events")

# Close connection
curr.close()
conn.close()
