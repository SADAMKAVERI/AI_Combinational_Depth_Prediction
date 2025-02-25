# Utility Functions
import os

def list_rtl_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.v')]

if __name__ == "__main__":
    print("Utility module")
