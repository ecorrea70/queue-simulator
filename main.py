from pseudorandom_number_generator import generate_random_numbers

def main():
    quantity = 100  # You can change this value as needed
    
    print(f"Generating {quantity} pseudo-random numbers...")
    random_numbers = generate_random_numbers(quantity)
    
    print(f"\nFirst 5 generated numbers:")
    for i, num in enumerate(random_numbers[:5], 1):
        print(f"{i}: {num:.10f}")
    
    print(f"\nLast 5 generated numbers:")
    for i, num in enumerate(random_numbers[-5:], len(random_numbers)-4):
        print(f"{i}: {num:.10f}")
    
    print(f"\nTotal of generated numbers: {len(random_numbers)}")

if __name__ == "__main__":
    main()
