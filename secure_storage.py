class SecureStorage:
    def __init__(self, storage_file='secure_storage.json'):
        self.storage_file = storage_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_data(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.data, file)

    def add_account(self, account_name, encrypted_password):
        self.data[account_name] = encrypted_password
        self.save_data()

    def get_password(self, account_name):
        return self.data.get(account_name)

    def remove_account(self, account_name):
        if account_name in self.data:
            del self.data[account_name]
            self.save_data()