from itertools import combinations

class CipherTextError(Exception):
    """Base class for cipher text errors."""
    pass

class NonDigitInputError(CipherTextError):
    pass

class LengthNotDivisibleError(CipherTextError):
    pass

class SubsetDivisibilityError(CipherTextError):
    pass

def validate_cipher(ciphertext: str, num_subsets: int, digit_divisor: int):
    if not ciphertext.isdigit():
        raise NonDigitInputError("Cipher text must contain only digits.")

    total_length = len(ciphertext)
    
    if total_length % num_subsets != 0:
        raise LengthNotDivisibleError(f"Total length ({total_length}) must be divisible by number of subsets ({num_subsets}).")

    subset_length = total_length // num_subsets

    if subset_length % digit_divisor != 0:
        raise SubsetDivisibilityError(
            f"Each subset must have a number of digits divisible by {digit_divisor}, but got {subset_length} digits per subset."
        )

    subsets = []
    for i in range(0, total_length, subset_length):
        chunk = ciphertext[i:i + subset_length]
        subsets.append(chunk)

    return subsets

def split_into_chunks(subset: str, chunk_size: int):
    return [int(subset[i:i+chunk_size]) for i in range(0, len(subset), chunk_size)]

def all_subset_sums(nums):
    sums = set()
    for r in range(1, len(nums) + 1):
        for combo in combinations(nums, r):
            sums.add(sum(combo))
    return sums

def mssp_decode(ciphertext: str, n: int, d: int):
    subsets = validate_cipher(ciphertext, n, d)
    
    all_sums = []
    for subset in subsets:
        nums = split_into_chunks(subset, d)
        sums = all_subset_sums(nums)
        all_sums.append(sums)
    
    # Find shared sums in all subsets
    common_sums = set.intersection(*all_sums)

    if not common_sums:
        return "No shared sum found"
    
    # Return the smallest shared sum (or sorted string of all if needed)
    return ''.join(str(x) for x in sorted(common_sums))

def main():
    try:
        #55495458205016966826278532461565 -> 4,2 = 112
        #799983342767152577242663441740985671678720845472559646208978678249295875506162204711109183474250893534771926 -> 4,3 = 2942
        ciphertext = input("Enter ciphertext (digits only): ").strip()
        n = int(input("Enter number of subsets (n): "))
        d = int(input("Each subset must have digits count divisible by (d): "))

        plaintext = mssp_decode(ciphertext, n, d)
        print(f"Decoded plaintext: {plaintext}")

    except CipherTextError as e:
        print(f"CipherText Error: {e}")
    except ValueError as e:
        print(f"Input Error: Expected a number - {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
