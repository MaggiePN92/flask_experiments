import json
from error_handling_and_logging.feilhaandtering import InvalidAPIUsage
import logging

class Bar:
    def __init__(self, some_data):
        some_data = json.loads(some_data)
        self.id = some_data["id"]
        print(f"Jobber med {self.id}.")
        try:
            self.sum_of_list = sum([int(i) for i in some_data["vals"].split(",")])
        except ValueError:
            logging.exception("Prøver å summere int og str.")
            raise InvalidAPIUsage(
                "Du proever aa summere str og int",
                self.id,
                status_code=400,
                payload=some_data
            )


    def get_data(self):
        return {self.id : self.sum_of_list}