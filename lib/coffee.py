#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float):
        self.size = size
        self.price = price

    @property
    def size(self) -> str:

        """Getter for size attribute."""
        return self._size

    @size.setter
    def size(self, value: str):
        """Setter that restricts input strictly to Small, Medium, or Large."""
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            self._size = "Medium"  

    def tip(self):
        """Prints a tip message and raises the coffee price by 1."""
        print("This coffee is great, here’s a tip!")
        self.price += 1


# Optional test ru
if __name__ == "__main__":
    print("Testing Coffee Class Execution:")
    latte = Coffee("Large", 4.50)
    print(f"Coffee ordered: {latte.size} | Initial Cost: ${latte.price:.2f}")
    latte.tip()
    print(f"Updated Cost: ${latte.price:.2f}")

    print("\nTesting Validation Trigger:")
    invalid_coffee = Coffee("Extra-Large", 5.00)