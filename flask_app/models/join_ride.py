from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class JoinRide:
    def __init__(self, data_base):
        self.id = data_base['id']
        self.user_id = data_base['user_id']
        self.ride_id = data_base['ride_id']
        self.created_at = data_base['created_at']
        self.updated_at = data_base['updated_at']
    
    #===================Join a User to a Ride==============================
    @classmethod
    def join_to_ride(cls, data):
        query = "INSERT INTO join_rides (user_id, ride_id) VALUES (%(user_id)s, %(ride_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Removes a User from a Ride==============================
    @classmethod
    def remove_from_ride(cls, data):
        query = "DELETE FROM join_rides WHERE user_id = %(user_id)s AND ride_id = %(ride_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    #===================Removes a Ride from joins==============================
    @classmethod
    def remove_from_joins(cls, data):
        query = "DELETE FROM join_rides WHERE ride_id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    #===================Select a joined ride by the user==============================
    @classmethod
    def get_one_join(cls,data):
        query = "SELECT * FROM join_rides WHERE user_id = %(user_id)s AND ride_id = %(ride_id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:  # Check if result exists
            return cls(results[0])  # Return the first dictionary object
        else:
            return None
    
    #===================Check if the User already joined the Ride==============================
    @classmethod
    def check_ride(cls, data):
        query = "SELECT ride_id FROM join_rides WHERE user_id = %(user_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return result
        else:
            return None

