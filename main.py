from ui.design import MainWindow
from storage.secure_storage import SecureStorage
from accounts.manager import AccountManager

def main():
    # Initialize secure storage
    storage = SecureStorage()

    # Initialize account manager
    account_manager = AccountManager(storage)

    # Set up the main application window
    app = MainWindow(account_manager)

    # Start the application
    app.run()

if __name__ == "__main__":
    main()