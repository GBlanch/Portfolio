    def __init__(
        self,
        client = MongoClient(host = 'localhost', port =*****),
        db = 'abtest' , 
        collection = 'applicants'
    ):
        self.collection = client[db][collection]
