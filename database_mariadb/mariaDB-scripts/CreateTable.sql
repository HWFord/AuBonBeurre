CREATE TABLE automates (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  unit_id INT(11) NOT NULL,
  sensor_id INT(11) NOT NULL,
  sensor_type INT(11) NOT NULL,
  cistern_temperature FLOAT NOT NULL,
  ambient_temperature FLOAT NOT NULL,
  cistern_milk_weight FLOAT NOT NULL,
  finish_product_weight FLOAT NOT NULL,
  pH FLOAT NOT NULL,
  kplus INT(11) NOT NULL,
  nacl FLOAT NOT NULL,
  salmonella_lvl INT(11) NOT NULL,
  ecoli_lvl INT(11) NOT NULL,
  listeria_lvl INT(11) NOT NULL,
  check_date DATETIME NOT NULL,
  send_date DATETIME NOT NULL
);