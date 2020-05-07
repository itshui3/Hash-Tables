def expensive_seq(x, y, z):
    # Implement me
     if x <= 0: return y + z
     if x > 0: 
         return expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
# Similar to caching fibonacci, I want to cache pre-calculated values so that they don't have to be recalculated
# Downstream of the recursive chain
# I need to determine which values are calculated often
# I need to determine how to reference check to see if they're already cached
if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
# Fast way would be to look up how to do fibonacci caching and copy the understanding from that