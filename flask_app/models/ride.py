from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE


class Ride:
    def __init__(self, data_base):
        self.id = data_base['id']
        self.from_location = data_base['from_location']
        self.to_location = data_base['to_location']
        self.when_time = data_base['when_time']
        self.seats = data_base['seats']
        self.user_id = data_base['user_id']
        self.created_at = data_base['created_at']
        self.updated_at = data_base['updated_at']
    
    #===================Adding a ride==============================
    @classmethod
    def add_ride(cls, data):
        query = "INSERT INTO rides (user_id, from_location, to_location, when_time, seats) VALUES (%(user_id)s, %(from_location)s, %(to_location)s, %(when_time)s, %(seats)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Getting all rides in the DB==============================
    @classmethod
    def get_all_rides(cls):
        query = "SELECT rides.id as id, rides.from_location as from_location, rides.to_location as to_location, rides.when_time as when_time, rides.seats as seats, rides.user_id as user_id, rides.created_at as created_at, rides.updated_at as updated_at, users.id as users_id, users.first_name as first_name, users.last_name as last_name FROM rides JOIN users ON users.id = user_id ;"
        results =  connectToMySQL(DATABASE).query_db(query)
        all_books = []
        for row in results:
            all_books.append( row )
        return all_books
    
    #===================Getting one ride by id along with user's informations==============================
    @classmethod
    def get_one_ride(cls, data):
        query = "SELECT rides.id as id, rides.from_location as from_location, rides.to_location as to_location, rides.when_time as when_time, rides.seats as seats, rides.user_id as user_id, rides.created_at as created_at, rides.updated_at as updated_at, users.id as users_id, users.first_name as first_name, users.last_name as last_name FROM rides JOIN users ON users.id = user_id WHERE rides.id = %(ride_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results[0]
    
    #===================Updating a ride by id==============================
    @classmethod
    def update_ride(cls, data):
        query = "UPDATE rides SET from_location=%(from_location)s, to_location=%(to_location)s, when_time=%(when_time)s, seats=%(seats)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Delete a ride by id==============================
    @classmethod
    def delete_ride(cls, data):
        query = "DELETE FROM rides WHERE rides.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Validate ride for creation or updating==============================
    @staticmethod
    def validate_ride(data_ride):
        is_valid = True
        if len(data_ride['from_location']) < 1:
            is_valid = False
            flash("You can't add a ride without starting point!","ride")
        if len(data_ride['to_location']) < 1:
            is_valid = False
            flash("You can't add a ride without adding the destination!","ride")
        return is_valid