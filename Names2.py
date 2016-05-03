#Names II
#David Cannady
#Create a program that manipulates dictionaries
#5/2/16 -DSC

users = {
'Students': [
    {'fname' : 'Michael', '1name' : 'Jordan'},
    {'fname' : 'John' , '1name' : 'Rosales'},
    {'fname' : 'Mark' , '1name' : 'Guillen'},
    {'fname' : 'KB' , '1name' : 'Tone1'}
],
'Instructor': [
    'Instructors':[
    {'fname' : 'Michael', '1name' : 'Choi'},
    {'fname' : 'Martin' , '1name' : 'Puryear'}
    ]
}
#iterate thru students and print first name, last name
def printStudentAndTeachersNames(dict):
    # get keys // Students; Instructors
    # for each key, get val: iter thru each val array
    for k, data in dict.items():
        print k
        for i in range(0, len(data)):
            name = ""
            for val in data[i].itervalues():
                name += val + ""
                #end i
                print str(i) + " - " + name.upper() + "- " + str(len(name))
            #end k, data
        #end def
# run the code
print "\n" *25
printStudentsAndTeachersNames(users)
print "\n\nexiting..."
