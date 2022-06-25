class compute():

   
    def ev_needed(data):
        d = (2 * data['base'] + data["iv"] + (data["ev"] / 4)) * (data['level'] / 100)
        ev_needed = (((((data['stat'] / data['nature']) - d) * 400 ) / data['level']) / 4 ) * 4
        return ev_needed

