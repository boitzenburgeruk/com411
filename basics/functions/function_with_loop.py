def cross_bridge(steps):
    for x in range(0, steps, 1):
        print("Crossed step!")
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")


cross_bridge(3)
cross_bridge(6)