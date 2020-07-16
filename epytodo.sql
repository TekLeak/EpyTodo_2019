CREATE DATABASE IF NOT EXISTS epytodo
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
USE epytodo;

CREATE TABLE IF NOT EXISTS user (
    `user_id` int(11) NOT NULL AUTO_INCREMENT,
    username varchar(25) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (`user_id`),
    UNIQUE (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS task (
    task_id int(11) NOT NULL AUTO_INCREMENT,
    title varchar(25) NOT NULL,
    begin datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end datetime DEFAULT NULL,
    status ENUM('not started', 'in progress', 'done') NOT NULL DEFAULT 'not started',
    PRIMARY KEY (task_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS user_has_task (
    fk_user_id int(11) NOT NULL,
    fk_task_id int(11) NOT NULL,
    CONSTRAINT fk_user_id FOREIGN KEY (fk_user_id) REFERENCES user(`user_id`),
    CONSTRAINT fk_task_id FOREIGN KEY (fk_task_id) REFERENCES task(task_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;