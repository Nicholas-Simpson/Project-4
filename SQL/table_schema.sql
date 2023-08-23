CREATE TABLE wine_train (
	id INT, 
	fixed_acidity FLOAT, 
	volatile_acidity FLOAT, 
	citric_acid FLOAT,
	residual_sugar FLOAT,
	chlorides FLOAT,
	free_SO2 FLOAT, 
	total_SO2 FLOAT, 
	density FLOAT, 
	pH FLOAT, 
	sulphates FLOAT, 
	alcohol FLOAT, 
	quality_score INT,
	PRIMARY KEY (id)
);

SELECT * FROM wine_train;

CREATE TABLE wine_test (
	id INT, 
	fixed_acidity FLOAT, 
	volatile_acidity FLOAT, 
	citric_acid FLOAT,
	residual_sugar FLOAT,
	chlorides FLOAT,
	free_SO2 FLOAT, 
	total_SO2 FLOAT, 
	density FLOAT, 
	pH FLOAT, 
	sulphates FLOAT, 
	alcohol FLOAT, 
	PRIMARY KEY (id)
);

SELECT * FROM wine_test;