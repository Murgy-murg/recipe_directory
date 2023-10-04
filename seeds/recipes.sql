DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name text,
    cooking_time int,
    rating int
);

INSERT INTO recipes (name, cooking_time, rating) VALUES ('Roast dinner', 80, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Asparagus risotto', 40, 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Chilli con carne', 50, 3);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Leek and bean stew', 45, 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Loaded sweet potato', 60, 1);
