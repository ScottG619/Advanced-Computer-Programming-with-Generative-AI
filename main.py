from rental import Vehicle, Renter, ElectricCar, Motorbike


def main():
    print("=== Siam University Vehicle Rental ===")

    car = Vehicle("Toyota", "Yaris", "1AB234")
    electric_car = ElectricCar("Tesla", "Model 3", "EV999", 75)
    motorbike = Motorbike("Honda", "Click", "MB123", 125)
    renter = Renter("Mai", 123456)

    print("\n--- New vehicles ---")
    print(car)
    print(electric_car)
    print(motorbike)

    print("\n--- Renter ---")
    print(renter)
    print("Rented list:", renter.rented)

    print("\n--- Rent and return ---")
    car.rent()
    renter.rented.append(car)
    print("After renting:")
    print(car)

    car.return_vehicle()
    renter.rented.remove(car)
    print("After returning:")
    print(car)

    print("\n--- Validation tests ---")
    try:
        Renter("", 1001)
    except ValueError as error:
        print("Bad name caught:", error)

    try:
        Renter("Somchai", 0)
    except ValueError as error:
        print("Bad license caught:", error)

    try:
        renter.name = ""
    except ValueError as error:
        print("Changing name caught:", error)

    try:
        renter.license_no = -50
    except ValueError as error:
        print("Changing license caught:", error)

    print("\n--- Mixed vehicle list: polymorphism ---")
    vehicles = [car, electric_car, motorbike]
    for vehicle in vehicles:
        print(vehicle)


if __name__ == "__main__":
    main()
