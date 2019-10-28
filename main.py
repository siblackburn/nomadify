from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

##telling the app to run on this ip address. 0.0.0.0 means run it on all network interfaces
#main method gets called first, and then that runs the app

# in web browser type in http://localhost:5000/
#0.0.0.0 is a special flag to tell the computer to listen to all network interfaces (wifi, ethernet etc)
#127.0.0.1 is a special IP for things inside your computer to talk to each other. e.g. 2 apps
