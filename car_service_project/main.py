from datetime import datetime
from car_factory import CarFactory

def main():
    # Current date for reference
    current_date = datetime.today().date()

    # Create a Calliope car instance
    calliope_car = CarFactory.create_calliope(
        current_date=current_date,
        last_service_date=datetime(2020, 5, 17).date(),
        current_mileage=35000,
        last_service_mileage=10000
    )

    # Create a Glissade car instance
    glissade_car = CarFactory.create_glissade(
        current_date=current_date,
        last_service_date=datetime(2019, 7, 29).date(),
        current_mileage=60000,
        last_service_mileage=20000
    )

    # Check if the cars need servicing
    print(f"Calliope needs servicing: {calliope_car.needs_service()}")
    print(f"Glissade needs servicing: {glissade_car.needs_service()}")

if __name__ == "__main__":
    main()
