from website import create_app
app = create_app()

#Vytvoření aplikace
if __name__ == "__main__":
    app.run(debug=False, threaded=True)
