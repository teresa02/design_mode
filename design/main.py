# -*- coding: utf-8 -*-
from design.server import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, host='127.0.0.1', debug=True)