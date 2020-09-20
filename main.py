import os  #after importing os we can work on our system dirs and etc

def isBinod(filename):
    with open(filename, "r") as f: #to open a file
        file_content = f.read()    #reading content of file 

# To detect all forms of binod
    if 'binod' in file_content.lower():
        return True
    else:
        return False


if __name__ == "__main__":
# Listing the content of this folder 
    dir_contents = os.listdir()   
    nbinod = 0
#for each text file run isBinod for them 
    for item in dir_contents:
        if item.endswith('txt'):     
            print(f"Detecting binod in {item}")
            flag = isBinod(item)
            if flag:
                print(f"Binod found in {item}")
                nbinod += 1
            else:
                print(f"Binod not found in {item}")
    
    print("*********Binod Detector Summary***********")
    print(f"{nbinod} files found with binod hidden into them.")