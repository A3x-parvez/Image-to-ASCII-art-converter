import pywhatkit as kit
import os

def Ascii_art(img,img_name):
     try:
        # Convert image to ASCII art using pwwhatkit module.
        ascii_img = kit.image_to_ascii_art(img)
        
        # extract the name from the image file.
        name = img_name.rsplit('.', 1)[0]
        
        # Save the ASCII art to a file into output folder
        with open("output_file\ "+name+"-ascii-art.txt", "w") as f:
            f.write(ascii_img)
        
        # Print the ASCII art
        print(ascii_img)
        
     except Exception as e:
        print(f"An error occurred: {e}")
  
#main area  
if __name__ == "__main__":   
     print("\n\n  --Image To ASCII Art converter--")
     print("# Step-1 : At first move the input image into the input_img folder.")
     print("# Step-2 : Give the name of the Image-file (ex:demo.jpg).")
     print("# Step-3 : You can get your output file as .txt inside the output_file.")
     print("-------------------------------------------------------------------------")
     
     img_name=input("Enter the img file : ")
     
     img_path= f"input_img/{img_name}"
     Ascii_art(img_path,img_name)
