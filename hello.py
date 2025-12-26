def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def main():
    message = greet("World")
    print(message)


if __name__ == "__main__":
    main()
