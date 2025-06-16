class AccountManager:
    def __init__(self, storage):
        self.storage = storage

    def add_account(self, account_name, username, password):
        encrypted_password = self.storage.encrypt_password(password)
        self.storage.save_account(account_name, username, encrypted_password)

    def remove_account(self, account_name):
        self.storage.delete_account(account_name)

    def list_accounts(self):
        accounts = self.storage.get_all_accounts()
        return accounts

    def get_account(self, account_name):
        account = self.storage.get_account(account_name)
        if account:
            decrypted_password = self.storage.decrypt_password(account['password'])
            return {
                'account_name': account['account_name'],
                'username': account['username'],
                'password': decrypted_password
            }
        return None