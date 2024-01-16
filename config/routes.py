from app.root.route import rootRoute 
def routing(app):
    app.include_router(rootRoute)
    