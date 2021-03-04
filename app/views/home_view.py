class HomeView:
    def __init__(self, app):
        @app.route('/')
        def home():
            return {'Home': 'in construction'}