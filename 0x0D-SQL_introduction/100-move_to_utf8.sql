-- Convert the database to UTF8
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the hbtn_0c_0 database
USE `hbtn_0c_0`;

-- Convert the first_table to UTF8
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Change the character set of the 'name' field in first_table
ALTER TABLE `first_table` CHANGE `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

