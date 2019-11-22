#! /usr/bin/python3


def read_gwas_term_list_file():
    ''' 
    Read content of file with GWAS 
    EFO terms extracted from database.
    '''
    with open('gwas-terms-IRIs.txt', 'r') as f:
        # terms = f.read().splitlines()
        terms = [line.strip() for line in f]
        print("DB terms: {}").format(len(terms))
        return terms


def read_gwas_slim_list_file():
    '''
    Read content of file with IRIs from 
    EFO slim of GWAS extracted terms.
    '''
    with open('class_list.txt', 'r') as f:
        slim_terms = f.read().splitlines()
        print("Slim terms: {}").format(len(slim_terms))
        return slim_terms


def compare_lists(a,b):
    '''
    Compare lists to find any terms missing in EFO Slim.
    '''
    missing_terms = list(set(a) - set(b))
    print("Mising terms: {}").format(missing_terms)


if __name__ == '__main__':
    db_terms = read_gwas_term_list_file()
    slim_terms = read_gwas_slim_list_file()
    compare_lists(db_terms, slim_terms)

