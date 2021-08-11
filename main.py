"""Simple API

This is a working example of a simple api done with
bottle.py and intended to be used as a Google Cloud Run
service.

"""

import sys
import datetime
import bottle
import routes.auth
import routes.example
import routes.storage
import models.base
import routes.vg_info

app = bottle.Bottle()

app.mount("/vg_info", routes.vg_info.app)
#app.mount("/vg_info/Cheats", routes.vg_info.app)
#app.mount("/vg_info/EasterEgg", routes.vg_info.app)
#app.mount("/vg_info/Opinion", routes.vg_info.app)
# curl localhost:8080/vg_info/<tu-0ruta>
#app.mount("/auth", routes.auth.app)
#app.mount("/storage", routes.storage.app)
#app.mount("/vg_info/add", routes.vg_info.app)
#app.mount("/vg_info/<vg_codigo>/Cheats", routes.vg_info.app)
#app.mount("/vg_info/<vg_codigo>/Easter_Egg", routes.vg_info.app)
#app.mount("/vg_info/<vg_codigo>/Opinion", routes.vg_info.app)
#app.mount("/auth", routes.auth.app)
#app.mount("/storage", routes.storage.app)


@app.get("/")
def root_index(*args, **kwargs):
    return dict(code=200)


if __name__ == '__main__':
    error = False
    if (argv_len := len(sys.argv)) > 1:
        if sys.argv[1] == 'routes':
            for route in app.routes:
                print(route.rule, route.method, route, sep="\t")
        if sys.argv[1] == 'db' and 'migrate' in sys.argv:
            print("Database Migration:")
            now_iso = datetime.datetime.utcnow().isoformat()
            models.base.migrate_database(now_iso)
        else:
            error = True
    elif error:
        print("Bad use")
    else:
        app.run(host="0.0.0.0", port=8080)
