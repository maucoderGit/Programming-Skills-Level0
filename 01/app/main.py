from colors import bcolors
import models

import db as db
import bank_app


def run():
    all_models = db.get_all_table_names()
    for model_name, table_name in all_models:
        db.init_json_db_files(table_name.default)

    bank_app.run()


if __name__ == "__main__":
    run()
