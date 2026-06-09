class Book:
    def __init__(self, title: str, page_count: int):
        self.title = title
        # Assigning to self.page_count passes the value through the validation setter below
        self.page_count = page_count

    @property
    def page_count(self) -> int:
        """Getter for page_count attribute."""
        return self._page_count

    @page_count.setter
    def page_count(self, value: int):
        """Setter that enforces page_count must be an integer."""
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
            # Assigning a safe default value so the program doesn't break entirely
            self._page_count = 0 

    def turn_page(self):
        """Prints a reading message."""
        print("Flipping the page...wow, you read fast!")


# Optional test run
if __name__ == "__main__":
    print("Testing Book Class Execution:")
    novel = Book("The Great Gatsby", 180)
    print(f"Book Title: {novel.title} | Total Pages: {novel.page_count}")
    novel.turn_page()

    print("\nTesting Validation Trigger:")
    invalid_book = Book("Invalid Test", "One Hundred Pages")
        