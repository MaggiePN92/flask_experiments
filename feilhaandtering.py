class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, id_from_req, status_code=None, payload=None):
        super().__init__()
        self.message = message
        self.id = id_from_req
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['id'] = self.id
        return rv

    def feil_mld(self):
        return {
            "id":self.id,
            "data":[self.payload],
            "message":self.message
        }
