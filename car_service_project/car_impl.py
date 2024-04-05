from car import Car

# Concrete Car Implementation
class CarImpl(Car):
    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
