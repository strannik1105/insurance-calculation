from app import App


def main():
    app = App.get_instance()
    app.run()


if __name__ == "__main__":
    main()
