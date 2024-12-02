from app import App
from common.kafka.client import KafkaMigrator
from insurance.router.insurance import InsuranceRouter


def main():
    KafkaMigrator().migrate()  # вообще это должно быть где-нибудь в /src/utils/pre-start.py

    app = App.get_instance()
    app.include_router(InsuranceRouter())
    app.run()


if __name__ == "__main__":
    main()
