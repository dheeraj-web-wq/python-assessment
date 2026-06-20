def add_item_buggy(item, cart=[]):
    cart.append(item)
    return cart


def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


def create_cart(owner: str, discount: float = 0) -> dict:
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart: dict, name: str, price: float, qty: int = 1) -> None:
    cart["items"].append({"name": name, "price": price, "qty": qty})
    print(f"Added to {cart['owner']}'s cart: {qty}x {name} @ ${price:.2f} each")


def update_price(price_tuple: tuple, new_price: float) -> None:
    print(f"Attempting to update price tuple {price_tuple} to {new_price}...")
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"Caught Expected Error: {e}")
        print(
            "Explanation: Tuples are immutable! Once created, their elements cannot be re-assigned, "
            "deleted, or modified. This makes them ideal for fixed records like keys or constants."
        )


def calculate_total(cart: dict) -> float:
    raw_total = sum(item["price"] * item["qty"] for item in cart["items"])
    discount_amount = raw_total * (cart["discount"] / 100.0)
    final_total = raw_total - discount_amount
    return final_total


def main():
    print("=== PART A: Demonstrating the Bug ===")
    print("Call 1 (apple):", add_item_buggy("apple"))
    print("Call 2 (banana):", add_item_buggy("banana"))
    print("Call 3 (milk, custom cart):", add_item_buggy("milk", cart=["bread"]))
    print("Call 4 (eggs):", add_item_buggy("eggs"))

    print("\n=== PART B: Demonstrating the Fix ===")
    print("Call 1 (apple):", add_item_fixed("apple"))
    print("Call 2 (banana):", add_item_fixed("banana"))
    print("Call 3 (milk, custom cart):", add_item_fixed("milk", cart=["bread"]))
    print("Call 4 (eggs):", add_item_fixed("eggs"))

    print("\n=== PART C: Complete Shopping Cart Demonstration ===")
    cart_alice = create_cart("Alice", discount=10)
    cart_bob = create_cart("Bob", discount=0)
    
    add_to_cart(cart_alice, "Laptop", 999.99, 1)
    add_to_cart(cart_alice, "Mouse", 25.50, 2)
    
    add_to_cart(cart_bob, "Book", 12.99, 3)
    
    print("\n--- Cart Status Verification ---")
    print(f"Alice's Cart: {cart_alice}")
    print(f"Bob's Cart: {cart_bob}")
    
    total_alice = calculate_total(cart_alice)
    total_bob = calculate_total(cart_bob)
    
    print(f"\nAlice's Final Total (with 10% discount): ${total_alice:.2f}")
    print(f"Bob's Final Total: ${total_bob:.2f}")
    
    print("\n--- Tuple Immutability Check ---")
    price_info = (50.0, "USD")
    update_price(price_info, 45.0)


if __name__ == "__main__":
    main()


# ==============================================================================
# DISCUSSION POINTS
# ==============================================================================
#
# 1. Why is discount=0 safe but cart=[] dangerous?
#    - discount=0 uses an integer (0), which is an immutable type. Even if the parameter value is
#      re-assigned inside the function, the original default value (0) itself cannot be mutated.
#    - cart=[] uses a list, which is a mutable type. When Python evaluates the function definition,
#      it creates a single list object. If you modify this list (e.g. by appending to it), the change
#      persists in the default parameter object across subsequent function calls.
#
# 2. What is the difference between rebinding and mutating?
#    - Rebinding (or re-assignment) changes which object a reference (name) points to. For example,
#      `x = [1, 2]` followed by `x = [3, 4]` rebinds `x` to a completely new list object. The original
#      list `[1, 2]` is unchanged.
#      Inside a function, doing `cart = []` rebinds the local name `cart` to a new empty list.
#    - Mutating alters the state of the existing object in-place without changing its memory address.
#      For example, `x.append(3)` or `x[0] = 99` mutates the list object that `x` points to.
#
# 3. Which of these are mutable? — list, tuple, dict, set, str, int
#    - Mutable: list, dict, set
#    - Immutable: tuple, str, int
#
# 4. When you pass a list into a function and modify it, do changes reflect outside? Why?
#    - Yes, changes reflect outside the function.
#    - Why: Python uses "call-by-sharing" (also known as pass-by-object-reference). When you pass a
#      list to a function, Python passes a reference to the existing list object. It does not make a copy.
#      Therefore, any mutation performed on the list inside the function (like `.append()`, `.pop()`,
#      or item assignment) directly alters the shared object in memory, which is visible outside the function.
#      However, if you rebind the parameter (e.g. `cart = [1, 2]`), you are changing the local reference
#      to point to a new object, which does NOT affect the original list outside the function.
#
