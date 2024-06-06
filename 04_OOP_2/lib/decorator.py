# 1. ✅ Demonstrate First Class Functions
# Create functions to be used as callbacks
# Create a higher-order function that will take a callback as an argument


def feed(pet):
    return f"{pet} has been fed!"


def walk(pet):
    return f"{pet} has been walked!"


def task_for_Mimi(func):
    return func("Mimi")


def task_for_Simon(func):
    return func("Simon")


print(task_for_Mimi(feed))
print(task_for_Mimi(walk))
print(task_for_Simon(feed))
print(task_for_Simon(walk))
# 2. ✅ Create a higher-order function that returns a function


def task_for_pet():
    def feed(pet):
        return f"{pet} has been fed!"

    return feed


print(task_for_pet()("Slash"))


# 3. ✅ Demonstrate a decorator
# Create a function that takes a function as an argument, has an inner function, and returns the inner function
# Demo examples of the decorator with and without pie syntax '@'


def coupon_calculator(func):
    def wrapper():
        print("Base price: $35/hr")
        new_price = func(35.00)
        print(f"Price after coupon: ${new_price}/hour")

    return wrapper


def fifty_off(price):
    return "{:.2f}".format(round(price / 2, 2))


def twenty_percent_off(price):
    return "{:.2f}".format(round(price * 0.8))


# Without pie syntax
half_off = coupon_calculator(fifty_off)
half_off()
twenty_off = coupon_calculator(twenty_percent_off)
twenty_off()

# With pie syntax


@coupon_calculator
def ten_off(price):
    return "{:.2f}".format(round(price - 10, 2))


ten_off()
