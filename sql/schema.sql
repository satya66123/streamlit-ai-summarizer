CREATE DATABASE summarizer_db;

USE summarizer_db;

CREATE TABLE summaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_text LONGTEXT,
    summary_text LONGTEXT,
    summary_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);