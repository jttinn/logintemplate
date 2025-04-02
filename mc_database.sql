-- File Name: mc_database.sql
-- Version: 1.7
-- Last Updated: 26-Mar-2025
-- Description: SQL script for creating core MrClean administrative database and tables in the ods database, with initial data.

-- Drop the database if it already exists (for development reset purposes)
DROP DATABASE IF EXISTS ods;

-- Create the main database for the application
CREATE DATABASE ods
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Use the newly created database
USE ods;

-- Drop the user if it exists to avoid Error 1396 (operation CREATE USER failed)
DROP USER IF EXISTS 'odsdev'@'localhost';

-- Create a developer user with a secure password (xyzzy7 as placeholder)
CREATE USER 'odsdev'@'localhost' IDENTIFIED BY 'xyzzy7';

-- Grant all privileges on the ODS database to the developer user
GRANT ALL PRIVILEGES ON ods.* TO 'odsdev'@'localhost';

-- Apply changes to privilege tables
FLUSH PRIVILEGES;

-- Table for registered users
CREATE TABLE mc_users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) NOT NULL UNIQUE,
    user_given_name VARCHAR(50) NOT NULL,
    password_hash VARCHAR(128),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    force_reset BOOLEAN DEFAULT FALSE NOT NULL,
    user_created_by INT,
    user_created_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_updated_by INT,
    user_updated_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login_ts TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (user_created_by) REFERENCES mc_users(user_id),
    FOREIGN KEY (user_updated_by) REFERENCES mc_users(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for temporary verification codes
CREATE TABLE mc_temp_codes (
    temp_code_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) NOT NULL,
    code VARCHAR(6) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for user roles
CREATE TABLE mc_roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE,
    role_desc VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    role_added_by INT,
    role_added_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role_updated_by INT,
    role_updated_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (role_added_by) REFERENCES mc_users(user_id),
    FOREIGN KEY (role_updated_by) REFERENCES mc_users(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Junction table for user-role assignments
CREATE TABLE mc_user_roles (
    user_id INT NOT NULL,
    role_id INT NOT NULL,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES mc_users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES mc_roles(role_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for application features
CREATE TABLE mc_features (
    feature_id INT AUTO_INCREMENT PRIMARY KEY,
    feature_name VARCHAR(50) NOT NULL UNIQUE,
    feature_desc VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    feature_link VARCHAR(50) NOT NULL UNIQUE,
    feature_added_by INT,
    feature_added_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    feature_updated_by INT,
    feature_updated_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (feature_added_by) REFERENCES mc_users(user_id),
    FOREIGN KEY (feature_updated_by) REFERENCES mc_users(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Junction table for role-feature assignments
CREATE TABLE mc_role_features (
    role_id INT NOT NULL,
    feature_id INT NOT NULL,
    PRIMARY KEY (role_id, feature_id),
    FOREIGN KEY (role_id) REFERENCES mc_roles(role_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES mc_features(feature_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Initial Inserts for Default Roles in mc_roles
INSERT INTO mc_roles (role_name, role_desc, is_active, role_added_by, role_added_ts, role_updated_by, role_updated_ts)
VALUES
    ('PUBLIC', 'Access to areas on the website not requiring a user account', TRUE, NULL, CURRENT_TIMESTAMP, NULL, CURRENT_TIMESTAMP),
    ('ADMIN', 'All features', TRUE, NULL, CURRENT_TIMESTAMP, NULL, CURRENT_TIMESTAMP),
    ('ANALYST', 'File configuration, file upload, user profile', TRUE, NULL, CURRENT_TIMESTAMP, NULL, CURRENT_TIMESTAMP),
    ('ENDUSER', 'File upload, user profile', TRUE, NULL, CURRENT_TIMESTAMP, NULL, CURRENT_TIMESTAMP);

-- Initial Insert for Default Admin User in mc_users
-- Note: password_hash is a mock SHA-256 hash of '4mrClean!' for dev purposes; in production, use Werkzeug's generate_password_hash
INSERT INTO mc_users (email, user_given_name, password_hash, is_active, force_reset, user_created_by, user_created_ts, user_updated_by, user_updated_ts, last_login_ts)
VALUES
    ('road2row@gmail.com', 'MrClean', 'e2f7a1d4a4d7b4e5e2f7a1d4a4d7b4e5e2f7a1d4a4d7b4e5e2f7a1d4a4d7b4e5', TRUE, FALSE, NULL, CURRENT_TIMESTAMP, NULL, CURRENT_TIMESTAMP, NULL);

-- Update self-referential fields for admin user (user_id = 1)
UPDATE mc_users
SET user_created_by = 1, user_updated_by = 1
WHERE user_id = 1;

-- Assign ADMIN role to the default admin user in mc_user_roles
INSERT INTO mc_user_roles (user_id, role_id)
SELECT 1, role_id
FROM mc_roles
WHERE role_name = 'ADMIN';