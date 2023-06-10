from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.ride import Ride
from flask_app.models.user import User
from flask_app.models.join_ride import JoinRide



#===================This method take you to the Dashboard page==============================
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'user_id': session['user_id']
    }
    user = User.get_one(data)
    rides = Ride.get_all_rides()
    joined_rides = JoinRide.check_ride(data)
    list_joined_rides = []
    if joined_rides:
        for ride in joined_rides:
            list_joined_rides.append(ride['ride_id'])
    return render_template("dashboard.html", user=user, rides=rides, list_joined_rides=list_joined_rides)


# #===================Creating a Ride==============================
@app.route('/add_new_ride', methods=['POST'])
def create_ride():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Ride.validate_ride(request.form):
        return redirect('/dashboard')
    data = {
        "user_id": session['user_id'],
        "from_location": request.form["from_location"],
        "to_location": request.form["to_location"],
        "when_time": request.form["when_time"],
        "seats": request.form["seats"]
    }
    Ride.add_ride(data)
    return redirect('/dashboard')


# #===================Deleting a Book==============================
@app.route('/dashboard/destroy_ride/<int:id>')
def delete_ride(id):
    if 'user_id' not in session:
        return redirect('/logout')
    del_data = {
        "id": id
    }
    Ride.delete_ride(del_data)
    JoinRide.remove_from_joins(del_data)
    return redirect('/dashboard')


#===================Logout method==============================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/log_page')
