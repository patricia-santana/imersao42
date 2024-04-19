###my_sort.py
def sort_by_year(input):    
    sorted_dict = input.copy()    
    return dict(sorted(input.items(), key = lambda x:x[1]))

def group_by_year(input ):                
    grouped_dict = {}
    for name, year in input.items():        
        if year not in grouped_dict:
            grouped_dict[year] = []        
        grouped_dict[year].append(name)
        grouped_dict[year].sort()
    
    return grouped_dict
        
def main():
    d = {
        'Hendrix' : '1942',
        'Allman' : '1946',
        'King' : '1925',
        'Clapton' : '1945',
        'Johnson' : '1911',
        'Berry' : '1926',
        'Vaughan' : '1954',
        'Cooder' : '1947',
        'Page' : '1944',
        'Richards' : '1943',
        'Hammett' : '1962',
        'Cobain' : '1967',
        'Garcia' : '1942',
        'Beck' : '1944',
        'Santana' : '1947',
        'Ramone' : '1948',
        'White' : '1975',
        'Frusciante': '1970',
        'Thompson' : '1949',
        'Burton' : '1939',
    }
        
    sorted_by_year = sort_by_year(d)
    grouped_by_year = group_by_year(sorted_by_year)

        
    print('Ordered by Year')
    for name,year in sorted_by_year.items():
        print(name)
            
    print('\nGrouped by Year')
    for year,names in grouped_by_year.items():
        print(', '.join(names))
            
main()
###fim my_sort.py
