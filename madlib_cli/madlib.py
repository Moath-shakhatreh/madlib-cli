import re

def intro():
   print('Welcome to Madlib game , this game take some words from you and reform the text pased on the user inputs')

def read_template(path) :
    try: 
     with open(path) as f : 
        rea = f.read()
        return rea
    except FileNotFoundError :
            raise



def parse_template(text):
 x = text
 empty = re.sub("{[^{}]+}","{}", x)
 words = re.findall(r'{([^}]+)}',x)
 return (empty,tuple(words))
    

# It was a {} and {} {}.

def merge(template,parts):
 template = template.format(*parts)
 return template




def prompts(lst):
   input_arr=[]
   for element in lst:
      user_input = input(f'enter a {element} ')
      input_arr.append(user_input)
   return input_arr       

def new_file(merged_template):
   with open("assets/result.text", "w") as f:
      f.write(merged_template)


if __name__ == '__main__' :
   intro()
   returned_content = read_template("assets/longText.txt")
   stripped, parts = parse_template(returned_content)
   user_prompts = prompts(parts)
   merged_txt = merge(stripped, user_prompts)
   print(merged_txt)
   new_file(merged_txt)
# read_template('assets/dark_and_stormy_night_template.txt')
# read_template('assets/moath.txt')