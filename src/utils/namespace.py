class NameSpace:

    class Schemas:

        class UserSchema:
            SCHEMA_NAME='user'
            class User:
                TABLE_NAME = 'user'
                ID =  'id'
                USER_NAME = 'user_name' 
                EMAIL = 'email' 
                PASSWORD = 'password'
                NIC = 'nic'
                CREATE_USER_ID='create_user_id'
                USER_TYPE_ID='user_type_id'
            class UserType: #Fixed
                TABLE_NAME = 'user_type'
                ID =  'id'
                TYPE = 'type' 
            class PrivilageEntity: #Fixed
                TABLE_NAME = 'privilage_entity'
                ID =  'id'
                NAME = 'name' 
            class DeleteAccess:
                TABLE_NAME = 'delete_access'
                ID =  'id'
                PRIVILAGE_ENTITY_ID = 'privilage_entity_id'
                USER_ID = 'user_id'
                CREATE_USER_ID='create_user_id'
            class CreateAccess:
                TABLE_NAME = 'create_access'
                ID =  'id'
                PRIVILAGE_ENTITY_ID = 'privilage_entity_id'
                USER_ID = 'user_id'
                CREATE_USER_ID='create_user_id'
            class EditAccess:
                TABLE_NAME = 'edit_access'
                ID =  'id'
                PRIVILAGE_ENTITY_ID = 'privilage_entity_id'
                USER_ID = 'user_id'
                CREATE_USER_ID='create_user_id'
            class ViewAccess:
                TABLE_NAME = 'view_access'
                ID =  'id'
                PRIVILAGE_ENTITY_ID = 'privilage_entity_id'
                USER_ID = 'user_id'
                CREATE_USER_ID='create_user_id'

        class FoodSchema:
            SCHEMA_NAME='food'
            class Food:
                TABLE_NAME = 'food'
                ID = 'id'
                PRICE = 'price' 
                NAME = 'name'
                DESCRIPTION = 'description' 
                CREATE_USER_ID= 'create_user_id'
            class FoodProtionType: #Fixed
                TABLE_NAME = 'food_portion_type'
                ID = 'id'
                TYPE = 'type' 
            class MapFoodFoodPortionType:
                TABLE_NAME = 'map_food_food_portion_type'
                ID = 'id'
                FOOD_ID='food_id'
                FOOD_PORTION_TYPE_ID='food_portion_type_id'
                CREATE_USER_ID='create_user_id'
            class FoodCategory:
                TABLE_NAME = 'food_category'
                ID =  'id'
                FOOD_CATEGORY = 'food_category' 
                CREATE_USER_ID='create_user_id'
            class MapFoodFoodCategory:
                TABLE_NAME = 'map_food_food_category'
                ID =  'id'
                FOOD_CATEGORY_ID = 'food_category_id' 
                FOOD_ID ='food_id'
                CREATE_USER_ID='create_user_id'

        class OrderSchema:
            SCHEMA_NAME='order'
            class Order:
                TABLE_NAME = 'order'
                ID = 'id'
                DESCRIPTION = 'description' 
                REQUESTED_TIME = 'requested_time'
                SUPPLIER_ID = 'supplier_id'
                CREATE_USER_ID= 'create_user_id'
                ORDER_TYPE_ID = 'order_type_id'
                ORDER_STATUS_ID = 'order_status_id'
                DISCOUNT_TYPE_ID = 'discount_type_id'
                CUSTOMER_ID = 'customer_id'
            class MapOrderFood:
                TABLE_NAME = 'map_order_food'
                ID = 'id'
                ORDER_ID = 'order_id' 
                FOOD_ID= 'food_id'
                COUNT = 'count'
            class OrderType: #Fixed
                TABLE_NAME = 'order_type'
                ID = 'id'
                TYPE = 'type' 
            class OrderStatus: #Fixed
                TABLE_NAME = 'map_food_food_portion'
                ID = 'id'
                STATUS='status'
            class DiscountType: #Fixed
                TABLE_NAME = 'food_category'
                ID =  'id'
                TYPE='type'

        class CustomerSchema:
            SCHEMA_NAME='customer'
            class Customer:
                TABLE_NAME = 'customer'
                ID =  'id'
                ADDRESS = 'address'
                USER_NAME = 'user_name' 
                EMAIL = 'email' 
                PASSWORD = 'password'
                PHONE_NUMBER = 'phone_number'
                CREATE_USER_ID='create_user_id'


    class BluePrint:
        USER_BLUEPRINT = "user_blueprint"
        FOOD_BLUEPRINT = "food_blueprint"
        ORDER_BLUEPRINT = "order_blueprint"
        CUSTOMER_BLUEPRINT = "customer_blueprint"
        FOOD_CATEGORY_BLUEPRINT = "food_category_blueprint"
        VIEW_ACCESS_BLUEPRINT = "view_access_blueprint"
        DELETE_ACCESS_BLUEPRINT = "delete_access_blueprint"
        EDIT_ACCESS_BLUEPRINT = "edit_access_blueprint"
        ADD_ACCESS_BLUEPRINT = "add_access_blueprint"


    class Endpoint:
        USER_BLUEPRINT = "/api/user"
        FOOD_BLUEPRINT = "/api/food"
        ORDER_BLUEPRINT = "/api/order"
        CUSTOMER_BLUEPRINT = "/api/customer"
        FOOD_CATEGORY_BLUEPRINT = "/api/food_category"
        VIEW_ACCESS_BLUEPRINT = "/api/view_access"
        DELETE_ACCESS_BLUEPRINT = "/api/delete_access"
        EDIT_ACCESS_BLUEPRINT = "/api/edit_access"
        ADD_ACCESS_BLUEPRINT = "/api/add_access"


    class StatusCode:
        class Success:
            STATUS_CODE_400 = 200
            STATUS_CODE_401 = 201
            STATUS_CODE_402 = 202
            STATUS_CODE_403 = 203
            STATUS_CODE_404 = 204
        class Redirect:
            STATUS_CODE_300 = 300
            STATUS_CODE_301 = 301
            STATUS_CODE_302 = 302
            STATUS_CODE_303 = 303
            STATUS_CODE_304 = 304
        class ClientError:
            STATUS_CODE_400 = 400
            STATUS_CODE_401 = 401
            STATUS_CODE_402 = 402
            STATUS_CODE_403 = 403
            STATUS_CODE_404 = 404
        class ServerError:
            STATUS_CODE_500 = 500
            STATUS_CODE_501 = 501
            STATUS_CODE_502 = 502
            STATUS_CODE_503 = 503
            STATUS_CODE_504 = 504

                
