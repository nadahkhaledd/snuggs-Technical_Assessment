cities = ['cairo', 'alexandria']
companies = ['xyz shipping', 'dxb shipping']
companies_cities_mapping = {'xyz shipping': {'cairo': 'C', 'alexandria': 'A'},
                            'dxb shipping': {'cairo': 'CAI', 'alexandria': 'ALX'}}

def get_city_mapping(city_name: str, shipping_company_name: str) -> str:
    """Returns the city mapping format for the specified shipping company.

            Parameters:
                    city_name (str): string with the full name of the city
                    shipping_company_name (str): string with the full name of the specified shipping company

            Returns:
                    city_mapping (str): mapping format for the city that corresponds to the shipping company"""

    if companies_cities_mapping.keys().__contains__(shipping_company_name.lower()):
        if companies_cities_mapping.get(shipping_company_name.lower()).__contains__(city_name.lower()):
            return companies_cities_mapping.get(shipping_company_name.lower()).get(city_name.lower())
        else:
            return 'invalid or non-found city name'
    else:
        return 'invalid or non-found shipping company name'


print(get_city_mapping('Cairo', 'dxb Shipping'))