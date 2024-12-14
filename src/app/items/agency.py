import os
import pickle

from app.items.offer import Offer


class Agency:
    OFFERS_PATH = 'app\\data\\offers.pkl'
    USERS_PATH = 'app\\data\\users.pkl'

    def __init__(self):
        self.offers = self._load_data(self.OFFERS_PATH)
        self.users = self._load_data(self.USERS_PATH)

    @staticmethod
    def _load_data(path):
        if os.path.exists(path):
            return pickle.load(open(path, 'rb'))
        return []

    def _save_offers(self):
        with open(self.OFFERS_PATH, 'wb') as file:
            pickle.dump(self.offers, file)

    def add_offer(self, offer_id, offer_name, offer_price):
        self.offers.append(Offer(offer_id, offer_name, offer_price))
        self._save_offers()

    def get_offers(self):
        return self.offers

    def delete_offer(self, offer_id):
        self.offers = [item for item in self.offers if item.id != offer_id]
        self._save_offers()

    def get_user(self, user_id):
        filtered_user = [item for item in self.users if item.user_id == user_id]
        if len(filtered_user) == 0:
            return None
        return filtered_user[0]

    def save_users(self):
        with open(self.USERS_PATH, 'wb') as file:
            pickle.dump(self.users, file)
