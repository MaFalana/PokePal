from flask import Flask, jsonify, request, g, session, redirect, url_for
from flask_cors import CORS, cross_origin
import requests

import os

from cryptography.hazmat.primitives import serialization

from db import DatabaseManager


db = DatabaseManager("PokePal") # Create a DatabaseManager instance with your desired database name

app = Flask(__name__) # Initialize the Flask application
CORS(app) # and enable CORS

@app.route('/Login', methods=['GET']) # Logins user
@cross_origin()
def getUser():
    query = { 'Username': request.form['email'] }

    users = db.query("Users", query)

    for user in users:
        if(user['Password'] == request.form['password']):
            session['user'] = user

    print(f'User: {session["user"]}')

    data = {
        'Message': f'Successfully logged in as {user["Username"]}',
        'User': session['user']
    }

    return jsonify(data)

@app.route('/Register', methods=['POST']) # Register a new user
@cross_origin()
def postUser():
    newUser = {
        'Username': request.form['firstName'],
        'Password': request.form['password'],
        'Email': request.form['email'],
        'Saves': [],
        'Cheats': []
    }

    db.insert("Users", newUser)

    return jsonify({'Message': 'Connected to Register Endpoint'})

@app.route('/Save', methods=['GET']) # Gets save file so user can export
@cross_origin()
def getSave():
    return jsonify({'Message': 'Connected to Save Endpoint'})

@app.route('/Save', methods=['POST']) # Gets save file so user can import
@cross_origin()
def postSave():
    newSave = {
        'Game': request.form['firstName'],
        'File': request.form['password'],
        'Date': ''
    }

    

    db.insert("Saves", newSave)
    return jsonify({'Message': 'Connected to Save POST Endpoint'})


@app.route('/Cheats', methods=['GET']) # Gets Cheats for current game
@cross_origin()
def getCheats():
    return jsonify({'Message': 'Connected to Cheats Endpoint'})


@app.route('/Cheats', methods=['POST']) # Post Cheats for current game
@cross_origin()
def postCheats():
    return jsonify({'Message': 'Connected to Cheats POST Endpoint'})



@app.route('/Gen/I', methods=['GET']) # Get All Gen I Roms
@cross_origin()
def getGenI():
    path = "./Games/Generation 1"

    games = os.listdir(path) # Get the list of all files and directories
    
    data = {
        'Message': 'Connected to Gen I Endpoint',
        'Games': games
    }

    return jsonify(data) # I want to return an array of the game names


@app.route('/Gen/II', methods=['GET']) # Get All Gen II Roms
@cross_origin()
def getGenII():
    path = "./Games/Generation 2"

    games = os.listdir(path) # Get the list of all files and directories

    data = {
        'Message': 'Connected to Gen II Endpoint',
        'Games': games
    }

    return jsonify(data) # I want to return an array of the game names


@app.route('/Gen/III', methods=['GET']) # Get All Gen III Roms
@cross_origin()
def getGenIII():
    path = "./Games/Generation 3"

    games = os.listdir(path) # Get the list of all files and directories

    data = {
        'Message': 'Connected to Gen III Endpoint',
        'Games': games
    }

    return jsonify(data) # I want to return an array of the game names



def readGBA(rom):
    with open(rom, "rb") as rom_file:
        header = rom_file.read(192)

    # Extract specific information from the header
    game_title = header[0xA0:0xAC].decode("utf-8")
    maker_code = header[0xAC:0xB0].decode("utf-8")

    print(f'Game Title: {game_title}')




# Start the server when the script is run directly
if __name__ == '__main__':
    app.run()
    