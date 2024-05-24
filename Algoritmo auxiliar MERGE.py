def merge_sort(A):
  if len(A) > 1:
      mid = len(A) // 2
      L = A[:mid]
      R = A[mid:]

      merge_sort(L)
      merge_sort(R)

      merge(A, L, R)

def merge(A, L, R):
  i = j = k = 0

  while i < len(L) and j < len(R):
      if L[i] < R[j]:
          A[k] = L[i]
          i += 1
      else:
          A[k] = R[j]
          j += 1
      k += 1

  while i < len(L):
      A[k] = L[i]
      i += 1
      k += 1

  while j < len(R):
      A[k] = R[j]
      j += 1
      k += 1

# Example usage:
A = [2, 4, 5, 7, 1, 2, 3, 6]
merge_sort(A)
print("Sorted array:", A)
