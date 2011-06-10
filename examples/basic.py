import rainmaker

def main():
    # Create a rainmaker object for use
    r = rainmaker.RainMaker('YOUR_API_KEY_HERE')

    # Get the results of a lookup
    rain = r.do_lookup()

    # Display the results of the lookup
    print rain

if __name__ == "__main__":
    main()
