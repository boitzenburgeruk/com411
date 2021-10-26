def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    print(f"Minimum likelihood of falling: {min(likelihoods)}%")
    print(f"Maximum likelihood of falling: {max(likelihoods)}%")


if __name__ == "__main__":
    likelihood()