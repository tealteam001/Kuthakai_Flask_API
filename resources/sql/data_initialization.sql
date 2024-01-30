DELETE FROM food.food_portion_type;
ALTER SEQUENCE food.food_portion_type_id_seq RESTART WITH 1;
INSERT INTO food.food_portion_type (type, description)
    VALUES ('full', 'Meal is some how ok for 2 people');
INSERT INTO food.food_portion_type (type, description)
    VALUES ('normal', 'Meal is perfect for single person');
	
DELETE FROM "user".user_type;
ALTER SEQUENCE "user".user_type_id_seq RESTART WITH 1;
INSERT INTO "user".user_type (type, description)
    VALUES ('cook', 'Person who cooks the meal');
INSERT INTO "user".user_type (type, description)
    VALUES ('manager', 'Person who manage the entire restuarent');
INSERT INTO "user".user_type (type, description)
    VALUES ('admin', 'Person who maintain the system');
	
DELETE FROM "user".privilage_entity;
ALTER SEQUENCE "user".privilage_entity_id_seq RESTART WITH 1;
INSERT INTO "user".privilage_entity (name, description)
    VALUES ('user', 'An entity to handle user attributes');
INSERT INTO "user".privilage_entity (name, description)
    VALUES ('food', 'An entity to handle food attributes');
INSERT INTO "user".privilage_entity (name, description)
    VALUES ('order', 'An entity to handle order attributes');
INSERT INTO "user".privilage_entity (name, description)
    VALUES ('customer', 'An entity to handle customer attributes');
	
DELETE FROM "order".order_type;
ALTER SEQUENCE "order".order_type_id_seq RESTART WITH 1;
INSERT INTO "order".order_type (type, description)
    VALUES ('delivery', 'Here the order is delivered to the customer');
INSERT INTO "order".order_type (type, description)
    VALUES ('dinning', 'Here the order is served to the customer');
INSERT INTO "order".order_type (type, description)
    VALUES ('takeaway', 'Here the order is take by customer');
	
DELETE FROM "order".order_status;
ALTER SEQUENCE "order".order_status_id_seq RESTART WITH 1;
INSERT INTO "order".order_status (name, description)
    VALUES ('pending', 'Here the order is given but its not yet started');
INSERT INTO "order".order_status (name, description)
    VALUES ('processing', 'Here the order is started to get processed');
INSERT INTO "order".order_status (name, description)
    VALUES ('out', 'Here the order is processed and ready for serve');
	
DELETE FROM "order".order_food_status;
ALTER SEQUENCE "order".order_food_status_id_seq RESTART WITH 1;
INSERT INTO "order".order_food_status (name, description)
    VALUES ('pending', 'Here the food of an order is not started to cook');
INSERT INTO "order".order_food_status (name, description)
    VALUES ('cooking', 'Here the food of an order is started to cook');
INSERT INTO "order".order_food_status (name, description)
    VALUES ('cooked', 'Here the food of an order is cooked');
	

DELETE FROM "order".discount_type;
ALTER SEQUENCE "order".discount_type_id_seq RESTART WITH 1;
INSERT INTO "order".discount_type (type, description)
    VALUES ('percentage', 'Here the discount is calculated through a specific percentage of the order amount');
INSERT INTO "order".discount_type (type, description)
    VALUES ('raw_amount', 'Here the discount is calculated by subtracting a specific amount form the order amount');
	

DELETE FROM "order".payment_type;
ALTER SEQUENCE "order".payment_type_id_seq RESTART WITH 1;
INSERT INTO "order".payment_type (type, description)
    VALUES ('card', 'Here the order amount is given as cash');
INSERT INTO "order".payment_type (type, description)
    VALUES ('cash', 'Here the order amount is given through card');
INSERT INTO "order".payment_type (type, description)
    VALUES ('loan', 'Here the order amount is taken as a loan');