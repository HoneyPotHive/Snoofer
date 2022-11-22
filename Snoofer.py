from snooferfunctions import *

#Target directory in which you want to scan txt and docx files
path2 = (r"C:\Test")

def main(path):
    functions.builddb()
    print("========================================================================")
    print(" ============= B U I L T   B A D   P W D   D B")
    functions.db()
    print("  ============  T O T A L   P W D S   "+ str(len(badpassworddb)))
    functions.locate(path)
    functions.exporting()
main(path2)
