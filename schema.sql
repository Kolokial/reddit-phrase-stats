CREATE TABLE IF NOT EXISTS read_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    postId TEXT UNIQUE NOT NULL
)