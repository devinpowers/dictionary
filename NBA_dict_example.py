''' NBA Example, Like lab 9'''

''' Using Dictionaries'''

def build_map( in_file1, in_file2 ):
    
    ''' Take both files and read them, build Dictionary'''
    data_map = {}
    # skip headers in both files
    in_file1.readline()
    in_file2.readline()

    #READ EACH LINE FROM FILE 1
    for line in in_file1:   
        # Skip empty line in txt file
        if len(line) > 1:
    
            cities_list = line.strip().split()
          
            # Discard whitespace
            city = cities_list[0].strip()
            team = cities_list[1].strip()

            if city not in data_map:
                data_map[city] = {}

            if team not in data_map[city]:         
                data_map[city][team] = []

     #READ EACH LINE FROM FILE 2    
     
    for line in in_file2:
        # Skip if empty line in txt file
        if len(line) > 1:
     
            team_list = line.strip().split()
            #Convert to Title case, discard whitespace
            team = team_list[0].strip().title()
            player = team_list[1].strip().title()
            
            # insert player (team is guaranteed to be in map)
            for city in data_map:    # Looking through each Key
          
                if team in data_map[city]:
             
                    if player not in data_map[city][team]:
                
                        data_map[city][team].append(player)
                        
  
    return data_map


def display_map( data_map ):
    
    ''' Display Dictionary Values '''
    
    
    for city, teams in sorted(data_map.items()):
        
        print(f'{city}:')
        
        for team, players in sorted(teams.items()):
            
        
            output_players = ', '.join(sorted(players))
            
            print(f'    {team} --> {output_players}')
    

def open_file():
    '''open files, try and except suite '''
    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

def main():
    '''Call to open files and run other functions  '''

    # Empty Initial Dictionary
    data_map = {}
    in_file1 = open_file() # NBA_Cities File
    in_file2 = open_file() # players.txt File

    # if both Files exist then:
    if in_file1 != None and in_file2 != None:    
        
        data_map = build_map( in_file1, in_file2 ) # call build_map function
        display_map( data_map )
        in_file1.close()   #close file
        in_file2.close()   #close file
        
if __name__ == "__main__":
    main()
    

