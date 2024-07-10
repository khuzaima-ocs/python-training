li = [
    {"country": "Pakistan", "city": "Lahore", "state": "Punjab"},
    {"country": "Pakistan", "city": "Karachi", "state": "Sindh"},
    {"country": "Pakistan", "city": "Peshawar", "state": "KPK"},
    {"country": "Pakistan", "city": "Okara", "state": "Punjab"},
    {"country": "India", "city": "Delhi", "state": "Delhi"},
    {"country": "India", "city": "Mumbai", "state": "Maharashtra"},
    {"country": "India", "city": "Kolkata", "state": "West Bengal"},
    {"country": "USA", "city": "New York", "state": "New York"},
    {"country": "UK", "city": "Manchester", "state": "England"},
    {"country": "UK", "city": "London", "state": "England"}
]


def group_by(li, by, cols = []):

    if len(cols) == 0 and len(li) != 0:
        item = li[0]
        for key in item.keys():
            if key != by:
                cols.append(key)

    output = {}

    for item in li:
        output[item[by]] = output.get(item[by], [])

        obj = {}
        for col in cols:
            if col in item:
               obj[col] = item[col]

        output[item[by]].append(obj)

    return output

print(group_by(li, by='country', cols=["city"]))