# Currency rate lib

## About library

This library put date from Pirvat24 and Monobank banks api, parse it and can save them in json or csv file

## Available methond
- main
- get_values_for_date_from_api
- get_values_for_range_date_from_api
- parse_by_date
- parse_by_range_date
- save_to_csv_file
- save_to_json_file

## About methods


1. ``main``
   This method save result in csv file and have 6 parames
   - start_date - range start date
   - end_date - range end date (if not input result will be only for start_date date)
   - to_csv - will save to csv file if value = True (By default False)will save 
   - to_json - will save to json file if value = True (By default False)
   - add_graph - (Available onlu for range) will show graph values currencies for range if value = True (By default False)
   - path_where_save - it path to directory where save results
2. ``save_to_csv_file``

    This method save result in csv file and have 4 parames 
   - currency_rate - date which save
   - start_date - for which date get rates (if the date range it is beginning date)
   - end_date - it is beginning date of range
   - path - it path where save results
3. ``save_to_json_file``

    This method save result in csv file and have 4 parames
   - currency_rate - date which save
   - start_date - for which date get rates (if the date range it is beginning date)
   - end_date - it is beginning date of range
   - path - it path where save results
4. ``get_values_for_date_from_api``

    This method sent request to api, return json data and have 1 parametr
   - date - date for which get rates

5. ``get_values_for_range_date_from_api``

    This method sent request to api, return json data and have 2 parames
   - start_date - range start date
   - end_date - range end date
   
6. ``parse_by_date``    
   This method parse data from request and have 3 parames
   - date - date for which get rates
7. ``parse_by_range_date``  
   This method parse data from request and have 3 parames
   - start_date - range start date
   - end_date - range end date

