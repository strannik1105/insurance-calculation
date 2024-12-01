from app import App
from insurance.router.insurance import InsuranceRouter


def main():
    app = App.get_instance()
    app.include_router(InsuranceRouter())
    app.run()


if __name__ == "__main__":
    main()
