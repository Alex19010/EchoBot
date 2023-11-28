from settings import URL
from pars import get_url_text, get_links, get_data

def main():
    html = get_url_text(url=URL)
    if html is None:
        print("URL isn't working")
        return None

    links = get_links(html=html)
    for link in links:
        html = get_url_text(url=link)
        if html is not None:
            try:
                data = get_data(html=html)
            except AttributeError as ex:
                print(f"{link} - There is a mistake or there isn't enough datas {ex}\n\n\n")
            else:
                print("\n\n", data, link, "\n")
                print("Datas are ok")
        else:
            print(f"{link} - aren't working")
    
if __name__ == "__main__":
    main()