from const import API_KEY, ZONE_ID
from cloudflare import list_records, delete_record


def main():
    all_records = list_records(ZONE_ID, API_KEY)

    for record in all_records:
        delete_record(ZONE_ID, record["id"], API_KEY)

if __name__ == "__main__":
    main()