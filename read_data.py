import logging
# Importing models and REST client class from Community Edition version


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = ""

# Default Tenant Administrator credentials
username = ""
password = ""

# Creating the REST client object with context manager to get auto token refresh
with RestClientCE(base_url=url) as rest_client:
    try:
        # Auth with credentials
        rest_client.login(username=username, password=password)
        """ # Creating an Asset
        asset = Asset(name="Building 1", type="building")
        asset = rest_client.save_asset(asset)

        logging.info("Asset was created:\n%r\n", asset)

        # creating a Device
        device = Device(name="Thermometer 1", type="thermometer")
        device = rest_client.save_device(device)

        logging.info(" Device was created:\n%r\n", device)

        # Creating relations from device to asset
        relation = EntityRelation(_from=asset.id, to=device.id, type="Contains")
        relation = rest_client.save_relation(relation)

        logging.info(" Relation was created:\n%r\n", relation)
        """
        asset_types = rest_client.get_asset_types()
        assets = []
        for asset_type in asset_types:
            if asset_type["type"] == "ASSET":
                asset_type = asset_type["type"]
                asset_list = rest_client.get_entities(asset_type)
                assets.extend(asset_list)
        for asset in assets:
            print(asset["name"])
    except ApiException as e:
        logging.exception(e)
