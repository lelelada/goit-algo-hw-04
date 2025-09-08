import timeit
import random

# --- Реалізація алгоритмів ---
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# --- Тестування та збір даних ---
test_data = {
    "малий (100)": [random.randint(0, 1000) for _ in range(100)],
    "середній (10000)": [random.randint(0, 10000) for _ in range(10000)],
    "великий (1000000)": [random.randint(0, 1000000) for _ in range(1000000)]
}

results = {}

for size, data in test_data.items():
    print(f"\n--- Тестування на масиві розміром {size} ---")
    results[size] = {}

    # Insertion Sort
    if size == "малий (100)" or size == "середній (10000)":
        t = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        results[size]["Insertion Sort"] = t
        print(f"Insertion Sort: {t:.6f} сек")
    else:
        results[size]["Insertion Sort"] = "надто довго"
        print("Insertion Sort: надто довго для великого масиву")

    # Merge Sort
    t = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    results[size]["Merge Sort"] = t
    print(f"Merge Sort: {t:.6f} сек")
    
    # Timsort (вбудований)
    t = timeit.timeit(lambda: sorted(data.copy()), number=1)
    results[size]["Timsort (sorted)"] = t
    print(f"Timsort (sorted): {t:.6f} сек")

print("\n--- Зведені результати (час в секундах) ---")
print("{:<20} {:<20} {:<20} {:<20}".format("Розмір масиву", "Insertion Sort", "Merge Sort", "Timsort"))
for size, res in results.items():
    print("{:<20} {:<20} {:<20} {:<20}".format(
        size, 
        f"{res.get('Insertion Sort', 'N/A'):.6f}" if isinstance(res.get('Insertion Sort'), float) else str(res.get('Insertion Sort', 'N/A')), 
        f"{res['Merge Sort']:.6f}", 
        f"{res['Timsort (sorted)']:.6f}"
    ))