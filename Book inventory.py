
class Book:

    def __init__(self):
        self.title=""
        self.author=""
        self.cost=0.0
        self.isbn=0

    def check_isbn(self):
        s=0
        for a in self.isbn:
            s+=len(a)
        if s!=10:
            return False
        else:
            l,S=1,0
            for a in self.isbn[:len(self.isbn)-1:]:
                for b in a:
                    S+=(l*int(b))
                    l+=1
            return S%11==int(self.isbn[len(self.isbn)-1])

    def get_book(self):
        self.title=raw_input("Enter title of book:")
        self.author=raw_input("Enter author name:")
        self.cost=float(raw_input("Enter cost:"))
        self.isbn=raw_input("Enter ISBN code(separated by hyphens):").strip().split('-')

    def display_book(self):
        print "==========","Book ID-","".join(self.isbn),"=========="
        print "Title- ",self.title
        print "Author- ",self.author
        print "Price- ",self.cost
        print "ISBN- ",'-'.join(self.isbn)



def MENU():
    print "\n-----------MENU----------\n1.Add Books\n2.Delete Books\n3.Modify Books\n4.Sort according to.....\n"

def sort_MENU():
    print "\nSort according to.....\n1.Price:highest to lowest\n2.Price:lowest to highest\n3.Title:A>>>Z\n4.Title:Z>>>A\n"



def del_book():
    global B
    ch=int(raw_input("Which of the following do you know about the book you want to delete??\n1.Title\n2.Author\n3.Cost\n4.ISBN\nEnter your choice:"))
    if ch==1:
        t=raw_input("Enter title:")
        for b in B:
            if b.title==t:
                B.remove(b)
    elif ch==2:
        a=raw_input("Enter author:")
        for b in B:
            if b.author==a:
                B.remove(b)

    elif ch==3:
        c=int(raw_input("Enter cost:"))
        for b in B:
            if b.cost==c:
                B.remove(b)

    elif ch==4:
        i=raw_input("Enter ISBN code(separated by hyphens):").strip().split('-')
        for b in B:
            if b.isbn==i:
                B.remove(b)

    else:
        print "Please enter proper choice"

def sort_price_asc(B):
    if len(B)==1:
        print "Sorted successfully"
    else:
        result,l,r=[],sort_price_asc(B[:len(B)/2:]),sort_price_asc(B[len(B)/2::])
        while len(l)>0 and len(r)>0:
            if l[0].cost()>r[0].cost():
                result.append(r.pop(0))
            else:
                result.append(l.pop(0))
        result.extend(l+r)
        B=result[:]
        print "Sorted successfully"
        
    
def sort_price_dsc(B):
    if len(B)==1:
        print "Sorted successfully"
    else:
        result,l,r=[],sort_price_asc(B[:len(B)/2:]),sort_price_asc(B[len(B)/2::])
        while len(l)>0 and len(r)>0:
            if l[0].cost()<r[0].cost():
                result.append(r.pop(0))
            else:
                result.append(l.pop(0))
        result.extend(l+r)
        B=result[:]
        print "Sorted successfully"

def sort_title_asc(B):
    if len(B)==1:
        print "Sorted successfully"
    else:
        result,l,r=[],sort_price_asc(B[:len(B)/2:]),sort_price_asc(B[len(B)/2::])
        while len(l)>0 and len(r)>0:
            if l[0].title()>r[0].title():
                result.append(r.pop(0))
            else:
                result.append(l.pop(0))
        result.extend(l+r)
        B=result[:]
        print "Sorted successfully"

def sort_title_dsc(B):
    if len(B)==1:
        print "Sorted successfully"
    else:
        result,l,r=[],sort_price_asc(B[:len(B)/2:]),sort_price_asc(B[len(B)/2::])
        while len(l)>0 and len(r)>0:
            if l[0].title()<r[0].title():
                result.append(r.pop(0))
            else:
                result.append(l.pop(0))
        result.extend(l+r)
        B=result[:]
        print "Sorted successfully"




B=[]

while True:
    MENU()
    try:
        ch=int(raw_input("Enter your choice:"))
        if ch<1 or ch>4:
            print "Please enter a proper choice in 1,2,3,4"
            continue
        elif ch==1:
            
            
    except ValueError:
        print "Please enter a proper choice in 1,2,3,4"
        continue
    
        



    

        

    
        
        
        
