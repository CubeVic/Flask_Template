from application import create_app


app = create_app()

if __name__ == "__main__":
    # app.run(host='0.0.0.0') # this will tell the os to listent to all public IPs
    app.run()