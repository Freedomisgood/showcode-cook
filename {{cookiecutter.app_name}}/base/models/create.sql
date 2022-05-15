SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

CREATE DATABASE if not EXISTS  `{{ cookiecutter.db_name }}` ;
use `stocks`;

-- ----------------------------
-- Table structure for {{ cookiecutter.table_name }}
-- ----------------------------
DROP TABLE IF EXISTS `{{ cookiecutter.table_name }}`;
CREATE TABLE `{{ cookiecutter.table_name }}`
(
    `id`                     int(11) NOT NULL AUTO_INCREMENT,
    `pub_date`               DATE NOT NULL COMMENT "发布日期",
    `board_team`               VARCHAR(255) DEFAULT NULL COMMENT "连板梯队",
    `break_board_num`          INTEGER(24) DEFAULT NULL COMMENT "炸板家数",
    `board_suc_rate`         FLOAT(24)    DEFAULT NULL COMMENT "封板率",
    `continuous_board_num`     INTEGER(24) DEFAULT NULL COMMENT "连板家数",
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET
FOREIGN_KEY_CHECKS = 1;

-- ALTER TABLE `{{ cookiecutter.table_name }}` MODIFY `title` VARCHAR(256);
