def swap_ends(L, k):
   if k <= 0 or len(L) == 0 or k > len(L) // 2:
      return L.copy(),0

   new_l = L.copy()
   new_l[:k], new_l[-k:] = L[-k:], L[:k]

   return new_l, k






