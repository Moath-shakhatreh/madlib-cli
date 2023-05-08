import re
def read_template(path) :
    print('Welcome to Madlib game')
    try: 
     with open(path) as f : 
        rea = f.read()
        return rea
    except FileNotFoundError :
            raise


# if __name__ == '__main__' :
# read_template('assets/dark_and_stormy_night_template.txt')
# read_template('assets/moath.txt')

def parse_template(text):
 x = text
 empty = re.sub("{[^{}]+}","{}", x)
 words = re.findall(r'{([^}]+)}',x)
 return (empty,tuple(words))
    

# It was a {} and {} {}.

def merge(text,tup):
 l1 = text
 for x in tup :
    l1 = l1.replace('{}',x,1) 
    
 return l1





        
