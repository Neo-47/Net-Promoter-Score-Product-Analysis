import pandas as pd


def check_csv(csv_name):
    """ Checks if a CSV has three columns: response_date, user_id, nps_rating

    Args:
        csv_name (str): The name of the CSV file.

    Returns:
        Boolean: True if the CSV is valid, False otherwise 
    """
    # Open csv_name as f using with open
    with open(csv_name, 'r') as f:
        first_line = f.readline()
        # Return true if the CSV has the three specified columns
        if first_line == "response_date,user_id,nps_rating\n":
            return True
        # Otherwise, return false    
        else:
            return False



def categorize_nps(x):
    """ 
    Takes a NPS rating and outputs whether it is a "promoter", 
    "passive", "detractor", or "invalid" rating. "invalid" is
    returned when the rating is not between 0-10.

    Args:
        x: The NPS rating

    Returns:
        String: the NPS category or "invalid".
    """
    # Write the rest of the function to match the docstring
    if(x >= 0 and x <= 6):
        return "detractor"
    elif(x == 7 or x == 8):
        return "passive"
    elif(x == 9 or x == 10):
        return "promoter"
    else:
        return "invalid"



def convert_csv_to_df(csv_name, source_type):    
    """ Convert an NPS CSV into a DataFrame with columns for the source and NPS group.

    Args:
        csv_name (str): The name of the NPS CSV file.
        source_type (str): The source of the NPS responses.

    Returns:
         A DataFrame with the CSV data and columns: source and nps_group.
    """
    df = pd.read_csv(csv_name)
    df['source'] = source_type
    # Define a new column nps_group which applies categorize_nps to nps_rating
    df['nps_group'] = df['nps_rating'].apply(categorize_nps)
    return df




def combine_nps_csvs(csvs_dict):
    # Define combine as an empty DataFrame
    combined = pd.DataFrame()
    # Iterate over csvs_dict to get the name and source of the CSVs
    for csv_file, source in csvs_dict.items():
        # Check if the csv is valid using check_csv()
        if check_csv(csv_file):
            # Convert the CSV using convert_csv_to_df() and assign it to temp
            temp = convert_csv_to_df(csv_file, source)
            # Concatenate combined and temp and assign it to combined
            combined = pd.concat([combined, temp])
        # If the file is not valid, print a message with the CSV's name
        else:
            print(csv_file + " is not a valid file and will not be added.")
    # Return the combined DataFrame
    return combined


# Define a function calculate_nps that takes a DataFrame
def calculate_nps(df):
    # Calculate the NPS score using the nps_group column 
    count = df['nps_group'].value_counts()
    promoters = count['promoter']
    detractors = count['detractor']
    # Return the NPS Score
    return ((promoters - detractors) / len(df['nps_group'])) * 100



# Define a function calculate_nps_by_source that takes a DataFrame
def calculate_nps_by_source(df):
    # Group the DataFrame by source and apply calculate_nps()
    a = df.groupby(['source']).apply(calculate_nps)
    # Return a Series with the NPS scores broken by source
    return a

