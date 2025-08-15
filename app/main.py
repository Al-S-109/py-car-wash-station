from typing import Any


class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    pass


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: float,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price += self.calculate_washing_price(car)
                car.clean_mark = self.wash_single_car(car)
        return price

    def calculate_washing_price(self, car: Car) -> float:
        differance = self.clean_power - car.clean_mark
        price = (
            car.comfort_class * differance * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, rate: float) -> Any:
        total_score = self.average_rating * self.count_of_ratings
        total_score += rate
        self.count_of_ratings += 1
        new_score = total_score / self.count_of_ratings
        self.average_rating = round(new_score, 1)
    pass
