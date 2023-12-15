import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in 
      the given CSV file.
    """
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        csv_reader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
        
        # Read only the first row (field names)
        fieldnames = next(csv_reader)
        
    return fieldnames

def read_csv_as_list_dict(filename, separator, quote):
    """
    
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    data = []  # List to store dictionaries

    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        csv_reader = csv.reader(csvfile, delimiter=separator, quotechar=quote)

        # Read the field names from the first row
        fieldnames = next(csv_reader)

        for row in csv_reader:
            # Create a dictionary mapping field names to row values
            row_dict = {fieldnames[i]: row[i] for i in range(min(len(fieldnames), len(row)))}
            data.append(row_dict)

    return data

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the 
      field values for that row.
    """
    data = {}  # Dictionary to store dictionaries

    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        csv_reader = csv.reader(csvfile, delimiter=separator, quotechar=quote)

        # Read the field names from the first row
        fieldnames = next(csv_reader)

        # Find the index of the key field
        key_index = fieldnames.index(keyfield)

        for row in csv_reader:
            # Create a dictionary mapping field names to row values
            row_dict = {fieldnames[i]: row[i] for i in range(min(len(fieldnames), len(row)))}

            # Use the key field value as the key for the outer dictionary
            key_value = row[key_index]
            data[key_value] = row_dict

    return data


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile, delimiter=separator, quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)

        # Write the header row with fieldnames
        csv_writer.writerow(fieldnames)

        # Write each row in the table
        for row in table:
            # Extract values from the row dictionary in the order of fieldnames
            row_values = [row[field] for field in fieldnames]
            
            # Write the row to the CSV file
            csv_writer.writerow(row_values)