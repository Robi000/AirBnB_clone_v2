-- We wil create a database calld hbb_test_db and a user with privilage
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
 
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
