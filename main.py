from const import API_KEY, ZONE_ID
from cloudflare import list_records, delete_record, APIKEYERROR, ZONEIDNOTFOUND, DNSRECORDNOTFOUND


def main():

    try:
        all_records = list_records(ZONE_ID, API_KEY)
    except APIKEYERROR:
        print("Your API Key is Invalid, Please try again!")
    except ZONEIDNOTFOUND:
        print("Looks like you entered your ZONEID incorrectly, Please try again!")

    for record in all_records:
        # Since we are deleting for id that we just recieved from cloudflare,
        # We donot need to check for DNS Record ID errors, as they are correct
        # And other errors has already been checked above
        delete_record(ZONE_ID, record["id"], API_KEY)

if __name__ == "__main__":
    main()