from app.items.agency import Agency
from app.items.offer import Offer

agency = Agency()

def create_offer(offer_name, offer_price):
    offer_id = 0 if len(agency.offers)==0 else max([item.id for item in agency.offers])+1
    agency.add_offer(offer_id, offer_name, offer_price)

def get_offer(offer_id):
    filtered_offers = [item for item in agency.offers if item.id == offer_id]
    if filtered_offers:
        return filtered_offers[0]
    return None

def get_offers():
    return [item for item in agency.offers]
    # return flask.render_template('\\templates\\get_offers.html')

def update_offer(offer_id, name, price):
    agency.offers = [item if item.id != offer_id else Offer(offer_id, name, price) for item in agency.offers ]

if __name__ == '__main__':
    agency = Agency()
    create_offer('Турція', 100)
    print(get_offers())
    print(get_offer(0))