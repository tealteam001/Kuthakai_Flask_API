# REST APIs Recording Project

Nothing here yet!


Sun 7 Jan:
1. Created the necessary schemas such as user, customer, order and food
2. Initialize the back end code architecture


To delete tables of specific schemas:
DROP TABLE "order".map_order_food;
DROP TABLE "order"."order";
DROP TABLE customer.customer;
DROP TABLE food.map_food_food_category;
DROP TABLE food.map_food_food_portion_type;
DROP TABLE food.food;
DROP TABLE food.food_category;
DROP TABLE food.food_portion_type;
DROP TABLE "order".discount_type;
DROP TABLE "order".order_food_status;
DROP TABLE "order".order_status;
DROP TABLE "order".order_type;
DROP TABLE "order".payment_type;
DROP TABLE "user".create_access;
DROP TABLE "user".delete_access;
DROP TABLE "user".view_access;
DROP TABLE "user".edit_access;
DROP TABLE "user".privilage_entity;
DROP TABLE "user".user;
DROP TABLE "user".user_type;

public schemas:
DROP TABLE alembic_version;
DROP TABLE items_tags;
DROP TABLE items;
DROP TABLE tags;
DROP TABLE stores;
DROP TABLE users;