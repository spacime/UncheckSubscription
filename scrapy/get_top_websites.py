def get_top_websites():
    file_in = open("Quantcast-Top-Million.txt", "r")
    file_out = open("Top_Viewed_Websites.txt", "w")

    for line in file_in:
        if "Hidden profile" in line:
            continue
        words = line.split("\t")
        file_out.write(words[1])

    file_in.close()
    file_out.close()

def main():
    get_top_websites()

if __name__ == '__main__':
    main()