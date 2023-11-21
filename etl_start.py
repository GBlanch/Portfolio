# Create `client`
client = MongoClient(host = 'localhost', port = ***** )

# Create `db`
db = client['abtest']

# Assign `"applicants"` collection to `gb_app`
gb_app = db['applicants']

# Aggregate applicants by nationality
result = gb_app.find_one({})

result = gb_app.aggregate(
    [
        {
            '$group':{'_id':'$country',
                      'count': {'$count' : {}
                                                    }
                     }
        }
    ]
)
