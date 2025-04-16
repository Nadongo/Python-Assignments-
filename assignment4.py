# Simple File Read and Write Program

# Ask user for input filename
input_filename = input("Enter the input filename: ")

try:
    # Open and read the file
    file = open(input_filename, "r")
    content = file.read()
    file.close()
    
    # Convert content to uppercase
    modified_content = content.upper()
    
    # Ask user for output filename
    output_filename = input("Enter the output filename: ")
    
    # Write to the new file
    output_file = open(output_filename, "w")
    output_file.write(modified_content)
    output_file.close()
    
    print(f"Success! Modified content written to {output_filename}")
    
except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except Exception as e:
    print(f"Error: {e}")

print("Program completed.")