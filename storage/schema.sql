CREATE TABLE github_events (
    id SERIAL PRIMARY KEY,
    event_type TEXT,
    repo TEXT,
    user_login TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);